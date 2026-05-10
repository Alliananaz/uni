# Formler til eksamen shibal
## Vektrom 
### Generell vektornotasjon

### Lengde (norm) og lengdenormalisering
    - for å redusere påvirkningen av lengden -- NORMALISERE alle vektorene slik at |x| = 1
    - dette kn gjøres ved å dele hver vcerdi på vektorens lengde: 
        x * (1 / |x|)
    - dette er slik at alle sin lengde er like lange 

### Avstand- / likhetsmål
    - euklidisk avstand
        - d(a,b) = XXXXX
        - intuitiv tolkning: 
            Avstanden mellom to punkter tilsvarer lengden på den rette linjen som forbinder dem
        - beregner lengden på vektoren som forbinder punktene
        - tenk på det som en trekant - a + b + c der c = d
    - prikkprodukt (dot product)
        a * b = a1b1 + a2b2 + a3+b3 ...
        - mellom to vektorer a og b 
        - summen av produktene av de tilsvarende komponentene
        - eks: a = [2,3] og b = [4,1]
            a * b = 2*4 + 3*1 = 8 + 3 = 11
    - kosinuslikhet
        cos(a,b) = (a * b) / (|a| * |b|)
        - finne vinkelen mellom to vektorer ^^
        - prikkprod har en geometrisk tolkning som kobler det til vinkelen θ mellom to vektorer:
            a * b = |a| * |b| * cos(θ)
        - |a| og |b| er lengdene til vektorene 
        - hva forteller cos(θ) oss:
            - 1     vektorene peker i samme retning (θ = 0 grader)
            - 0     vektorene er vinkelrette på hverandre (θ = 90 grader)
            - -1    vektorene peker i motsatt retning (θ = 180 grader)
            - >0    vinkelen er mindre enn 90 grader
            - <0    vinkelen er større enn 90 grader
        - eks: a = [1,0] og b = [0,1]
            a * b = 1*0 + 0*1 = 0
            |a| = 1, |b| = 1
            cos(θ) = 0 / (1*1) = 0 --> θ = 90 grader

### TF-IDF (Term Frequency-Inverse Document Frequency)
    TF-IDF = TF * IDF
        TF = antall ganger ord dukker opp / totalt antall ord i dok
        IDF = log(totalt antall dok / antall dok som inneholder ordet)
            ** log() brukes for å "dempe" effekten - ellers ville veldig sjeldne ord dominere alt
    - en måte å MÅLE hvor VIKTIG et ord er i et dokument, sammenlignet med en samling av mange dokumenter 
    - ord som er vanlige i ett dokument, men sjeldne på tvers av alle dokumenter, får høy score
    - eks: 1000 artikler og ser på ordet "kvantecomputer" i en bestemt artikkel:
        "kvantecomputer" dukker opp 5x i en artikkel med 200 ord
        TF = 5/200 = 0.025
        det finnes bare i 10 av 1000 artikler 
        IDF = log(1000/10) = log(100) ~ 2.0
        TF-IDF = 0.025 * 2.0 = 0.05
    - eks: 1000 artikler og ordet "og":
        TF ~= 0.08
        IDF ~= 0
        TF-IDF = 0 -- akkurat det vi vil!

### Sentroidevektor
    μᵢ = (1 / |Cᵢ|) × Σ xj
    - summen alle vektorene xj som tilhører klassen Cᵢ, og del på antall medlemmer 
    - enkelt gjennomsnittsvektoren av en gruppe vektorer
    - eks: tre dok i klassen "sport" - representert som enkle 2D-vektorer
        dok1 = [2,4]
        dok2 = [4,2]
        dok3 = [3,3]
        sentroiden = μ = [(2+4+3) / 3, (4+2+3) / 3] = [3,3]
    - [3,3] er tyngdepunktet til klassen - det representerer hele klassen med en enkelt vektor

