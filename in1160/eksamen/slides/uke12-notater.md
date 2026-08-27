# Uke 12 – ML i praksis: trening, evaluering og databehandling

## Relevante prøveeksamensspørsmål: Q16, Q17, Q18 (utdypning)

---

## Treningsprosessen

### Trenings-, validerings- og testsett

```
Datasett → [Treningssett 70%] [Valideringssett 15%] [Testsett 15%]
```

| Sett                  | Brukt til |
|---|---|
| Treningssett          | Læring av parametere (`w`, `b`) |
| Valideringssett       | Tuning av hyperparametere |
| Testsett              | Endelig evaluering (kun én gang!) |

**Viktig:** Testsett må aldri brukes til å ta designvalg – da "lekker" informasjon.

### Kryssvalidering (k-fold)
- Del data i `k` like deler
- Tren på `k−1`, test på 1
- Gjenta `k` ganger, gjennomsnitt av resultater

---

## Bias og varians (bias-variance tradeoff)

```
Forventet feil = Bias² + Varians + Irreducibel støy
```

| Problem                       | Symptom                           | Løsning |
|---|---|---|
| Høy bias (underfitting)       | Dårlig på trening OG test         | Mer kompleks modell |
| Høy varians (overfitting)     | Bra på trening, dårlig på test    | Regularisering, mer data |

---

## Hyperparameter-tuning

**Hyperparametere settes FØR trening:**
- Læringsrate η
- Regulariseringsstyrke λ
- Antall lag / noder
- Batch-størrelse

**Metoder:**
- Grid search: prøv alle kombinasjoner
- Random search: tilfeldig utvalg
- Bayesian optimization: smart søk

---

## Databehandling

### Håndtering av manglende verdier
- **IKKE erstatt med 0** (forvrenger statistikk)
- Imputering med gjennomsnitt/median
- Fjern rader med manglende verdier
- Bruk modell til å predikere manglende verdier

### Normalisering og skalering

**Standardisering:**
```
x' = (x − x̄) / s
```

**Min-max:**
```
x' = (x − min) / (max − min)
```

### Kategoriske variabler
- **Ordinale**: har naturlig rekkefølge → tall-koding OK
- **Nominale**: ingen rekkefølge → **one-hot encoding**

---

## Læringsrate og konvergens

```
Stor η → overskyting, instabilitet
Liten η → langsom konvergens
Optimal η → rask og stabil konvergens
```

**Adaptiv læringsrate:** Adam, RMSProp justerer η automatisk

---

## Batchtyper

| Type                  | Beskrivelse |
|---|---|
| Batch GD              | Hele datasettet per oppdatering |
| Mini-batch GD         | Delmengde per oppdatering (vanligst) |
| Stochastic GD (SGD)   | Én prøve per oppdatering |

---

## Vanlige feil i ML-prosjekter

1. Datalekkasje (test-info i trening)
2. Feil håndtering av manglende verdier
3. Ikke skalere features
4. Evaluere kun på treningssett
5. Ikke sjekke for skjevheter i data

---

## Formler å huske (fra formler.md)

- x' = (x−x̄)/s  (standardisering)
- MSE = (1/n)Σ(yᵢ−ŷᵢ)²
- Bias-varians: Total feil = Bias² + Varians + Støy
