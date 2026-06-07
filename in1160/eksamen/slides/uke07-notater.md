# Uke 07 – Beslutningstrær og ensembler

## Relevante prøveeksamensspørsmål: Q13, Q14, Q15

---

## Beslutningstrær

### Struktur
- **Rot**: første splittepunkt
- **Interne noder**: splittebetingelser
- **Blader**: klasse-prediksjoner

### Entropi (Q14)
```
E = −Σᵢ pᵢ × log₂(pᵢ)
```
- `pᵢ` = andel av klasse `i` i noden
- Måler "urenhet" (impurity)

**Viktige verdier:**
- 50/50 fordeling → `E = 1.0` (maksimal urenhet)
- Ren node (100% én klasse) → `E = 0.0`

**Q14 svar: Entropi av 50/50 split = 1.0**

Beregning: −(0.5 × log₂(0.5) + 0.5 × log₂(0.5)) = −(0.5 × −1 + 0.5 × −1) = 1.0

### Informasjonsgevinst (Information Gain)
```
IG = E(forelder) − Σₖ (|Cₖ|/|C|) × E(Cₖ)
```
- Velg splitte-attributt med høyest informasjonsgevinst

### Gini-indeks (alternativ til entropi)
```
Gini = 1 − Σᵢ pᵢ²
```

---

## Ensemblemetoder

### Hva er en ensemblemodell?
- Kombinerer mange svake modeller til en sterkere
- Reduserer varians og/eller bias

### Svak lærer (weak learner) (Q13)
- En modell som er **bare litt bedre enn tilfeldig gjetting**
- Typisk nøyaktighet ~51–60%
- Mange svake lærere → sterk ensemble

**Q13 svar: Svak lærer = barely better than random (C)**

---

## Random Forest (Q15)

### Prinsipper
1. **Bagging (Bootstrap Aggregating)**: tren hvert tre på tilfeldig utvalg med tilbakelegging
2. **Tilfeldig feature-utvalg**: ved hver splitt, bruk tilfeldig delmengde av features

**Antall features per splitt:**
```
√n features (klassifikasjon)
n/3 features (regresjon)
```

### Egenskaper
- Mange trær på tilfeldige underutvalg
- Reduserer overfitting sammenlignet med enkelt tre
- Robust mot støy

**Q15 svar: Random forest = mange trær på tilfeldige underutvalg (B)**

### Boosting (alternativ til bagging)
- Trener trær sekvensielt
- Hvert tre fokuserer på feil fra forrige
- Eksempel: AdaBoost, Gradient Boosting

---

## Sammenligning av ensemblemetoder

| Metode | Parallell? | Fokus |
|---|---|---|
| Bagging (Random Forest) | Ja | Reduserer varians |
| Boosting | Nei (sekvensiell) | Reduserer bias |

---

## Formler å huske (fra formler.md)

- Entropi: E = −Σpᵢlog₂(pᵢ)
- E(50/50) = 1.0, E(ren node) = 0.0
- Random forest: √n features per splitt
- IG = E(parent) − Σ(|Cₖ|/|C|)·E(Cₖ)
