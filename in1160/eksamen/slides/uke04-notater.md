# Uke 04 – Lineær regresjon

## Relevante prøveeksamensspørsmål: Q6, Q7

---

## Lineær regresjonsmodell

**Modell:**
```
ŷ = Xw + b
```
- `X` = feature-matrise
- `w` = vektvektor (parametere)
- `b` = bias (skjæringspunkt)

**Enkeltdimensjonal versjon:**
```
ŷ = wx + b
```

### Viktige egenskaper (Q7)
- Responsen (output) **kan være negativ** (ingen begrensning)
- Når `x = 0` → `ŷ = b` (skjæringspunktet med y-aksen)
- Lineær relasjon mellom input og output

---

## MSE – Mean Squared Error

**Formel:**
```
MSE = (1/n) × Σᵢ (yᵢ − ŷᵢ)²
```
- `yᵢ` = faktisk verdi
- `ŷᵢ` = predikert verdi
- `n` = antall datapunkter

### Beregningseksempel (Q6)
Hvis MSE ≈ 0.001, er modellen veldig nøyaktig.

**Steg for å beregne MSE:**
1. Beregn prediksjon `ŷ = wx + b` for hvert punkt
2. Beregn feilen: `eᵢ = yᵢ − ŷᵢ`
3. Kvadrer feilen: `eᵢ²`
4. Ta gjennomsnittet

---

## Gradient descent (optimering)

**Formål:** Minimere tapsfunksjonen (MSE)

**Oppdateringsregel:**
```
w ← w − η × ∂L/∂w
b ← b − η × ∂L/∂b
```
- `η` = læringsrate (hyperparameter)
- `∂L/∂w` = gradient av tapet med hensyn til vekten

### Viktig distinksjon
- Gradient descent er en **optimaliseringsmetode**, IKKE en målemetode
- MSE er tapsfunksjonen som skal minimeres

### Læringsrate (η)
- For stor → overskyting, divergens
- For liten → langsom konvergens
- Hyperparameter satt FØR trening

---

## Hyperparametere vs. parametere

| Type | Eksempel | Settes |
|---|---|---|
| **Parametere** | `w`, `b` | Under trening (læres) |
| **Hyperparametere** | `η`, `k` i kNN | FØR trening (av bruker) |

---

## Regularisering

**L2 (Ridge):**
```
L = MSE + λ × Σwᵢ²
```

**L1 (Lasso):**
```
L = MSE + λ × Σ|wᵢ|
```
- Begge favoriserer lave absoluttverdier på parametere
- L1 kan gi sparsom løsning (noen vekter = 0)

---

## Formler å huske (fra formler.md)

- MSE = (1/n) Σ(yᵢ − ŷᵢ)²
- ŷ = Xw + b
- w ← w − η·∇L
