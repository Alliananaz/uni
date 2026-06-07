# Uke 05 – Matriseregning og logistisk regresjon

## Relevante prøveeksamensspørsmål: Q8, Q9

---

## Matriseregning

### Matrisemultiplikasjon (Q8)

**Regler:**
- `A` er `m×n`, `B` er `n×p` → `AB` er `m×p`
- Element `(i,j)` i produktet = rad `i` i A · kolonne `j` i B
- **Ikke kommutativ**: `AB ≠ BA` generelt

**Eksempel:**
```
A = [1, 2]   B = [1]     AB = [1×1 + 2×2] = [5]
             [2]
```

Prøveeksamen Q8: AB = [5, −1]

### Viktige matrise-operasjoner
- **Transponering**: `Aᵀ` — rader blir kolonner
- **Identitetsmatrise**: `I` — `AI = A`
- Lineær regresjon med matrise: `ŷ = Xw + b`

---

## Logistisk regresjon

### Binær logistisk regresjon (sigmoid)

**Sigmoid-funksjon:**
```
σ(z) = 1 / (1 + e^−z)
```
- Output: verdi mellom 0 og 1 (tolkes som sannsynlighet)
- `z = Xw + b` (lineær kombinasjon)

### Beslutningsgrense (Q9)
- Beslutningsgrensen er der `z = 0`
- `σ(0) = 0.5` → klassen avgjøres av hvilken side av z=0

### Multinomial logistisk regresjon (softmax)

**Softmax:**
```
softmax(zₖ) = e^zₖ / Σⱼ e^zⱼ
```
- Gir sannsynlighetsfordeling over alle klasser
- Summer alltid til 1

### Antall parametere (Q9)
- `C` klasser, `F` features → `C × F` parametere (+ bias per klasse)
- Eksempel: 5 klasser × 8 features = **40 parametere** (bias telles separat)

---

## Tapsfunksjon

### Binær kryssentropy (BCE)
```
L = −[y·log(ŷ) + (1−y)·log(1−ŷ)]
```

### Kategorisk kryssentropy (CCE)
```
L = −Σₖ yₖ·log(ŷₖ)
```

**Viktige egenskaper:**
- Kryssentropy er **ubegrenset** (kan bli veldig stor)
- Er IKKE begrenset til [0,1]
- Lavere verdi = bedre modell

---

## Sammenligning: Lineær vs. Logistisk

| Egenskap | Lineær regresjon | Logistisk regresjon |
|---|---|---|
| Output | Kontinuerlig (−∞ til +∞) | Sannsynlighet (0 til 1) |
| Tapsfunksjon | MSE | Kryssentropy |
| Aktivering | Ingen | Sigmoid / Softmax |
| Bruk | Regresjon | Klassifikasjon |

---

## Formler å huske (fra formler.md)

- σ(z) = 1/(1+e^−z)
- softmax(zₖ) = e^zₖ / Σⱼ e^zⱼ
- BCE: L = −[y·log(ŷ) + (1−y)·log(1−ŷ)]
- Beslutningsgrense: z = 0
