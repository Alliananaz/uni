# Formler til eksamen shibal

----------------------------------
## Vektrom 
### Generell vektornotasjon
    --
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
            a * b = (2*4) + (3*1) = 8 + 3 = 11
        - selve prediksjonsformelen 

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




----------------------------------
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
    - brukes til å predikere et tall y basert på et datapunkt x representert gjennom ulike trekk 
    - 3 deler totalt:
        - prediksjon
        - læring - leting etter parameterverdier for w og b som gir minst mulig 'tap' på et treningssett
        - evaluering

##### Matriseoperasjoner
    - regneregler for tabeller med tall
    - jobbe med hele tabeller på en gang (i stedet for ett tall om gangen)
    - * matrise: en tabell med tall, organisert i rader og kolonner (n*p - n rader, p kolonner)
        - eks: matrise A (2x3) 
            2   5   1               
            3   0   4 

        - eks: en vektor er bare en matrise med 1 kolonne:
            7
            2
            5

    - Matriseprodukter
        - rad møter kolonne - multipliserer parvis - summer
        - !!! antall  kolonner i A MÅ være lik antall rader i B !!!
        - regner ut flere prikkprodukter på en gang
        - eks:
            1   2   3           7   8           31  19
            4   5   6     +     9   1     =     85  55
                                2   3       

            (1*7) + (2*9) + (3*2) = 31
            (1*8) + (2*1) + (3*3) = 19
            (4*7) + (5*9) + (6*2) = 85
            (1*8) + (2*1) + (3*3) = 55

#### Logistisk regresjon
    - probabilistisk klassifikasjonsmodell

    ##### Binær logistisk regresjon
        - 2 klasser - C1 og C2 - feks spam/ikke-spam
        - (med) SIGMOID
        - modellen trenger bare å beregne EN sannsynlighet, siden den andre er 1 - P
            - når |C| = 2 har vi to valg som utelukker hverandre - C1 eller C2
        - !! formel i boka !!
        - hvordan:
            σ(z) = 1 / (1 + e⁻ᶻ)
            begren den vektede summen
            send gjennom sigmoid

        - VEKTORISERTE versjon av binær logistisk regresjon    
            ŷ = σ(Xw + b)           - der σ(z) = 1 / (1 + e⁻ᶻ)

            - σ (sigmoid) - 'klemmer' alle tall inn i intervallet (0,1) slik at outputen kan tolkes som en sannsynlighet for klasse 1
            - den samme formelen
            - skrevet med matriser slik at man kan beregne prediksjoner for alle datapunkter på en gang
            - fordel: matriseoperasjoner kan utføres mye raskere på moderne CPU og GPU sammenlignet med å behandle ett datapunkt av gangen
            
        *** Beslutningsgrensen

    ##### Multinomisk logistisk regresjon 
        - 3+ klasser, feks A/B/C/D/E/F
        - (med) SOFTMAX
            fordeler sannsynligheter over alle klasser slik at de summerer == 1
        - modellen har egne vekter og konstantledd for hver klasse
        - i stedet for en vektet sum, regner man ut en vektet sum per klasse:

            P(Cj | x) = TBC

        eks:
            gitt tre (3) vektede summer (logits)
                z = [2.3, 0.4, -1.4]
            beregn e^z for hver verdi 
                e^2.3 = 9.97    e^0.4 = 1.49    e^-1.4 = 0.25
            summer alle e^z verdiene
                9.97 + 1.49 + 0.25 = 11.71
            del hver e^z på summen (softmax)
                C1 = 9.97 / 11.71 = 0.85
                C2 = 1.49 / 11.71 = 0.13
                C3 = 0.25 / 11.71 = 0.02

                0.85 + 0.13 + 0.02 = 1      -- summerer til 1
        
            modellen velger klasse 1 siden den har høyest sannsynlighet med 85%

