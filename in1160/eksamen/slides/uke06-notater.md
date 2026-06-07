# Uke 06 – Nevrale nett og perceptron

## Relevante prøveeksamensspørsmål: Q10, Q11, Q12

---

## Perceptron

### Modell
```
ŷ = f(Σᵢ wᵢxᵢ + b)
```
- `wᵢ` = vekt for input `xᵢ`
- `b` = bias
- `f` = aktiveringsfunksjon

### Perceptron-oppdatering (Q10)
```
Δwᵢ = η × (y − ŷ) × xᵢ
```
- `η` (eta) = **læringsraten**
- `y` = korrekt svar
- `ŷ` = predikert svar
- Oppdatering skjer kun ved feilklassifisering

**Q10 svar: `η` er læringsraten**

### Aktiveringsfunksjoner

| Funksjon | Formel | Output |
|---|---|---|
| Terskel (step) | 1 hvis z > 0, ellers 0 | {0, 1} |
| Sigmoid | 1/(1+e^−z) | (0, 1) |
| ReLU | max(0, z) | [0, +∞) |
| Tanh | (e^z − e^−z)/(e^z + e^−z) | (−1, 1) |

---

## Flerlags nevrale nett

### Arkitektur
- **Inputlag**: raw features
- **Skjulte lag**: lærte representasjoner
- **Outputlag**: prediksjon

### Foroverpassering (forward pass)
```
h = f(W₁x + b₁)
ŷ = g(W₂h + b₂)
```
- Beregnes via matrisemultiplikasjon lag for lag

### Bakoverpassering (backpropagation) (Q11)
- Brukes i **flerlags** nevrale nett (IKKE enkeltlag perceptron)
- Oppdaterer vekter for å **redusere treningsfeil**
- Bruker kjerneregelen (chain rule) til å beregne gradienter
- Flyter feilen **bakover** fra output til input

**Q11 viktige punkter:**
- Backprop brukes i multi-layer nets ✓
- Backprop oppdaterer vekter for å redusere treningsfeil ✓
- Backprop er IKKE det samme som gradient descent (det er optimaliseringsalgoritmen)

---

## Klassifikasjonseksempel (Q12)

For et nevralt nett med softmax-output:
- Klassen med **høyest sannsynlighet** velges
- Eksempel: output [0.1, 0.2, 0.7] → klasse 3 (indeks 2, 1-indeksert: klasse 3)

---

## Overfitting og regularisering

- **Overfitting**: modellen lærer treningsdata for godt, dårlig generalisering
- **Underfitting**: modellen er for enkel
- **Dropout**: tilfeldig deaktiverer noder under trening
- **L1/L2 regularisering**: straffer store vekter

---

## Hyperparametere i nevrale nett

| Hyperparameter | Beskrivelse |
|---|---|
| Læringsrate η | Skritt-størrelse i gradient descent |
| Antall lag | Dybde av nettverket |
| Antall noder per lag | Bredde av nettverket |
| Batch-størrelse | Antall eksempler per oppdatering |
| Epochs | Antall ganger gjennom treningsdata |

---

## Formler å huske (fra formler.md)

- Δwᵢ = η(y−ŷ)xᵢ  (perceptron-oppdatering)
- ReLU(z) = max(0, z)
- σ(z) = 1/(1+e^−z)
