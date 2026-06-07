# Uke 14 – Oppsummering og eksamensforberedelse

## Dekker alle prøveeksamensspørsmål

---

## Hurtigreferanse: alle emner og formler

### TF-IDF og vektormodeller (Q1–Q3)
```
TF(t,d) = freq(t,d) / |d|
IDF(t) = log(N / df(t))
TF-IDF = TF × IDF
cos(u,v) = (u·v) / (||u||·||v||)
Sentroid: c = (1/|C|) × Σ dᵢ
```
- Høy IDF = sjelden term = viktig
- cos=1 → Euklidsk avstand = 0 (for normaliserte vektorer)
- Rocchio: sentroidbasert, trenger ikke treningssett etter trening

---

### Evaluering og klynging (Q4–Q5)
```
Accuracy = (TP+TN)/(TP+TN+FP+FN)
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
F1 = 2PR/(P+R)
WCSS = Σₖ Σᵢ∈Cₖ ||xᵢ−μₖ||²
```
- k-Means: flat, krever k, kan gi lokalt min, ikke-deterministisk
- Intrinsisk = direkte mot fasit; Ekstrinsisk = downstream utility

---

### Lineær regresjon (Q6–Q7)
```
ŷ = Xw + b
MSE = (1/n) Σ(yᵢ−ŷᵢ)²
w ← w − η·∇L
```
- Output kan være negativ
- x=0 → ŷ=b
- Gradient descent er optimeringsmetode (ikke målemetode)

---

### Matriseregning og logistisk regresjon (Q8–Q9)
```
σ(z) = 1/(1+e^−z)       [sigmoid, binær]
softmax(zₖ) = e^zₖ/Σe^zⱼ  [multinomial]
BCE: L = −[y·log(ŷ)+(1−y)·log(1−ŷ)]
Beslutningsgrense: z = 0
Parametere: C klasser × F features = C×F
```

---

### Nevrale nett og perceptron (Q10–Q12)
```
Δwᵢ = η(y−ŷ)xᵢ   [perceptron-oppdatering]
ReLU(z) = max(0, z)
```
- η = læringsraten
- Backprop: brukt i flerlags nett, oppdaterer vekter mot lavere treningsfeil
- Velg klassen med høyest softmax-output

---

### Beslutningstrær og ensembler (Q13–Q15)
```
E = −Σpᵢlog₂(pᵢ)    [entropi]
E(50/50) = 1.0
IG = E(parent) − Σ(|Cₖ|/|C|)·E(Cₖ)
Random forest: √n features per splitt
```
- Svak lærer = bare litt bedre enn tilfeldig
- Random forest = bagging + tilfeldig feature-utvalg

---

### ML i praksis (Q16–Q18)
```
x' = (x−x̄)/s           [standardisering]
Outlier: |x−x̄| > 2s
One-hot: k kategorier → k-dimensjonal vektor
```
- Ikke erstatt manglende verdier med 0
- L1/L2: begge favoriserer lave absoluttverdier
- Strukturert prediksjon: grafer, trær, sekvenser

---

### Forsterkende læring (Q19–Q21)
```
Q-læring: Q(S,A) ← Q(S,A) + μ[r + γ·max Q(S',A') − Q(S,A)]
SARSA:    Q(S,A) ← Q(S,A) + μ[r + γ·Q(S',A') − Q(S,A)]
```
- Q-læring: off-policy, bruker max
- SARSA: on-policy, bruker faktisk neste handling (IKKE greedy)
- γ = diskonteringsfaktor (vekter fremtidige belønninger)

---

### Generativ KI og LLM (Q22–Q24)
```
Attention: A = softmax(QKᵀ/√dₖ)·V
```
- Generativ AI lærer datafordelingen P(x)
- Embeddings: lav-dim, tette (dense), distribuerte
- Attention = vektet sum av verdivektorer basert på query-key likhet
- LLM-faser: pre-trening → instruksjons-finjustering → RLHF

---

### Filosofi og etikk (Q25–Q26)

**Jagged intelligence (Q25):**
- AI utmerker seg på vanskelige oppgaver men feiler på enkle
- Uforutsigbare, ujevne kapabiliteter

**Etikk – automatisert CV-sortering (Q26):**
1. Bias/diskriminering (historiske mønstre i data)
2. Manglende åpenhet/forklarbarhet (black-box)
3. Proxy-diskriminering (indirekte via nøytrale variabler)

---

## Eksamenstips

| Spørsmålstype | Strategi |
|---|---|
| Flervalg (enkelt) | Sjekk mot formler; utelukk åpenbart gale |
| Flervalg (multiple) | Alle korrekte svar må med – delpoeng |
| Beregning | Vis utregning steg for steg |
| Fritekst | 2–3 setninger per punkt, bruk fagterminologi |

**Husk:**
- Les spørsmålene nøye (USANT vs. SANT)
- Ved tvil: gå tilbake til grunnleggende definisjoner
- Fritekst-svar: eksempler gir ekstrapoeng
