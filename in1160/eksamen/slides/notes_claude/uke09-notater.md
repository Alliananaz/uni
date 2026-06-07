# Uke 09 – ML i praksis

## Relevante prøveeksamensspørsmål: Q16, Q17, Q18

---

## Datainnsamling og statistiske skjevheter (Q16)

### Typer statistisk skjevhet (bias) i data

**Utvalgsfiltrering / Selection bias:**
- Dataen er ikke representativ for populasjonen
- Eksempel: trener på eng. tekst, bruker på norsk

**Bekreftelsesfiltrering / Confirmation bias:**
- Labeling påvirket av forventninger
- Annotører stempler i tråd med antagelser

**Historisk bias:**
- Treningsdata reflekterer historiske ulikheter
- Eksempel: CV-screening som diskriminerer kvinner

**Rapporteringsfiltrering / Reporting bias:**
- Hendelser rapporteres ulikt basert på hvem som er involvert

**Andre typer:**
- Survivorship bias
- Measurement bias (feil i innsamling)

**Q16: Du skal nevne 2 statistiske skjevheter – velg fra listen over.**

---

## Feature engineering (Q17)

### One-hot encoding
- Brukes for **kategoriske variabler** uten ordning
- Antall kategorier `k` → vektor av lengde `k`
- Eksempel: 3 farger {rød, grønn, blå} → [1,0,0], [0,1,0], [0,0,1]

**Q17: One-hot vektor har lengde = antall kategorier (k)**

### Manglende verdier
- **IKKE erstatt med 0** (kan ødelegge statistikk)
- Alternativ: imputering (gjennomsnitt, median, modus)
- Alternativ: fjern raden/kolonnen

### Outlier-deteksjon (Q18)

**2 standardavvik-metoden:**
- Beregn gjennomsnitt `x̄` og standardavvik `s`
- Outlier: `|x − x̄| > 2s`

**Q18 eksempel:** Datasett [0, 3, 5, 9, −2]
- x̄ = (0+3+5+9−2)/5 = 3
- s = √((9+0+4+36+25)/5) = √14.8 ≈ 3.85
- Grenser: 3 ± 2×3.85 = [−4.7, 10.7]
- Alle verdier er innenfor → **ingen outliers**

**Q18 svar: ingen verdi (d)**

---

## Regularisering (Q17)

### L1 (Lasso)
```
L = tapsfunksjon + λ × Σ|wᵢ|
```
- Favoriserer **sparse** løsninger (noen vekter = 0)

### L2 (Ridge)
```
L = tapsfunksjon + λ × Σwᵢ²
```
- Favoriserer **jevne** løsninger (alle vekter små)

**Q17: Begge L1 og L2 favoriserer lave absoluttverdier på parametere**

---

## Strukturert prediksjon (Q17)

- Output er **strukturert**: sekvens, tre, graf
- Eksempler: POS-tagging, parsing, maskinoversettelse
- Mer komplekst enn enkel klassifikasjon

**Q17: Strukturert prediksjon gjelder grafer, trær og sekvenser**

---

## Feature scaling

**Standardisering (z-score):**
```
x' = (x − x̄) / s
```
- `x̄` = gjennomsnitt
- `s` = standardavvik

**Min-max skalering:**
```
x' = (x − min) / (max − min)
```

---

## Treningsoppsett

| Begrep | Forklaring |
|---|---|
| Treningssett | Brukes til å lære parametere |
| Valideringssett | Brukes til å tune hyperparametere |
| Testsett | Brukes kun til endelig evaluering |
| Hyperparametere | Settes FØR trening |

---

## Formler å huske (fra formler.md)

- x' = (x − x̄) / s  (standardisering)
- Outlier: |x − x̄| > 2s
- One-hot: k kategorier → k-dimensjonal vektor