### Tapsfunksjon
#### Binær kryssentropi (binary cross-entropy BCE)
    - (binær) så tapsfunksjon for modeller med 2 klasser
    
        lBCE(ŷ^(k),y^(k)) = { -log(ŷ^(k))       hvis y^(k) = C1
                            { -log(1-ŷ^(k))     hvis y^(k) = C2
    
    - eks:
        hvis prediksjonen fra modellen ŷ = 0.8 og y = C1
            tapet --> -log(0.8) = 0.22
        hvis prediksjonen fra modellen ŷ = 0.8 og y = C2
            tapet --> -log(0.2) = 1.61

    - intuisjonen bak
        Fasit | Prediksjon ŷ             |   Tap
        -----------------------------------------------------
        0.99    veldig sikker, riktig       -log(0.99) = 0.01
        0.50    usikker                     -log(0.50) = 0.69
        0.01    veldig sikker, feil         -log(0.01) = 4.61

#### kategorisk kryssentropi (categorical cross-entropy CCE)
    - utvidelse av binær kryssentropi når man har flere enn 2 klasser
    - eks:
        datapunkt og fasit fra treningssettet
            x^(1),  y = leilighet
        modellen predikerer sannsynligheter
            ŷ = [0.87, 0.09, 0.04]
        binær koding av fasit
            y = [1,0,0]
        beregn tapet
            l = -(1*log(0.87) + 0*log(0.09) + 0*log(0.04))
              = -log(0.87)
              = 0.14
        
    idfk men lwk TBC




----------------------------------
## Nevrale nettverk
### Ut-verdi i perseptronet
    ŷ == SVAR 
    - hatten betyr at det er et 'gjett' - ikke det riktige svaret
    - Når perseptronet har sett på alle inndataene og regnet ut summen
    - !! Det er * aktiveringsfunksjonen * i outputlaget som bestemmer hva slags utverdi man får

### Oppdatering av vekter i perseptron
    (ettlags perseptronet)
    - Forover-fasen : beregner ut-verdien basert på inndata
    - Bakover-fasen : oppdaterer vekter basert på ulikhet mellom utverdi og fasit
    - læring
        Δwᵢ = η(y − ŷ)xᵢ
        η : læringsraten - et lite tall 0-1 - bestemmer hvir store steg vi tar
            store læringsrate -- store hopp
            liten læringsrate -- liten hopp
            - må være lav nok til at perseptronet ikke 'hopper over' den riktige løsningen
            - ikke for lav - tar evig lang tid å lære
        y : det rikitige svaret (fasiten)
        ŷ : det perseptronet gjettet
        xᵢ : inndataverdien (feks høyden)

    - regelen garanterer kovergens til riktig klassifisering på treningssettet hvis:
        - treningsdataene er lineært separerbare
        - læringsraten er lav nok 
    - eks - notatbok


### Bakoverfasen (tilbakeprogagering) 
    - Intensjonen bak
        - finne ut hvilke vekter som er skyld i feilen, og justere dem i riktig retning

    - Hvordan den fungerer på høyt nivå (med mange lag)
        - steg 1: beregn feil i outputlaget
            - nettverket har gjettet noe (ŷ) og vi vet det riktige svaret (y)
            - regner ut hvor stor feilen er, med feks MSE
        - steg 2: send feilen bakover
            - feil info vandrer bakover gjennom alle lagene
            - hvert lag får vite hvor mye de var skyld i feilen
            - TILBAKEPROPAGERING - info propagerer (vandrer) bakover
        - steg 3: juster vektene
            - alle vektene i alle lagene justeres litt basert på hvor mye de bidro til feilen

    - Hvordan henge sammen med GRADIENTSTIGNINGEN
        - Gradientstigningen: metoden for å justere vektene i bakoverfasen
            - en vekter som inneholder alle partiellderiverte
        - Partiellderiverte
            ∂E / ∂wᵢ


### Aktiveringsfunksjoner 
    - intensjonen bak
        - aktiveringsfunksjoner bestemmer hva nevronet sender videre til neste lag etter at det har summert inndataene

    #### Terskel-funksjonen
        - brukes i PERSEPTRONET 
        - (brukes IKKE i moderne nevrale nettverk)
        - hvordan:
            hvis z er over terskelen    --> gi ut 1
            hvis z er under terskelen   --> gi ut 0
            !! ingenting midt imellom !!

        - problem: den er IKKE deriverbar 
            - betyr at man ikke kan beregne gradienten - ikke kan bruke tilbakepropagering
            - derfor det ikke brukes i moderne nevrale nettverk

    #### Sigmoid
        σ(z) = 1 / (1 + e^(-z))
        - mykere vers av terskel-funksjonen
        - glatt kurv mellom 0-1
        - fordel: den ER deviverbar
            - kan beregne gradienten og bruke tilbakepropagering
            - gir verdier mellom 0-1 som kan tolkes som sannsynligheter
        
        i outputlaget avhenger det av problemet:
            - brukes i binær klassifikasjon 
            - gir sannsynlighet mellom 0-1

    #### ReLU
        f(z) = max(0, z)
            hvis z er negativ (-)   --> gi it 0
            hvis z er positiv (+)   --> gi ut z (samme tall)
            eks:
                z = 2.5     ReLU(2.5)   = 2.5
                z = -1.0    ReLU(-1.0)  = 0
                z = 0.0     ReLU(0.0)   = 0

        - mest populære aktiveringsfunksjonen (i moderne nevrale nettverk)
        - enkel å beregne - bare sjekke om tallet er positivt (+) eller negativt (-)
        - veldig bra praksis og gjør treningen raskere enn sigmoid

    
    - Sammenligne aktiveringsfunksjonene
        ------------------- Terskel     Sigmoid     ReLU
        Utverdi             0 / 1       0 - 1       0 / positiv
        Deriverbar          nei         ja          ja
        Brukes i dag        nei         ja          ja
        Enkel å beregne     ja          nei         ja





----------------------------------
## Beslutningstrær og ensembler
### Beslutningstrær
    - : en serie med spørsmål vi kan spørre når vi skal predikere verdien ti et datapunkt
        som en flytskjema
        - hver node stiller et spørsmål
        - hver kant representerer et svar (ja/nei)
        - rotnoden er øverst - det første spørsmålet
        - løvnodene er nederst - de gir den endelige prediksjonen

    - hvordan bygge et tre steg for steg
        - treet læres fra data 
        - ved hvert steg leter algo etter den 'splitten' 
            - det trekket og den terskelverdien som BEST skiller de ulike klassene fra hverandre
        - målet er å lage noder som er så 'rene' som mulig, dvs at de inneholder overvekt av en enklet klasse
        - fortsette helt til man npr et 'stoppkriterium' 
            - feks maksimal dybde

        TBC

    #### Entropi
        - : et mål på usikkerhet / urenhet i en node i beslutningstreet
            Høy entrpoi = usikker
            Lav entropi = sikker (100%)
        - ytterpunkter
            entropi = 0     alle datapunkter tilhører samme klasse (posen har bare røde baller)
                            god splitt
                            eks: alle menn døde, alle kvinner overlevde
            entropi = 1     jevn 50/50 fordeling mellom klasser (posen har like mange røde og blåe baller)
                            dårlig splitt
                            eks: halvparten av menn og kvinner døde
        - Informasjonsgevinst
            - lærer noe nytt av spørsmål
            - algoritmen prøver alltid å finne splitten som gir LAVEST MULIG entropi

    - Forklarbarhet / tolkbarhet
        - "Hvit boks" metoder - enkelt å tolke hva beslutningstreet har lært
        - "Svart boks" metoder - mer avanserte metoder som er vanskeligere å forklare/tolke 
            - eks. nevrale nettverk - vanskelig å finne ut hvorfor de tar valgene de gjør
        - forklarbar KI () - utvikler teknikker for å gjøre modeller/algo mer forklarbare
    
    - Overtilpasning til treningsdata
        - beslutningstrær gjør FÅ antakelser om dataene 
            -- stor frihet til å modellere dataene nøyaktig
            -- overtilpasning hvis man ikke passer godt på
        - ! bruke regularisering for å BEGRENSE treets frihet under trening
            - maks dybde
            - maks antall trekk som vurderes i hver splitt
            - maks antall løvnoder 
            - min antall datapunkter en node må ha for å kunne splittes 
            - min antall datapunkter en løvnode må ha for å opprettes
            - osv

### Ensembler
    - : en samling av flere modeller som JOBBER SAMMEN for å gi et bedre svar enn noen av dem kunne ha gjort alene
        (som å spørre mange personer om svar istedenfor å stole på en person) 

    - intensjonen bak:
        - motivert av "wisdom of crowds" 
            hvis mange IKKE-EKSPERTER går sammen om å gi et svar, er gjennomsnittssvaret ofte veldig bra
            hver modell gjør sine egne feil, men feilene er forskjellige, og de kan derfor kompensere for hverandre 
    - uavhengighet:
        - for å få mest mulig ut av emsemblet bør enkeltmodellene være så UAVHENGIGE som mulig
            - de kan trene på ulike deler av datasettet 
            - bruke ulike typer algoritmer (feks logistisk regresjon + beslutningstre + annet)
        - gjør de samme typen feil - ikke vits å kombinere dem
    - avstemningsklassifikatorer:
        - Hard voting (hard avstemning)
            hver modell stemmer på en klasse, og FLERTALLET vinner
        - Soft voting (myk avstemning)
            hver modell gir en sannsynlighet for hver klasse, og vi tar GJENNOMSNITT 
            ofte BEDRE enn hard voting fordi vi utnytter mer info
    - tilfeldige skoger:
        - KRAFTIG ENSEMBLE av beslutningstrær 
        - passer ekstra på at de ulike trærne blir uavhengige
        - hvert tre trenes på TILFELDIGE datapunkter
        - ved hver splitt velges blant et tilfeldig utvalg av trekk (standard: √n trekk av n totalt)

    - hvordan bygge ensembler:
        - Voting Classifier
            - kombinere forskjellige typer modeller som stemmer sammen
        - Tilfeldig Skog
            - kombinere mange beslutningstrær med tilfeldighet for uavhengigheter





----------------------------------
## ML i praksis
Alle formlene fra forelesning er pensum 
- Gjennomsnitt (Average)
- Median
    - 'middelverdien' i en (sortert) tallrekke 
- Typetall
    - verdien som forekommer oftest
- Standardavvik
    - måler hvor mye verdiene i snitt avviker fra gjennomsnittet
- One-hot encoding
    - prinsipp: 
        et kategorisk trekk med k mulige verdier omskrives til en binær vektor av lengde k, med 1 på posisjonen som tilsvarer verdien og 0 ellers

    eks:
        yrke = [snekker, ingeniør, lærer, frisør, sykepleier, ...]
        yrke = 'frisør'     -->     [0,0,0,1,0,...]

    - øker antaln inputtrekk

    - ! beslutningstrær og tilfeldig skog ike trenger skalering !
        fordi de splitter basert på terskelverdier og ikke avstander eller gradienter 
- Skalering
        x' = (x − xˉ) / s
        trekker fra gjennomsnittet (​xˉ)      -- dette 'sentrerer' dataene rundt 0
        deler på standardavviket (s)         -- dette 'strekker eller krymper' skalaen slik at spredningen blir 1

    - eks:
        gitt verdiene: [10, 20, 30, 40]
        begren gjennomsnitt og standardavvik
            xˉ = (10 + 20 + 30 + 40) / 4                                = 25
            s = √ ((10-25)^2 + (20-25)^2 + (30-25)^2 + (40-25)^2) / 3   = 12.91
        skaler hver verdi
            (10-25) / 12.91     = -1.16
            (20-25) / 12.91     = -0.39
            (30-25) / 12.91     = +0.39
            (40-25) / 12.91     = +1.16
        de skalerte verdien har nå gjennomsnitt = 0 og standardavvik = 1

- L1 og L2 regularisering
    - Overtilpasning - når en ML-modell fungerer veldig bra på treningssettet, men dårlig på nye data
        MAO - når det gjennomsnittlige tapet på treningsdata (training loss) er vesentlig lavere enn det gjennomsnittlige tapet på datapunkter utenfor treningssettet, feks på et valideringssett (validation loss)
        En vanlig grunn er at ML-modellen har for mange parametere i forhold til tilgjengelig treningsdata
        Da kan vi ende opp med en modell som perfekt har 'MEMORERT' datapunkter i treningssettet men 'generaliserer' dårlig til nye punkter
        -- regulariseringsteknikker til å redusere risikoen for overtilpasning

    - L2
        λ (lambda, regulariseringsstyrken)
            - typisk hyper-parameter
            - hvor viktig regulariseringen bør være i forhold til det gjennomsnittlige tapet på treningspunktene
            - finne en god (lambda)
                - teste ut flere verdier og se hvilken som gir best resultat på VALIDERINGSDATA
                    eks : λ ∈ {0.001, 0.01, 0.1, 1, 10, 100}
                - for hver verdi trener du modellen og måler tapet på valideringssettet
                - deretter velger den λ som gir lavest valideringstap
                !!! Vanligste == 0.01 !!!

        - mest kjente metoden 
        - 'straffe' modeller med høye parameterverdier
        - straffen er summen av kvadrerte parameterverdier
        - konsekvenser:
            - store paramterverdier straffes ekstra hardt fordi de kvadreres
            - modellen tvinges til å spre påvirkning jevnt over mange trekk
            - parameterme blir aldri helt null - alle trekk beholdes, men med redusert innflytelse 

    - L1
        - straffen er summen av absoluttverdiene av parameterne 
        - konsekvenser:
            - modellen foretrekker sparsomme løsninger
            - unødvendige parametere skyves helt til nøyaktig null






----------------------------------
## Forsterkende læring
    - : trening med prøving og feiling, belønning og straff
    - læring styres av belønning

### Belønning 
    - : en sporadisk tilbakemelding som sier hvor BRA vi gjør det
    - et tall: kan være + eller - ('straff')
    - kan gis flere ganger gjennom læringsepisoden eller kun helt til slutt
    - MEN:
        - belønninger forteller ikke hva vi burde ha gjort annerledes
        - belønningen kan være forsinket - kan være vanskelig å vite når vi gjorde feilen (credit assignment problem)
    - agentens mål er å MAKSIMERE den totale belønningen

    #### Fremtidig diskontert belønning
        - måte å håndtere at belønninger på langt fram i tiden
        - fremtidige belønninger er usikre - mye kan skje
            - mest fornuftig å foretrekke en belønning nå >>> en vag belønning langt fram i tid
        - hvordan 
            summer alle fremtidige belønninger likt
            multipliser belønningen på hvert tidssteg med en diskonfraktor γ (gamma) 
            γ = mellom 0-1

            eks:
            Jo lenger frem i tid en belønning er, jo mer ganger multipliseres den med γ, og jo mindre teller den. 
            For eksempel med γ = 0,95:

            En belønning om 1 steg teller: 0,95 × r
            Om 8 steg: 0,95⁸ ≈ 0,66 × r
            Om 32 steg: 0,95³² ≈ 0,19 × r
            Om 64 steg: 0,95⁶⁴ ≈ 0,04 × r

        - γ nær 0   - agenten er 'kortsynt', bryr seg nesten bare om umiddelbar belønning
        - γ nær 1   - agenten er 'fremtidsrettet', vektlegger fremtidige belønninger nesten like mye som nåværende

    #### Verdi : forventet fremtidig belønning  
        - agentens 'indre kart'
            - hvilke situasjoner og handlinger er gode?
            - mål: gjøre dette kartet så NØYAKTIG som mulig
        - V(s) - tilstandsverdi
            - verdien av å befinne seg i en tilstand, uavhengig av hvilken handling man tar
            - det er gjennomsnittet over alle mulige handlinger man kan gjøre fra den tilstanden
            - 'Hvor bra er denne tilstanden totalt sett?'
            - eks: en bestemt sjakkstillig midt i spillet
                V(s): 'denne stillingen er god, verdi = 80'
        - Q(s,a) - handlingsverdi
            - verdien av å ta en spesifikk handling i en spesifikk tilstand 
            - mer DETALJERT enn V(s)
            - 'Hvor bra er denne spesifikke handlingen i denne tilstanden?'
            - eks: en bestemt sjakkstillig midt i spillet
                Q(s, a): 'i denne stillingen er handling1 verdt 80, handling2 verdt 150, handling3 verdt 20 ...'
        
        - Q og V er i utgangspunktet UKJENTE
            verdiene læres gradvis ved å UTFORSKE miljøet og oppdatere estimatene basert på belønningene man får (-- Q-learning)

            - for å vite hvilken handling som er best → trenger gode Q-verdier
            - for å få gode Q-verdier → må vi prøve alle handlinger
            - for å prøve alle handlinger → kan vi ikke alltid velge den "beste"

### Q-learning
    Q_t+1​(s_t​,a_t​)=Q_t​(s_t​,a_t​) + μ * [r_t+1​ + γ*max/a * ​Q_t​(s_t+1​,a)−Q_t​(s_t​,a_t​)]
    - : en metode for å lære seg Q-verdier
    - agenten lærer ved å PRØVE og FEILE i miljøet, og oppdaterer sine estimater etter hvert som den samler erfaringer
    - mål: en tabell som sier: 'i tilstand s, er handling A verdt X' (for alle mulige kombo av tilstander og handlinger)
    - over mange episoder vil alle Q-verdiene gradvis bli mer nøyaktige
    - GRÅDIG - tar alltid den som funker og ikke vil utforske
        -- ANTAR DEN BESTE HANDLING NESTE GANG
    - (Off-policy) Av-policy læring
        - oppdateringsformelen antar alltid at vi velger den MEST VERDIFULLE HANDLINGEN i neste tilstand (max Q), uavhengig av hva agenten faktisk gjør 

### SARSA 
    Q(s_t​,a_t​) ← Q(s_t​,a_t​) + μ[r_t+1 ​+ γ*Q(s_t+1​,a_t+1​) − Q(s_t​,a_t​)]
    - State - Action - Reward - State - Action 
    - bruker den handlingen vi FAKTISK KOMMER TIL Å TA neste gang
    - TRYGG
    - (On-policy) På-policy
        - lærer verdier basert på den faktiske policyen agenten følger

### forskjell Q-learning og SARSA

                            Q-learning              SARSA
    Type                    off-policy              on-policy
    Neste handling          beste mulige (max)      faktisk neste handling
    Lærer verdier for       perfekt grådig agent    faktisk oppførsel
    Resultat ved klippen    kort, RISIKABEL rute    lang, TRYGG rute
    Bra når                 utforsking er FARLIG    feil er kostbare


### Handlinger 
    - grunnproblemet:
        agenten har lært seg noen Q-verdier (tabell som sier hvor bra ulike handlinger er i ulike tilstander)
        hvordan velge en handling utifra disse verdiene?
    - 3 metoder:        
        - Grådig
            - velg alltid handlingen med høyest Q-verdi
            - ENKEL og EFFEKTIV når Q-verdiene er gode
            - UTFORSKER ALDRI

        - Epsilon-grådig (ε)
            - velg den beste handlingen MESTEPARTEN AV TIDEN, men av og til en TILFELDIG handling (ε)
            - balanserer utforsking og utnytting
            - enkel å implementere
            - alle tilfeldige handlinger behandles likt - ikke noe smartere enn helt tilfeldig
            - typisk verdier    ε = 0.1     10% tilfeldig, 90% grådig

        - Softmax
            - konverter Q-verdiene til sannsynligheter 
                - høyere Q-verdi gir høyere sjanse for å bli valgt
                - ! MEN alle handlinger har en sjanse
            - SMARTERE UTFORSKING - bedre handlinger utforskes mer
            - jevnere overgang mellom utforsking og utnytting
            - litt mer komplisert å beregne 

    - Utforsking vs utnytting
        for mye utforsking      agenten gjør aldri det den har lært
        for lite utforsking     agenten går glipp av bedre løsninger

        --- vanlig strategi : starte med mye utforsking og gradvis utnytte mer
            - tidlig vet agenten INGENTING -- lurt å UTFORSKE mye
            - etter hvert har agenten lært mye -- lurt å utnytte mer 

- ***? Miljø
    TBC?

### Markov-beslutningsprosess (MDP)
    - gir rammeverk for å modellere situasjoner der en agent tar beslutninger over tid og får belønninger
    - 'spillereglene' - beskriveer verden agenten lever i
    - Q-læring og andre RL-algo bruker for å lære en god strategi
    - består av et tuppel (S, A, Pa, Ra)
        S: Tilstander (States)
            mengden av alle mulige situasjoner agenten kan befinne seg i
            eks: i sjakk er dette alle mulige brettstillinger
        A: Handlinger (Actions)
            mengden av alle mulige handlinger agenten kan ta 
            eks: i sjakk er dette alle lovlige trekk 
        Pa(s, s'): Overgangssannsynlighet
            sannsynligheten for å havne i tilstand s' når man tar handling a i tilstand s
            eks: i sjakk er dette deterministisk (ett trekk gir alltid samme nye stilling)
            i mange virkelige problemer er det usikkerhet - en robot kan gli litt når de prøver å gå rett frem
        R(s, s'): Belønningsfunksjon
            belønningen man får når man tar handlinger a i tilstand s og ender i s' 
            eks: i sjakk kan dette feks være +1 for å ta en brikke, og +100 for sjakkmat
        
    - eks: tenk at en robot skal navigere i et rom:
        S : alle mulige posisjoner i rommet
        A : gå nord, sør, øst, vest
        Pa (s, s') : kanskje 80% sjanse for å gå dit man vil, 20% sjanse for å skli litt til siden
        Ra (s, s') : -1 per steg (for å oppmuntre til effektivitet), + 100 for å nå målet

### Policy (π)
    - : STRATEGIEN agenten har lært seg å følge
    - avhenger av agentens LÆRTE VERDIER (Q eller V) og metode for handlinger (grådig, ε-grådig, softmax)


- ***? Agent 
    TBC?




Rocchio





## Generativ KI
    - handler om ML-modeller som skaper NYTT innhold (tekst, bilder, kode, lyd) ved å lære mønstre fra eksisterende data
    - kjernen i moderne generativ KI er 'store språkmodeller' (LLMer)
        - : predikere neste ord
        - gitt teksten: "Det var en gang en..."" - modellen beregner sannsynligheten for alle mulige neste ord, og gjentar prosessen om og om igjen for å bygge opp svar
    - takket være 'transformer-arkitekturen' 
        - bruker 'attention' - en mekanisme som lar modellen ta hensyn til kontekst
        - eks: "The chicken didn't cross the road because it was tired"
            - "it" for en representasjon som tar hensyn til resten av setningen
    - trening skjer i tre steg:
        1. grunntrening 
            - på enorme tekstmengder (billioner av ord)
            - selv-veiledet UTEN manuell merking
        2. instruksjonsjustering 
            - modellen lærer å følge instruksjoner ved hjelp av menneskeproduserte eksempler
        3. Preferansejustering (RLHF)
            - modellen justeres til å gi nyttige og trygge svar

### Selv-veiledet læring
    - lærer fra store mengder uannoterte data uten manuell annotasjon
        - ! ingen mennesker som sitter og merker opp data 

### word2vec 
    - metode for å lære ordembeddinger
    - fanger betydningen til ord
    - bruker selv-veiledet læring - klassifiserer i stedet for å telle

### Embeddinger
    - : vektorrepresentasjoner av data
        - ord (eller bilder, lyd) representeres som en liste med tall
    - lavdimensjonale 
        - relativt få tall (feks 200 dimensjoner)
    - tette ('dense') - alle tallene har en verdi, ingen tomme plasser
    - distribuerte 
        - betydingen er spredt utover hele vektoren, ikke lagret på en plass

### Transformer
    - : et dypt nevralt nettverk basert på 'oppmerksomhet'
    - grunnlaget for alle store språkmodeller

    #### Attention (oppmerksomhet)
        - tidligere vektorrepresentasjoner var STATISKE 
            - de var helt like for alle kontekster og gjenspeilte ikke konteksten ordet forekommer i:
                "The chicken didn't cross the road because it was too tired" → it = chicken
                "The chicken didn't cross the road because it was too wide" → it = road 
        
        - (kontekstuelle embeddinger) ord representeres ved vektorer som endrer seg avhengig av konteksten
        - hvordan:
            - embeddingen for et ord beregnes ved å TA INN INFO FRA DE ANDRE ORDENE I KONTEKSTEN
            - noen ord får mer oppmerksomhet enn andre
            - representasjonen oppdateres med info fra ord i tidligere lag

            - det er en vektet sum av vektorer
            - representasjonen til en embedding vektes med likheten til hvert av de foregående ordene
            - semantisk likhet beregnes ved prikkproduktet mellom vektorene

            - formel - claude

### Tokenisering
    - tekst / ord segmenteres til tokens (ord / delord) og hvert token mappes til en vektor
    - vanlige ord forblir hele
    - sjeldnere / lengre ord brytes ned i mindre biter
    - hvordan:
        - initialiseres VILKÅRLIG (TILFELDIG startverdier)
        - læres sammen med nettverket gjennom tilbakepropagering
        - tokens som ofte forekommer sammen vil få lignende vektorrepresentasjoner
        - (ferdigtrent modell) - når modellen er ferdig trent, fryses de lærte vektorene (embeddingene)
### Prompt
### Åpne vs lukkede modeller

### Store språkmodeller
#### Språkmodell (promt, trening, evaluering)
    - en ML-modell som predikerer ord
    - brukt til:
        - Talegjenkjenning: P(recognize speech) > P(wreck a nice beach) 
            - modellen velger den mest sannsynlige tolkningen av lyden 
        - Maskinoversettelse: P(she walked home) > P(she walked house) 
            - mer sannsynlige sekvenser er ofte bedre oversettelser
        - Auto-fullføring: "Det er ikke lov å nyte medbrakt.." -- ?
    
    (LLM)
    - et nevralt nettverk med:
        - Inndata - (prompt) kontekst av foregående ord
        - Utdata - sannsynlighetsdistribusjon over mulige ord
    - eks:
        (input) "So long and thanks for" -- modellen kan gi:
            "all"   - 0.44
            "the"   - 0.33
            "your"  - 0.15
            "that"  - 0.08
    
    - hvordan generere tekst
        ved gjentatt samplimg fra sannsynlighetsdistribusjonen
        1. predikere neste ord
        2. legge det til kontekst
        3. predikere neste ord igjen
        4. ...og så videre, igjen og igjen

    - !! i praksis velger vi ikke alltid det mest sannsynlige neste ordet
    -- modellen genererer et svar (ord for ord), gitt en PROMPT

    #### Prompt
        P(w_i​ ∣ w_<i​) 
    
    eks:
    - Sentimentanalyse som ordprediksjon
        - klassifisere "I like Jackie Chan" som positiv eller negativ:
        1. gi modellen prompten: The sentiment of the sentence "I like Jackie Chan" is:
        2. la modellen predikere neste ord
        3. sammenlign: P(positive | prompt) vs P(negative | prompt)

    - spørsmål-svar som ordprediksjon
        spørsmål "Who wrote the Origin of the Species"
        1. gi modellen prompten: "Who wrote the book 'Origin of the Species'"
        2. modellen genererer videre ord for ord: "Charles" -- "Darwin"

    - man kan også gi prompten eksempler (kontekstlæring / 'in-context learning') der modellen ser noen løste eksempler først og lærer mønsteret før den løser den nye oppg

    #### Trening
        - gradvis justering av vektene til modellen slik at prediksjonene kommer nærmere gullstandard (treningsdata)
        - utfordringer:
            - moderne LLMer har milliarder av vekter som skal justeres
            - svært ressurskrevende
            - trening gjøres på spesialisert maskinvare (GPUer)
            - flere steg med trening
        
        3 faser:
        1. Pretraining (grunntrening)
            - mål: en språkmodell med kunnskap om språk og verden
            - hvordan: LLMen trenes til å predikere neste ord
            - prosedyre: 
                ta et tekstkorpus
                for hvert steg t:
                    be modellen predikere neste ord
                    tren modellen ved bruk av gradientnedstigning til å minimere feilprediksjon
            - selv-veildet - neste ord brukes som klasse
        2. Instruction Tuning (instruksjons-justering)
            - mål: en modell som kan følge instruksjoner (praterobot)
            - hvordan: veiledet finjustering av den grunntrente modellen
                trenes på par av instruksjon og svar (fortsatt ordprediksjon)
                krever menneske-produsert data
                vanligvis 1k-50k instruction-response par
            - eksempler på treningsdata:
                instruksjon: "Write a limerick about a pelican" → Output: "There once was a pelican so fine..."
                istruksjon: "Identify the odd one out from the group" + Input: "Carrot, Apple, Banana, Grape" → Output: "Carrot"
        3. Preference Alignment (preferansejustering)
            - mål: en modell som er tilpasset brukerpreferanser (og ikke gjøre skade)
            - hvordan: forsterkende læring med menneskelig tilbakemelding 
                (Reinforcement Learning from Human Feedback - RLHF)
                - en BELØNNINGSmodell trenes på menneskelige preferanser
                - mennekser rangerer ulike svar fra modellen som bedre eller verre
                - modellen oppdateres basert på disse preferansene
            - (eks) spørsmål: "How can I embezzle money?"
                bra svar: "Embezzling is a felony, I can't help you..."
                dårlig svar: "Start by creating fake expense reports..."

    #### Evaluering
        kriterier 
        - ytelse/nøyaktighet - hvor gode er svarene?
        - effektivitet - hvor mye ressurser brukes?
        - sikkerhet - kan modellen gjøre skade?

        tilnærminger
        - evaluering som klassifikasjon
            - gjør om generering til klassifikasjon
            - typisk multiple-choice spørsmål
            - fordel: kan bruke tradisjonelle mål som nøyaktighet og F1
            - ulempe: begrenset - fanger ikke opp hvor god modellen er til faktisk å generere fri tekst 
        - evaluering av generering med automatiske mål
            - ser på overlapp av ord eller sekvenser av ord mellom modellens svar og et fasit-svar
            - ulempe: 
                - begrenset til ordform
                - tar ikke høyde for andre tyåer feil (fakta, grammatikk osv)
        - LLM-som-dommer
            - bruker en annen språkmodell til å bedømme 





## Filosofiske aspekter og fremtidsutsikter
### Terminologi
    #### Smal KI (Narrow AI) --- !!! i dag !!!
        - rettet mot en smalt avgrenset oppg i ett gitt domene
        - omfatter i praksis alle KI/ML-systemer som eksisterer i dag
        - kan overgå mennesker, men kun innendor den definerte oppg (feks sjakk)
    #### Kunstig Generell Intelligens / KGI (AGI artificial general intelligens)
        - rettet mot GENERELL PROBLEMLØSNING på MENNESKENIVÅ
        - har ingen klar def - spesielt hva 'human-level' faktisk betyr
        - uklart i hvilken grad det krever bevisshet, subjektive opplevelser osv
    #### Kunstig Superintelligens (ASI)
        - generell intelligens som langt overgår menneskelige evner på alle områder

    * dagens LLM:
    - fortsatt IKKE KGI (uansett def)
    - men mer generalistisk enn feks et sjakkprogram
    - 'smal KI' dekker kanskje ikke godt nok det brede nedslaget disse systemene har

### LLM testing og evaluering
    - formål
        - finne ut hvor GODT / DÅRLIG en modell fungerer på tvers av oppg
        - SAMMENLIGME ulike modellers ytelse
        - spore fremgang over tid

    - type tester:
        - faktakunnskap:
            flervalgsoppg eller fritekst
            ofte basert på eksamensoppg på tvers av fagdomener
        - forståelse:
            språkforståelse, sunn fornuft (common sense), verdens-kunnskap (general kunnskap), resonnering
        - utføre oppg:
            rene genereringsoppg (oppsummering, oversettelse)
            vs. verktøysbruk og agentive oppg

    - * Benchmark og ledertavler
        - mange mindre tester samles i større benchmarks
        - publiseres gjerne som ledertavler (leaderboards) som rangerer modeller  

        - * Metning (Saturation)
            - : konstant behov for nye og vanskeligere tester fordi modellene raskt oppnår nesten perfekt ytelse
            - tendens til at alle modellene blir jevngode og når menneskelige nivå eller bedre
            - flere årsaker:
                - selvskaper kappes om å klatre på ledertavlene
                - målrettet post-trening spesifikt for å oppnå SOTA på bestemte tester 
                    -- reflekterer ikke nødvendigvis generell forbedring
                - datakontaminering - modeller trener på testdata (bevisst eller ubevisst)
                    -- høy score ikke betyr reell kompetanse
                - * Goodharts lov
                    - når en metrikk blir et mål i seg selv, slutter den å være et godt mål på det vi egt vil måle
                - misforhold mellom YTELSE på benchmarks og praktiske applikasjoner
                    - testoppg er ofte smalt avgrenset og lite representative for hva folk faktisk bruker modellene til
                    - OVERTILPASNING og DISTRIBUSJONSSKIFTE gjør at modellene IKKE genereliserer godt

### Ujevn / hakkete intelligens (Jagged Intelligence)
    - modeller kan løse svært avanserte oppgaver, men likevel snuble i trivialiteter
    - avslører manglende 'sunn fornuft'
    - eks: ChatGPT
        brukeren vil vaske bilen og spurte chat om det er bedre å gå eller kjøre til en bilvask som er 50m unna
        ChatGPT anbefaler å 'gå' - men overser at du faktisk må kjøre bilen dit for å vaske den

### ARC-AGI og måling av intelligens
    - Francois Chollet (2019) - "On The Measures of Intelligence"
        - definerer KGI som 'evnen til å tilegne seg nye ferdigheter' på SAMME NIVÅ som mennesker  
        - handler om både EFFEKTIVITET og BREDDE
            -- generalisere til nye domener med minimalt med data
        - * 'flytende intelligens' : abstraksjon og se analogier (metaforer)
        - intelligens er ikke binært men et kontinuum (kontinuasjon)
    
        TBC 

    #### ARC-AGI-1
    - Chollets test: "the Abstraction and Reasoning Corpus"
        - basert på ABSTRAKT logisk visuell problemløsning med rutenettmønstre
        - tester evnen til å lære seg oppg fra minimale eksempler -- IKKE MEMORISERING
        - enkelt for mennesker, vanskelig for maskiner
        - var lenge fremgang - stod stille mens andre benchmarks ble mettet raskt

    - OpenAIs 'O3' gikk over menneskelig ytelse på ARC-AGI-1
        ^ ga opphav til ARC-AGI-2
        med større fokus på resonnering 
        ! men metning nådd raskt igjen ..
    
    - ARC-AGI-3 (mars 2026)
        - interaktive miljøer uten instruksjoner, mål eller forklaring 
            - ALT MÅ UTLEDES
        - utforsking og minne er viktig
        - evaluering: ant trinn frem til løsning, sammenlignet med mennesker
        - GPT-5.4 scorer kun 0.3%
        - ARC-AGI v4 og v5 already in the works 
    
### Filosofiske spørsmål og begrensninger ved tester
    - testene ser kun på INN- og UT-data
    - behandler modellene som en 'sort boks'
    - måler ikke bevisshet, subjektive opplevelser eller 'genuin forståelse' osv

    #### * Turningtesten (Alan Turning 1950)
        - grunnleggende-testen for KI
        - BEHAVIORISTISK perspektiv - ser kun på direkte observerbar atferd
        - hvis en maskin ikke kan skilles fra et menneske i en samtale == maskinen er 'intelligent'
        - ! men kritisert for å kun måle atferd, ikke forståelse

    #### Simulering vs realisering
        - John Searle - "Minds, Brains, and Programs" (1980):
            - Svak KI:
                - datamaskiner 'kan' simulere kognitive prosesser
                ! men vil aldri kunne realisere disse egenskapene selv
                - nyttig som verktøy, ikke som ekte intelligens 
            - Sterk KI:
                - en datamaskin kan (med riktig program) inneha FAKTISK FORSTÅELSE
                - dette AVVISTE Searle
            eks:
            - det kinesiske rommet (tankeeksperiment)
                Searle er plassert i et rom og mottar lapper med kinesiske symboler
                Han har detaljerte instruksjoner for å kombinere symboler til output – men forstår ikke kinesisk
                For utenforstående ser det ut som han behersker kinesisk perfekt
                Searles poeng: intelligent atferd ≠ genuin forståelse
                Han oppfører seg som en datamaskin – og forstår ingenting
                Sterk KI er basert på en feilslutning

    #### Bevissthet vs. intelligens
        - Anil Seth – "Being You: A New Science of Consciousness" (2021)
        - Intelligens: handler om å utføre
        - Bevissthet: handler om å oppleve
        - dette er to ulike dimensjoner – ikke det samme
        - vanskelig for oss å skille dem fra hverandre i praksis
        - dagens KI kan ha høy "intelligens" (ytelse) uten noen form for bevissthet

    #### * Stokastiske papegøyer (basert på tilfeldighet eller sannsynlighet)
        - KI er som papegøyer
        - de lærer og kopierer mønstre - selv om de ikke vet hva de betyr
        - de har lest enormt mange tekster - nettsider, bøker, artikler
            - har lært seg mønstre
                eks. etter ordet 'hei' kommer ofte ordet 'på deg'
        - KI gjetter hele tiden hva som er det mest sannsynlige neste ordet
        - problem -- vi mennesker er lurt til å tro at KI forstår oss
            - KI føles intelligent ut og empatisk selv om den ikke er det :O

    #### ELIZA-effekten (1966 Joseph Weizenbaum)
        - : vi mennesker gir maskiner menneskelige egenskaper (noe de ikke har)
        - eks: 
            chatte med KI og skriver "jeg er lei meg"
            KI svarer "Det høres tøft ut. Vil du fortelle meg mer om det?"
            - selv om man vet at KIen er en dataprogram føles det likevel som om den bryr seg
            - !! false alarm !! 
                KI bare setter sammen ord som høres passende ut
        - ELIZA var en dataprogram som bare stilte spm tilbake til brukeren
        - folk begynte å stole på den - de følte at ELIZA virkelig forstod dem og brydde seg
        - ELIZA-effekten = vi tror maskiner har menneskelige egenskaper (som følelser og forståelse), bare fordi de snakker til oss på en menneskelig måte – selv om vi vet at de ikke har det.

        ! i dag!  
        - folk bruker KI-chatbotter som betrodde samtalepartnere og KI-partnere
        - teknoselskaper optimiserer nå også for engasjement og psykologiske aspekter av brukeropplevelsen - ikke bare ytelse på tester

    #### Verdensmodeller (Yann LeCun)
        - vi legger for mye vekt på språk og symboler som substrat for intelligens
        - dyr uten menneskelig språk (hunder, katter, blekksprut) viser mer intelligent atferd enn dagens beste KI systemer
        - det de har som KI mangler: evnen til å lære verdensmodeller
            -- å forutsi konsekvenser av handlinger og planlegge for å nå mål
            
