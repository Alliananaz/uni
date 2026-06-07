# Uke 10 – Forsterkende læring (Reinforcement Learning)

## Relevante prøveeksamensspørsmål: Q19, Q20, Q21

---

## Grunnleggende begreper

| Begrep | Forklaring |
|---|---|
| Agent | Den som tar beslutninger |
| Miljø (Environment) | Det agenten interagerer med |
| Tilstand (State S) | Nåværende situasjon |
| Handling (Action A) | Det agenten gjør |
| Belønning (Reward r) | Tilbakemelding fra miljøet |
| Policy π | Agentens strategi: tilstand → handling |
| Q-verdi | Forventet fremtidig belønning for (S, A)-par |

---

## Q-læring (Q19, Q20)

### Q-oppdateringsregel
```
Q(S,A) ← Q(S,A) + μ[r + γ·max_{A'} Q(S',A') − Q(S,A)]
```
- `μ` = læringsrate
- `γ` = diskonteringsfaktor
- `r` = mottatt belønning
- `S'` = neste tilstand
- `max Q(S',A')` = beste Q-verdi i neste tilstand (greedy)

### Egenskaper ved Q-læring
- **Off-policy**: lærer optimal policy uavhengig av atferd
- Bruker **max**-operatoren (antar at agenten alltid tar beste handling neste)
- Lagrer Q-verdier i Q-tabell

---

## SARSA (Q19)

### SARSA-oppdateringsregel
```
Q(S,A) ← Q(S,A) + μ[r + γ·Q(S',A') − Q(S,A)]
```
- Bruker **faktisk** neste handling `A'` (ikke max)
- `A'` er valgt av agentens nåværende policy

### Egenskaper ved SARSA
- **On-policy**: lærer verdien av nåværende policy
- **Antar IKKE greedy policy** i neste steg
- Mer konservativ enn Q-læring

**Q19 svar: USANT – SARSA antar IKKE greedy policy (det er Q-læring som gjør det)**

### Q-læring vs. SARSA

| Egenskap | Q-læring | SARSA |
|---|---|---|
| Policy-type | Off-policy | On-policy |
| Neste handling | max Q(S',A') | Q(S',A') |
| Risikovillighet | Mer aggressiv | Mer konservativ |

---

## Diskonteringsfaktor γ (Q21)

```
Fremtidig belønning = r₁ + γ·r₂ + γ²·r₃ + ...
```

- `γ = 0`: Agent bryr seg kun om øyeblikkelig belønning
- `γ = 1`: Agent vektlegger fremtidig og nåværende belønning likt
- `0 < γ < 1`: Fremtidige belønninger vektes lavere

**Q21: Diskonteringsfaktoren bestemmer hvor mye fremtidige belønninger vektlegges**

---

## Q-tabell-eksempel (Q20)

Gitt:
- Q(S1, A2) = initial verdi
- μ = 0.1, γ = 0.9, r = 1
- Neste tilstand S2 med beste Q-verdi

**Oppdatering:**
```
Q(S1,A2) ← Q(S1,A2) + 0.1 × [1 + 0.9 × max Q(S2,·) − Q(S1,A2)]
```

---

## Utforsking vs. utnyttelse (Exploration vs. Exploitation)

- **Utforsking**: prøver nye handlinger (ε-greedy: velg tilfeldig med sannsynlighet ε)
- **Utnyttelse**: velger kjent beste handling
- **ε-greedy**: vanlig strategi som balanserer begge

---

## Formler å huske (fra formler.md)

- Q-læring: Q(S,A) ← Q(S,A) + μ[r + γ·max Q(S',A') − Q(S,A)]
- SARSA: Q(S,A) ← Q(S,A) + μ[r + γ·Q(S',A') − Q(S,A)]
- Diskontert retur: G = Σₜ γᵗ·rₜ