### Evalueringsmål av klassifikasjon:
    - TP - true positive
    - FP - false positive
    - FN - false negative
    - FN - false negative
    - N - antall / total

    - eks: spamfilter som skal si om en e-post er spam (positiv) eller ikke-spam (negative). Du tester den på 10 e-poster, der 4 faktisk er spam og 6 er ikke spam
        TP = 3, FP = 1, FN = 1, TN = 5

    - Nøyaktighet (accuracy)
        (TP + TN) / N = ((TP + TN) / (TP + TN + FP + FN))
        - hvor ofte har modellen rett totalt sett
        - andelen korrekte prediksjoner
        - ikke egnet for ubalaserte klasser (dvs stor forskjell i ant positive / negative eks)
        - eks:
            (3 + 5) / 10 = 0.8
            80% av epostene ble klassifisert riktig

    - Presisjon (precision)
        TP / (TP + FP)
        - når modellen sier "ja" - har den rett?
        - andelen identifiserte klassemedlemmer som var korrekte
        - eks: 
            3 / (3 + 1) = 0.75
            75% av epostene som ble flagget som spam var faktisk spam
            lav presisjon betyr at mange vanlige eposter havner i søppelpost-mappen

    - Sensitivitet (recall)
        TP / (TP + FN)
        - av alle de som faktisk er positive - finner modellen dem?
        - andelen faktisk klassemedlemmer som ble identifisert 
        - eks:
            3 / (3 + 1) = 0.75
            75% av den faktiske spamen ble oppdaget
            lav sensitivitet betyr at mye spam slipper gjennom - også uønsket

    ** Avveining: positive prediksjoner for alle eks vil gi sensitivitet på 100% - men typisk svært dårlig presisjon **
        - hvis modellen er veldig "aggressiv" og flagger nesten alt som spam, fanger opp mer spam (høy sensitivitet) - men plager  
    - F1-mål (F1-score)
        (2 * presisjon * sensitivitet) / (presisjon + sensitivitet)
        - balanse mellom presisjon og sensitivitet i ett mål 
        - er spesielt nyttig når begge deler er viktige

### Klyngeanalyse: 
    - handler om å gruppere objekter automatisk BASERT på likhet (uten at noen har fortalt modellen på forhånd hvilke grupper som finnes)
    - INGEN FORHÅNDSDEFINERTE KLASSER - modellen oppdager strukturen i dataene selv
    - FORSKJELL fra klassefikasjon - der man på forhånd bestemmer at klassene er feks "sport", "politikk" eller "økonomi" og trenger modellen på disse eksemplene
    - nyttig når man IKKE VET hva man leter etter på FORHÅND / npr det ville vært for dyrt og tidkrevende å merke opp all dataen manuelt
    
    - forskjell fra klassifikasjon
                                        Klassifikasjon      Klyngeanalyse
        trenger merkelapper             ja                  nei
        klasser bestemt på forhånd      ja                  nei
        type læring                     veiledet            ikke-veiledet
        eksempel                        spamfilter          kundesegmentering 

    - k-means
        - k : antall klynger du vil ha (bestemmes på forhånd)
            - Svakhet - man må gjette hvor mage naturlige grupper som finnes i dataene
            - God teknikk - bare prøve seg fram med forskjellige k-er
            - *albue metoden (elbow method):
                - Man prøver alle k-verdier 
                - Unngåer overfitting - slik at algo ikke deler opp grupper som ikke burde deles
                - Generaliserbart - klynger skal helst representere EKTE, MENINGSFULLE mønstre i dataene
                - Enkelhet - en modell med færre klynger er enklere å tolke og forklare
        - Tenk at man har en gjeng med mennesker i et rom og vil dele dem inni 3 grupper basert på hvor de står
        plasserer 3 "gruppeledere" tilfeldig i rommet, og alle går til nærmeste gruppeleder
        gruppelederne flytter seg til midten av sin gruppe
        dette gjentar seg til ingen bytter gruppe lenger
        - k-means prøver å minimere klyngeintern kvadratsum (WCSS)

        - Klyngeintern kvadratsum (within-cluster sum of squares WCSS)
            - et MÅL på hvor tette og kompakte klyngene er
            - for hver klynde måler hvor langt hvert punkt er fra sentroiden sin
                - jo nærmere alle punktene er sentroiden, jo bedre er klyngen
            - lav WCSS - tette, kompakte klynger    = bra
            - høy WCSS - spredte, løse klynger      = dårlig

            - hvordan: (for hvert punkt i en klynge) 
                beregne avstanden til sentroiden --> svar
                punktsvar = svar^2
                totalsvar = punktsvar + punktsvar + punktsvar
                eks: klynge 1 med sentroide [2,2] og tre punkter A, B og C
                    A = [1,1] --> (2-1)^2 + (2-1)^2 = 1+1 = 2
                    B = [2,3] --> (2-2)^2 + (2-3)^2 = 0+1 = 1
                    C = [3,2] --> (3-1)^2 + (2-2)^2 = 0+1 = 1
                    WCSS = 2+1+1 = 4
            
            - ^2 :
                - kvadrering gjør at negative og positive avstander ikke kansellerer hverandre
                - kvadrering straffer kvadrering store avvik ekstra hardt
                    et punkt som er veldig langt unna sentroiden trekker opp WCSS mye mer enn to punkter med halve avstanden





