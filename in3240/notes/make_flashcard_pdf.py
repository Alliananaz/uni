#!/usr/bin/env python3
"""
make_flashcard_pdf.py  (v3)
---------------------------
Changes from v2:
  - Q side: auto-picks the largest font that fits (16 → 14 → 12 → 10 pt),
    then centers the question both horizontally and vertically in the card.
  - Rows are stretched equally to fill the page when it is >= 60% full.
    Pages that are mostly empty (last/sparse page) are left as-is.

Print: Two-sided / Duplex -> Flip on Long Edge (portrait).
Cut:   1 vertical line + N horizontal lines per sheet.
Each cut piece = QUESTION one face, ANSWER the other.
"""
import re
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Frame
from reportlab.pdfbase.pdfmetrics import stringWidth

# ── geometry ───────────────────────────────────────────────────────────────
W, H    = A4                             # 595.28 × 841.89 pt
CW      = W / 2                          # card width ≈ 105 mm
PAD     = 4.5 * mm                       # inner padding (all sides)
BANNER  = 11 * mm                        # coloured title band height
TOP_PAD = 3                              # pt gap between banner bottom and first text line
MIN_CH  = BANNER + 2 * PAD + TOP_PAD + 8 * mm   # absolute minimum card height

# Pages that are >= 60% filled get their rows stretched to fill completely.
# Pages below 60% full are left as-is (they're sparse / last-page offcuts).
STRETCH_MIN_FILL = 0.60

# ── colours ────────────────────────────────────────────────────────────────
Q_BC = HexColor('#1b3a5c')   # Q banner — deep navy
A_BC = HexColor('#1a5440')   # A banner — deep forest green
Q_BG = HexColor('#f3f6fb')   # Q background — pale blue
A_BG = HexColor('#f3fbf6')   # A background — pale green
CUT  = HexColor('#ababab')   # cut-guide colour

# ── A-side paragraph styles (8 pt, left-aligned) ───────────────────────────
sn  = ParagraphStyle('n',  fontName='Helvetica',      fontSize=8,   leading=10.2, spaceAfter=1.5)
sh  = ParagraphStyle('h',  fontName='Helvetica-Bold', fontSize=8.5, leading=11,   spaceAfter=2)
sm  = ParagraphStyle('m',  fontName='Courier',        fontSize=6.5, leading=8.5,  spaceAfter=1.5)
sli = ParagraphStyle('li', fontName='Helvetica',      fontSize=8,   leading=10.2,
                     leftIndent=9, firstLineIndent=-9, spaceAfter=1)
sni = ParagraphStyle('ni', fontName='Helvetica',      fontSize=8,   leading=10.2,
                     leftIndent=12, firstLineIndent=-12, spaceAfter=1)


# ── markdown helpers ───────────────────────────────────────────────────────
def _esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def _inl(t):
    t = _esc(t)
    t = re.sub(r'\*\*(.+?)\*\*',  r'<b>\1</b>',                              t)
    t = re.sub(r'\*([^*\n]+?)\*', r'<i>\1</i>',                              t)
    t = re.sub(r'`([^`\n]+?)`',   r'<font face="Courier" size="7">\1</font>', t)
    return t

def to_story(text):
    """Parse markdown into A-side flowables (8 pt, left-aligned)."""
    story, in_code, cbuf = [], False, []

    def flush():
        if cbuf:
            story.append(Paragraph('<br/>'.join(_esc(l) for l in cbuf), sm))
            cbuf.clear()

    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith('```'):
            if in_code: flush(); in_code = False
            else:        in_code = True
            continue
        if in_code:
            cbuf.append(raw); continue
        if re.match(r'^\|[\s\-:|]+\|$', s): continue
        if s.startswith('|') and s.endswith('|'):
            cells = [c.strip() for c in s[1:-1].split('|')]
            txt   = ' | '.join(_inl(c) for c in cells if c)
            if txt: story.append(Paragraph(txt, sn))
            continue
        m = re.match(r'^#{1,6}\s+(.*)', s)
        if m: story.append(Paragraph(_inl(m.group(1)), sh)); continue
        m = re.match(r'^[-*•]\s+(.*)', s)
        if m: story.append(Paragraph('• ' + _inl(m.group(1)), sli)); continue
        m = re.match(r'^(\d+)\.\s+(.*)', s)
        if m: story.append(Paragraph(m.group(1) + '. ' + _inl(m.group(2)), sni)); continue
        if not s: story.append(Spacer(1, 2.5)); continue
        story.append(Paragraph(_inl(s), sn))
    flush()
    return story


