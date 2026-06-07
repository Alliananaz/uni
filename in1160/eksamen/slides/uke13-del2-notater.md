# Uke 13 Del 2 – Etikk i AI

## Relevante prøveeksamensspørsmål: Q26

---

## Etiske problemer i automatiserte systemer (Q26)

### Q26: Nevn 3 etiske problemer ved automatisert CV-sortering

**1. Bias og diskriminering**
- Modellen kan lære historiske diskriminerende mønstre
- Eksempel: trenet på historiske ansettelser der kvinner ble valgt bort → diskriminerer kvinner
- Beskyttet klasser: kjønn, etnisitet, alder, religion

**2. Mangel på åpenhet (Transparency / Forklarbarhet)**
- Søkere vet ikke hvorfor de ble avvist
- Black-box modeller gir ingen begrunnelse
- Vanskelig å bestride en avgjørelse
- GDPR: rett til forklaring ved automatiserte beslutninger

**3. Rettferdighet (Fairness)**
- Ulik behandling av grupper med samme kvalifikasjoner
- Proxy-diskriminering: postnummer, navn kan korrelere med etnisitet
- Disparate impact: nøytrale regler som rammer én gruppe uforholdsmessig

**Andre gyldige svar:**
- Personvern (lagring av sensitive data)
- Ansvarlighetsproblemer (hvem er ansvarlig når systemet gjør feil?)
- Manglende kontekst (CV-en fanger ikke opp menneskelig kompleksitet)

---

## Typer bias i ML-systemer

| Type bias | Beskrivelse |
|---|---|
| Historisk bias | Treningsdata reflekterer historisk urettferdighet |
| Representasjonsbias | Visse grupper er underrepresentert i data |
| Målbias | Feil proxy-mål for det vi egentlig vil måle |
| Evalueringsbias | Testsett representerer ikke reell populasjon |
| Aggregeringsbias | En modell for alle passer ikke alle like godt |

---

## Fairness-definisjoner

**Demografisk paritet:**
```
P(ŷ=1 | A=0) = P(ŷ=1 | A=1)
```
- Like mange positive prediksjoner i alle grupper

**Equalized odds:**
```
P(ŷ=1 | y=1, A=0) = P(ŷ=1 | y=1, A=1)
```
- Like høy recall i alle grupper

**Viktig:** Ulike fairness-definisjoner er matematisk uforenlige i mange scenarioer.

---

## Personvern og GDPR

- **Rett til innsyn**: vite hvilke data som lagres
- **Rett til sletting**: "retten til å bli glemt"
- **Rett til forklaring**: ved automatiserte beslutninger
- **Dataminimering**: samle ikke mer enn nødvendig
- **Formålsbegrensning**: data brukes kun til oppgitt formål

---

## Forklarbar AI (XAI)

| Metode | Beskrivelse |
|---|---|
| LIME | Lokal forklaring: approksimer modellen lokalt |
| SHAP | Shapley-verdier: bidrag per feature |
| Attention-visualisering | Hvilke ord fokuserte modellen på? |
| Feature importance | Random forest: hvilke features brukes mest? |

---

## Ansvarskjeden

```
Datakilde → Datavask → Modelltrening → Deployment → Beslutning
```
- Feil kan introduseres i hvert steg
- Ansvaret er distribuert og uklart

---

## Tips til Q26 (fritekst)

Eksempelsvar (3 problemer):
> 1. **Bias**: Systemet kan lære historisk diskriminering fra treningsdataen og urettferdig avvise søkere basert på kjønn eller etnisitet.
> 2. **Manglende åpenhet**: Søkere får ingen forklaring på avvisningen, noe som bryter med retten til begrunnelse (GDPR Art. 22).
> 3. **Proxy-diskriminering**: Tilsynelatende nøytrale variabler som postnummer kan korrelere med beskyttede karakteristikker og indirekte diskriminere.