## Lineær og logistisk regresjon
"Alle formler som har blitt gjennomgått i forelesning er pensum" legit skyt meg

### Lineær regresjon (grunnformelen)
- EN VEKTET SUM av opplysninger (inputtrekk) + en fast startverdi (b)
- Hver trekk (x, y) --> vekt, som forteller hvor mye det bidrar til prisen
    stor vekt -     viktig trekk
    liten vekt -    ikke så viktig trekk
- Intuisjon: 
    læring handler om å finne verdiene for w1,...,wP og 'b' som gjør at "feilene" mellom hva modellen forutsier og fasitverdiene i trenngssettet blir så små som mulig 
    trenger TRE komponenter: 
        - et TRENINGSSETT av n eksempler {hvor 1 <= k <= n}

        - en TAPSFUNKSJON som måler avviket mellom modellens prediksjoner og de faktiske verdiene
            - en måte å måle hvor mye feil modellen gjør
            - MSE Gjennomsnittlig kvadratfeil (mean squared error)
                - hvordan:
                    differansen mellom gjettet og ekte verdi
                    differansen^2
                    ta gjennomsnittet over alle datapunkter
            lwk TBC

        - en OPTIMERINGSMETODE som leter etter "gode" verdier for w og b, gitt tapsfunksjon og treningssett
            - optimaliserimgsalgo fungerer ofte iterativt: 
                - starter med en 'dum' løsning for parameterne som skal estimeres
                - gradvis forbedrer denne inntil tapet ikke lenger lar seg redusere

            - GD (gradient descent) - faren til optimeringsalgo
                - 'hvis man ikke vet hvor svaret er, gå alltid i den retningen som føles mest nedoverbakke'
                - nedoverbakke -- tapsfunksjonen (MSE)
                - høyde -- hvor mye feil modellen gjør
                - mål : FINNE de verdiene for w og b som gir det laveste punktet (altså minst mulig feil)


        !!! Merk: Akkurat for lineær regresjon er det også mulig å estimere parameterne «analytisk», altså helt uten optimering:
            - Analytiske løsninger sliter med å skalere når antallet trekk blir stort, som ofte er tilfellen i maskinlæring,
            - Disse løsningene kan dessuten ikke brukes for mer avanserte ML-modeller (slik som nevrale nettverk).
        !!! 
    
### Lineær og logistisk regresjon i matriseformat
#### Lineær regresjon 
    ŷ = Xw + b
    - for n datapunkter med p trekk hver samler man alt i en matrise X og en vektvektor w 
        X (størrelse n*p)
        w (stærrelse p*1)

#### Logistisk regresjon
    ŷ = σ(Xw + b)           - der σ(z) = 1 / (1 + e⁻ᶻ)
    - σ (sigmoid) - 'klemmer' alle tall inn i intervallet (0,1) slik at outputen kan tolkes som en sannsynlighet for klasse 1

    TBC
    


- Matriseoperasjoner
- Matriseprodukter
- Logistisk regresjon
    - (med) Sigmoid
    - (med) Softmax
- Binær og kategorisk kryssentropi





## Nevrale nettverk
- Ut-verdi i perseptronet
- Oppdatering av vekter i perseptron
- Bakoverfasen (tilbakeprogagering) 
    - Kjenner til intensjonen bak
    - Hvordan den fungerer på høyt nivå
    - Hvordan henge sammen med gradientnedstigning
- Aktiveringsfunksjoner 
    - Kjenner til intensjonen bak
    - Kan anvende aktiveringsfunksjonene
    - Terskel-funksjonen
    - ReLU





## Beslutningstrær og ensembler
- Beslutningstrær
    - Intensjonen for hvordan vi velger trekk for å splitte på i noder
    - Hvordan bygge tre steg for steg
    - Entropi
- Ensembler
    - Intensjonen bak
    - Hvordan bygge ensembler





## ML i praksis
Alle formlene fra forelesning er pensum 
- Gjennomsnitt
- Median
- Typetall
- Standardavvik
- One-hot encoding
- Skalering
- L1 og L2 regularisering





## Forsterkende læring
- Forsterkende læring
- Agent
- Tilstand
- Belønning
    - Fremtidig diskontert belønning
- Handlinger 
    - Grådig
    - Epsilon-grådig
    - Softmax
- Miljø
- Markov-beslutningsprosess
- policy
- Q-læring
- SARSA





Rocchio