# ── Q-side font selection ──────────────────────────────────────────────────
# Try largest font first; pick the first that keeps the text within N lines.
_Q_CANDIDATES = [
    (16, 2),   # 16 pt  → ok if it wraps to ≤ 2 lines
    (14, 3),   # 14 pt  → ok if it wraps to ≤ 3 lines
    (12, 5),   # 12 pt  → ok if it wraps to ≤ 5 lines
    (10, 8),   # 10 pt  → ok if it wraps to ≤ 8 lines
]

def _q_params(text):
    """
    Return (font_size, leading, rendered_height) for the Q side.
    Picks the largest font that keeps the text within the line budget.
    """
    fw = CW - 2 * PAD
    for fs, max_lines in _Q_CANDIDATES:
        ld = round(fs * 1.3)
        st = ParagraphStyle('_q', fontName='Helvetica-Bold', fontSize=fs,
                            leading=ld, alignment=TA_CENTER)
        _, h = Paragraph(_inl(text), st).wrap(fw, 99999)
        if h <= ld * max_lines:
            return fs, ld, h
    # fallback: 10 pt, no line cap
    ld = round(10 * 1.3)
    st = ParagraphStyle('_q', fontName='Helvetica-Bold', fontSize=10,
                        leading=ld, alignment=TA_CENTER)
    _, h = Paragraph(_inl(text), st).wrap(fw, 99999)
    return 10, ld, h


# ── height measurement ─────────────────────────────────────────────────────
def min_q_card_h(text):
    """Minimum card height to fit a Q card (uses large centered font)."""
    _, _, ch = _q_params(text)
    raw = BANNER + 2 * PAD + TOP_PAD + ch + 3   # 3 pt safety
    return max(MIN_CH, min(H - 6 * mm, raw))

def min_a_card_h(text):
    """Minimum card height to fit an A card (uses 8 pt left-aligned text)."""
    fw    = CW - 2 * PAD
    total = 0.0
    for item in to_story(text):
        _, h = item.wrap(fw, 99999)
        total += h
        if isinstance(item, Paragraph):
            total += item.style.spaceAfter
    raw = BANNER + 2 * PAD + TOP_PAD + total + 3
    return max(MIN_CH, min(H - 6 * mm, raw))


