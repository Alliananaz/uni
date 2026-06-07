# Uke 03 – Evaluering og klyngeanalyse (k-Means)

## Relevante prøveeksamensspørsmål: Q4, Q5

---

## Evaluering av ML-systemer

### Intrinsisk vs. Ekstrinsisk evaluering (Q5)

| Type | Hva måles | Eksempel |
|---|---|---|
| **Intrinsisk** | Direkte kvalitet mot fasit (gold standard) | Presisjon, recall, F1 |
| **Ekstrinsisk** | Nytte i et nedstrøms system | Forbedrer søkesystemet brukertilfredsheten? |

- **Ekstrinsisk** = downstream utility (nytte i kontekst)
- **Intrinsisk** = direkte mot gullstandard

### Evalueringsmål

**Nøyaktighet (Accuracy):**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Presisjon (Precision):**
```
Precision = TP / (TP + FP)
```

**Recall:**
```
Recall = TP / (TP + FN)
```

**F1-score:**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## k-Means klyngeanalyse

### Algoritme
1. Velg `k` tilfeldige sentroider
2. Tilordne hvert punkt til nærmeste sentroid
3. Beregn nye sentroider (gjennomsnitt av klyngen)
4. Gjenta til konvergens

### Egenskaper (Q4)
- **Flat clustering**: ingen hierarki
- **Krever k på forhånd** (hyperparameter)
- **Kan konvergere til lokalt minimum** (ikke garantert globalt optimum)
- **Ikke-deterministisk** (avhenger av tilfeldige startverdier)

### WCSS (Within-Cluster Sum of Squares)
```
WCSS = Σ Σ ||xᵢ − μₖ||²
```
- Brukes for å evaluere klyngekvalitet
- Lavere WCSS = tettere klynger

### Elbow-metoden
- Plot WCSS mot `k`
- Velg `k` der kurven "knekker" (avtagende gevinst)

---

## Viktige punkter å huske

- k-Means er **uovervåket læring**
- Rocchio (uke02) er overvåket; begge er sentroidbaserte
- Ekstrinsisk evaluering er dyrere men mer meningsfull i praksis

---

## Formler å huske (fra formler.md)

- WCSS = Σₖ Σᵢ∈Cₖ ||xᵢ − μₖ||²
- Accuracy = (TP+TN)/(TP+TN+FP+FN)
- F1 = 2PR/(P+R)
