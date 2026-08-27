# Uke 11 – Generativ KI og språkmodeller

## Relevante prøveeksamensspørsmål: Q22, Q23, Q24

---

## Generativ vs. Diskriminativ AI (Q22)

### Diskriminativ modell
- Lærer **beslutningsgrensen** mellom klasser
- Modellerer `P(y|x)` — sannsynlighet for klasse gitt input
- Eksempler: logistisk regresjon, SVM, nevrale nett for klassifikasjon

### Generativ modell
- Lærer **datafordelingen** `P(x)` eller `P(x|y)`
- Kan generere nye datapunkter
- Eksempler: VAE, GAN, GPT, diffusjonsmodeller

**Q22 svar: Generativ AI lærer datafordelingen (c)**

---

## Embeddings / Innbygging (Q23)

### Hva er embeddings?
- **Lavdimensjonal, tett (dense), distribuert** representasjon
- Representerer ord/konsepter som kontinuerlige vektorer

### Egenskaper (Q23)
- **Lavdimensjonal**: mye færre dimensjoner enn one-hot (f.eks. 300 i stedet for 100 000)
- **Tett (dense)**: de fleste verdier er ikke-null (i motsetning til one-hot)
- **Distribuert**: mening er spredt over alle dimensjonene

**Q23 svar: Embeddings er lavdimensjonale, tette og distribuerte (b)**

### Sammenligning med one-hot

| Egenskap          | One-hot                   | Embedding |
|---|---|---|
| Dimensjonalitet   | = vokabularstørrelse      | Mye lavere (e.g. 100–1000) |
| Tetthet           | Sparse (én 1, resten 0)   | Dense (mange ikke-null verdier) |
| Semantisk likhet  | Nei                       | Ja (nærliggende ord → nærliggende vektorer) |

---

## Transformer-arkitektur og Attention (Q24)

### Attention-mekanismen
```
Attention(Q, K, V) = softmax(QKᵀ / √dₖ) × V
```
- **Q** (Query): det vi søker etter
- **K** (Key): det vi sammenligner mot
- **V** (Value): det vi henter ut
- Output = **vektet sum av verdivektorer** basert på query-key likhet

**Q24 svar: Attention er vektet sum av vektorer basert på likhet mellom query og key (a)**

### Enkelt forklart
- For hvert ord: beregn likhet med alle andre ord
- Bruk likheter som vekter til å kombinere representasjoner
- Gjør det mulig å fange avhengigheter på tvers av lange sekvenser

### Transformer-egenskaper
- Parallell behandling (i motsetning til RNN)
- Skalerer godt
- Grunnlag for GPT, BERT, T5, mfl.

---

## Treningsfaser for LLM (store språkmodeller)

### Fase 1: Pre-trening
- Tren på enorme tekstmengder (neste-ord-prediksjon)
- Lærer generell kunnskap om språk og verden

### Fase 2: Instruksjons-finjustering
- Tren på par av instruksjon → svar
- Gjør modellen mer nyttig og følsom for instruksjoner

### Fase 3: RLHF (Reinforcement Learning from Human Feedback)
- Menneskelige evaluerere rangerer svar
- En belønningsmodell lærer å score svar
- PPO-algoritme finjusterer LLM mot belønningsmodellen

---

## Generative modeller

| Modell                | Prinsipp |
|---|---|
| VAE                   | Encoder-decoder, latent rom |
| GAN                   | Generator vs. diskriminator |
| Diffusjonsmodell      | Fjern støy steg for steg |
| GPT (autoregressive)  | Prediker neste token |

---

## Formler å huske (fra formler.md)

- Attention: A = softmax(QKᵀ/√dₖ)·V
- Embeddings: dense, low-dim, distributed
- LLM-faser: pre-training → instruction fine-tuning → RLHF