# ── card renderer ──────────────────────────────────────────────────────────
def draw_card(c, ox, oy, rh, num, label, subtitle, body_md, bg, bc):
    """
    Draw one flashcard.
      ox, oy   = bottom-left corner (page coordinates)
      rh       = card height (row height after optional stretching)
      label    = 'Q' or 'A'
      subtitle = abbreviated question shown in banner on A cards; '' for Q cards
    """
    is_q = (label == 'Q')

    # background
    c.setFillColor(bg)
    c.rect(ox, oy, CW, rh, fill=1, stroke=0)
    # border
    c.setStrokeColor(HexColor('#c4c4c4'))
    c.setLineWidth(0.35)
    c.rect(ox, oy, CW, rh, fill=0, stroke=1)

    # banner strip at the top of the card
    by = oy + rh - BANNER
    c.setFillColor(bc)
    c.rect(ox, by, CW, BANNER, fill=1, stroke=0)

    # banner: Q / A label
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 14)
    c.drawString(ox + PAD, by + 3.1 * mm, label)

    # banner: card number (right-aligned)
    c.setFont('Helvetica-Bold', 7.5)
    c.drawRightString(ox + CW - PAD, by + 3.3 * mm, f'#{num}')

    # banner: subtitle (question preview on A cards)
    if subtitle:
        avail = CW - PAD * 2 - 17
        sub   = subtitle.replace('\n', ' ')
        while sub and stringWidth(sub, 'Helvetica', 6.5) > avail:
            sub = sub[:-4] + '...'
        c.setFont('Helvetica', 6.5)
        c.drawString(ox + PAD + 16, by + 3.3 * mm, sub)

    # body area: from oy+PAD (bottom) up to the banner bottom
    fw = CW - 2 * PAD
    fh = rh - BANNER - 2 * PAD    # total height available for body + topPad

    if fh <= 0:
        return

    if is_q:
        # ── Q side: large bold text, horizontally + vertically centered ───
        fs, ld, _ = _q_params(body_md)
        st = ParagraphStyle('q', fontName='Helvetica-Bold', fontSize=fs,
                            leading=ld, alignment=TA_CENTER)

        # Measure actual rendered height of this paragraph at this width
        p_measure = Paragraph(_inl(body_md), st)
        _, th = p_measure.wrap(fw, fh)

        # Vertical offset so the text block sits in the middle of the body area
        usable = fh - TOP_PAD            # height below the gap
        v_off  = max(0.0, (usable - th) / 2.0)

        # Build the story: spacer (top padding + centering offset) then paragraph
        story = []
        total_top = TOP_PAD + v_off
        if total_top > 0.5:
            story.append(Spacer(1, total_top))
        story.append(Paragraph(_inl(body_md), st))

        frame = Frame(ox + PAD, oy + PAD, fw, fh,
                      leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        frame.addFromList(story, c)

    else:
        # ── A side: 8 pt left-aligned text, flowing from the top ──────────
        frame = Frame(ox + PAD, oy + PAD, fw, fh,
                      leftPadding=0, rightPadding=0,
                      topPadding=TOP_PAD, bottomPadding=0)
        frame.addFromList(to_story(body_md), c)


# ── cut-guide renderer ─────────────────────────────────────────────────────
def draw_cuts(c, row_ys):
    """
    Draw dashed cut guides.
      row_ys : list of y-coordinates at the bottom of each row on this page.
    """
    c.saveState()
    c.setStrokeColor(CUT)
    c.setLineWidth(0.3)
    c.setDash([4.5, 3.5], 0)
    c.line(CW, 2.5 * mm, CW, H - 2.5 * mm)          # vertical centre
    for y in row_ys:
        if 2 * mm < y < H - 2 * mm:
            c.line(2.5 * mm, y, W - 2.5 * mm, y)     # horizontal per row
    c.setDash([], 0)
    c.setLineWidth(0.5)
    for y in row_ys:
        if 2 * mm < y < H - 2 * mm:
            d = 1.6 * mm
            c.line(CW - d, y, CW + d, y)
            c.line(CW, y - d, CW, y + d)
    c.restoreState()


# ── parser ─────────────────────────────────────────────────────────────────
def parse(md_path):
    text  = Path(md_path).read_text(encoding='utf-8')
    cards = []
    for blk in re.split(r'\n---\n', text):
        qm = re.search(r'\*\*Q:\*\*[ \t]*(.*?)(?=\n\*\*A:\*\*)', blk, re.DOTALL)
        am = re.search(r'\*\*A:\*\*[ \t]*(.*?)$',                 blk, re.DOTALL)
        if qm and am:
            cards.append((qm.group(1).strip(), am.group(1).strip()))
    return cards


# ── layout engine ──────────────────────────────────────────────────────────
def layout(cards):
    """
    Returns a list of sheets.
    Each sheet = list of (oy, rh, left_idx, right_idx_or_None).
    oy = bottom-left y of the row on the page.
    """
    print('  Measuring card heights...')
    hs = []
    for i, (q, a) in enumerate(cards):
        hs.append((min_q_card_h(q), min_a_card_h(a)))
        if (i + 1) % 20 == 0:
            print(f'    {i+1}/{len(cards)} done')
    print(f'    {len(cards)}/{len(cards)} done')

    # Pair cards; row height = max of all four sub-heights (Q_l, A_l, Q_r, A_r)
    pairs = []
    for i in range(0, len(cards), 2):
        j = i + 1 if i + 1 < len(cards) else None
        hql, hal = hs[i]
        hqr, har = hs[j] if j is not None else (0, 0)
        rh = min(max(hql, hal, hqr, har), H - 6 * mm)
        pairs.append((i, j, rh))

    # Greedily pack rows into sheets from the top
    sheets, cur, y = [], [], H
    for (li, ri, rh) in pairs:
        if cur and y - rh < 2 * mm:
            sheets.append(cur); cur, y = [], H
        cur.append((y - rh, rh, li, ri))
        y -= rh
    if cur:
        sheets.append(cur)
    return sheets


# ── stretch-to-fill ────────────────────────────────────────────────────────
def stretch_sheets(sheets):
    """
    For each sheet that is >= STRETCH_MIN_FILL full, distribute the leftover
    space equally among its rows so the cards fill the page edge-to-edge.
    Sparse pages (below the fill threshold) are left untouched.
    """
    result = []
    for sheet in sheets:
        total_h   = sum(rh for (_, rh, _, _) in sheet)
        fill_pct  = total_h / H

        if len(sheet) >= 2 and fill_pct >= STRETCH_MIN_FILL:
            extra = H - total_h
            bonus = extra / len(sheet)
            new_sheet, y = [], H
            for (_, rh, li, ri) in sheet:
                new_rh = rh + bonus
                new_sheet.append((y - new_rh, new_rh, li, ri))
                y -= new_rh
            result.append(new_sheet)
        else:
            result.append(sheet)
    return result


# ── PDF builder ─────────────────────────────────────────────────────────────
def build(cards, out_path):
    print('  Computing layout...')
    sheets = stretch_sheets(layout(cards))
    print(f'  Rendering {len(sheets)} sheets...')

    c = canvas.Canvas(str(out_path), pagesize=A4)
    c.setTitle('IN4240 Software Testing - Flashcards')
    c.setSubject('Print duplex flip-on-long-edge then cut. Q front / A back.')

    for sheet in sheets:
        ys = [oy for (oy, _, _, _) in sheet]

        # ── FRONT: questions ───────────────────────────────────────────────
        draw_cuts(c, ys)
        for (oy, rh, li, ri) in sheet:
            q, _  = cards[li]
            draw_card(c, 0,  oy, rh, li+1, 'Q', '', q, Q_BG, Q_BC)
            if ri is not None:
                q2, _ = cards[ri]
                draw_card(c, CW, oy, rh, ri+1, 'Q', '', q2, Q_BG, Q_BC)
        c.showPage()

        # ── BACK: answers (x-mirrored for duplex long-edge flip) ───────────
        # Flipping over the long (right) edge swaps left <-> right:
        #   left card on front  -> right position on back  (draw at x = CW)
        #   right card on front -> left  position on back  (draw at x = 0)
        draw_cuts(c, ys)
        for (oy, rh, li, ri) in sheet:
            q, a = cards[li]
            if ri is not None:
                q2, a2 = cards[ri]
                draw_card(c, 0,  oy, rh, ri+1, 'A', q2, a2, A_BG, A_BC)
                draw_card(c, CW, oy, rh, li+1, 'A', q,  a,  A_BG, A_BC)
            else:
                draw_card(c, CW, oy, rh, li+1, 'A', q, a, A_BG, A_BC)
        c.showPage()

    c.save()
    return len(sheets)


# ── entry point ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    notes = Path(__file__).parent
    md    = notes / 'flashcards.md'
    pdf   = notes / 'flashcards.pdf'

    print(f'Reading:  {md}')
    cards = parse(md)
    print(f'Parsed:   {len(cards)} flashcards\n')

    n = build(cards, pdf)

    print(f'\nSaved:    {pdf}')
    print(f'Sheets:   {n} physical A4 sheets  ({n*2} PDF pages)')
    print()
    print('HOW TO USE')
    print('  1. Print -> Two-sided / Duplex -> Flip on Long Edge (portrait).')
    print('  2. Cut along ALL dashed lines (1 vertical + several horizontal per sheet).')
    print('  3. Each cut piece = question on one face, answer on the other.')
