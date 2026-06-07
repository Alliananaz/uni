# Uke 02 – Vektorrommodeller og TF-IDF

## Relevante prøveeksamensspørsmål: Q1, Q2, Q3

---

## TF-IDF

**Termfrekvens (TF):**
```
TF(t, d) = freq(t, d) / |d|
```
- `freq(t, d)` = antall ganger term `t` forekommer i dokument `d`
- `|d|` = total antall termer i `d`

**Invers dokumentfrekvens (IDF):**
```
IDF(t) = log(N / df(t))
```
- `N` = totalt antall dokumenter
- `df(t)` = antall dokumenter som inneholder termen `t`

**TF-IDF:**
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

**Viktige egenskaper (Q1):**
- TF-IDF *demper* termer som forekommer i mange dokumenter (høy `df` → lav `IDF`)
- Termer som er unike for få dokumenter får høy score
- Stopwords (og, i, er…) får lav TF-IDF fordi de er overalt

---

## Kosinuslikhet og Euklidsk avstand

**Kosinuslikhet:**
```
cos(u, v) = (u · v) / (||u|| × ||v||)
```
- Verdier mellom −1 og 1
- Kosinuslikhet = 1 → vektorene peker i samme retning → Euklidsk avstand = 0

**Viktige egenskaper (Q2):**
- Maksimere kosinuslikhet = minimere Euklidsk avstand (for lengdenormaliserte vektorer)
- Kosinuslikhet = 1 betyr Euklidsk avstand = 0

**Lengdenormalisering:**
```
û = u / ||u||
```
- Gjør vektorer sammenlignbare uavhengig av dokumentlengde

---

## Rocchio-klassifikator

- **Sentroidbasert**: beregner gjennomsnittsvektoren (sentroid) for hver klasse
- Klassifiserer nye dokumenter til nærmeste sentroid

**Fordeler (Q3):**
- Lav beregningskostnad ved prediksjon
- Trenger IKKE å lagre treningssett etter trening
- Enkel og rask

**Ulemper:**
- Fungerer dårlig når klasser ikke er konvekse
- Anta at klasser er lineært separerbare

---

## kNN (k nærmeste naboer)

- Lagrer hele treningssettet
- Finner de `k` nærmeste naboene for et nytt datapunkt
- Stemmer (majoritet) bestemmer klassen

**Sammenligning med Rocchio:**
| Egenskap | Rocchio | kNN |
|---|---|---|
| Trenger treningssett | Nei (etter trening) | Ja (alltid) |
| Beregningskostnad | Lav | Høy |
| Fleksibilitet | Lav | Høy |

---

## Formler å huske (fra formler.md)

- TF(t,d) = freq(t,d) / |d|
- IDF(t) = log(N/df(t))
- cos(u,v) = (u·v) / (||u||·||v||)
- Sentroid: c = (1/|C|) × Σ dᵢ
