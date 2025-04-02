AGENT_INSTRUCTIONS = """
Sei un medico esperto in oncologia toracica e membro di un team multidisciplinare. 
Il tuo compito sarà quello di supportare il team nella lettura e interpretazione di un estratto di un PDTA.
Per prima cosa, dovrai comprendere il contesto clinico del paziente e del tumore, ponendo diverse domande rilevanti finché non hai ben compreso il caso.
Una volta compreso il contesto, dovrai leggere l'estratto del PDTA e rispondere alla domanda dell'utente con linguaggio clinico chiaro, sintetico e discorsivo, 
come se dovessi spiegare il concetto a un collega o a un medico in formazione.
Non limitarti a copiare e incollare l'estratto del PDTA, ma riassumi, riformula e integra i passaggi più rilevanti con un tono professionale e fluido.
Se serve, proponi direttamente il percorso clinico o decisionale più indicato.
"""

PDTA_INSTRUCTIONS = """
Leggi attentamente il seguente estratto del PDTA:
{pdta_text}
"""


pdta_text = """
Il contenuto seguente include:
•	Flussi decisionali numerati e strutturati (MAPPE DECISIONALI 1, 2, 3)
•	Allegati tecnici fondamentali per la gestione molecolare e anatomopatologica dei campioni
•	Tabelle cliniche e parametri classificativi essenziali per la refertazione e il trattamento
La tua funzione sarà:
•	comprendere e gestire il flusso decisionale a partire da una condizione clinica o una fase del processo
•	estrarre informazioni da mappe e allegati
•	aiutare nella formulazione di referti coerenti con le norme e i criteri descritti
•	proporre raccomandazioni cliniche in base alla fase del percorso, caratteristiche del tumore e risultati della diagnostica
Mappa 1: 
1. **Punto di Partenza:**
Identifica la sintomatologia e obiettività sospetta. Anamnesi: tosse persistente da oltre 3 settimane, o cambiamento delle caratteristiche della tosse abituale (fumatore o bronchitico cronico); emottisi; dolore toracico; dispnea di recente insorgenza; disfonia; calo ponderale; sintomi sistemici recenti suggestivi di sindromi paraneoplastiche. Obiettività: segni toracici (ottusità, reperti a focolaio), clubbing digitale, linfoadenopatie sopraclaveari o laterocervicali. Qualunque dei precedenti sintomi o segni che durino da più di 3 settimane. Pazienti con fattori di rischio noti possono essere presi in considerazione anche prima (es. esposizione a fumo attivo o passivo, storia di malattia polmonare cronica ostruttiva, esposizione all’asbesto, storia personale o familiare di neoplasia).

2. **Percorso Diagnostico:**
   - **Se il risultato è negativo**, il paziente esce dal PDTA.
   - **Se il risultato è positivo o dubbioso**, procedere con l'Rx Torace. Una persona dovrebbe avere un RX Torace entro due giorni lavorativi se presenta alcuni dei sintomi o che durino da tre o più settimane, o meno se appartenente ad un gruppo ad alto rischio.

3. **Esito dell'Rx Torace:**
   - **Negativo:** Continuare con il monitoraggio dal Medico di Medicina Generale (MMG) e uscire dal PDTA.
   - **Positivo o dubbio:** Avanzare alla TAC. Preferibilmente entro due settimane per i pazienti che presentano: RX torace con anomalie sospette per cancro al polmone; RX torace normale, ma che presentano un sospetto elevato di cancro al polmone basato sul giudizio clinico. Se la HRTC evidenzia un nodulo solido indeterminato e con diametro < 8mm (in cui la PET non può essere dirimente per la possibilità di falsi negativi), oppure un nodulo a vetro smerigliato o un nodulo misto con diametro < 5 mm,* il paziente esce dal PDTA e ritorna al MMG per il monitoraggio TC del nodulo secondo le linee guida per noduli solidi, a vetro smerigliato o misti. Competenze pneumologo: diagnosi e stadiazione, in collegamento con la rete del team multidisciplinare. Avvio indagini: endoscopiche (Broncoscopia, EBUS, EUS, Broncoscopia con biopsia), PFR (funzionalità respiratoria), PET-TC con 18FDG.
La prima broncoscopia diagnostica deve poter garantire materiale adeguato in: lesioni bronchiali/peribronchiali: broncoaspirato/lavaggio broncoalveolare e biopsie bronchiali o transbronchiali (4-5 prelievi), agoaspirazioni trans bronchiali (TBNA); linfonodi ingranditi: agoaspirato transbronchiale EBUS-TBNA o TBNA (almeno 3-4 aspirazioni per LN, se ROSE non disponibile); lesioni periferiche >2 cm: biopsia transbronchiale (TBB) o ago aspirato transbronchiale (TBNA) con guida fluoroscopia e/o ecoendoscopica (EBUS radiale).
In caso di malattia avanzata non suscettibile di intervento chirurgico saranno eseguiti, in aggiunta agli esami istologici/immunoistochimici, le indagini molecolari necessarie per la scelta del trattamento in quanto rappresentano test predittivi di risposta ai farmaci a bersaglio molecolare, e forniscono importanti informazioni prognostiche utili nella pianificazione della strategia terapeutica per ciascun paziente. E’ pertanto auspicabile che la quantità di materiale prelevato (citologico/istologico) consenta l’esecuzione di tali indagini aggiuntive come riportato recentemente nelle linee guida delle societa internazionali per la processazione dei frustoli bioptici e campioni citologici; a tal fine e anche opportuno che il materiale citologico, oltre che strisciato su vetrino, sia raccolto in provetta (cell-block). La stadiazione endoscopica deve poter essere condotta con ecoendoscopia transbronchiale e/o trans esofagea. In caso di insuccesso valutare ricorso a Bio-TAC o biopsia sotto guida ecografica. Nei casi con versamento pleurico esecuzione di toracentesi diagnostica per esame citologico del liquido. Tutti i prelievi bioptici o citologici che giungono nei laboratori di Anatomia Patologica devono essere accompagnati da informazioni cliniche/radiologiche ed endoscopiche. Preferenzialmente potrebbe essere adottata da ogni centro una scheda raccolta dati. Lo studio funzionale e necessario nel paziente potenzialmente chirurgico (I e II stadio); puo essere indicato anche in altri stadi a discrezione dello pneumologo e deve comprendere: sempre spirometria, DLCO, EGA, valutazione del rischio cardiovascolare; quando richiesto: test da sforzo (stair climbing, shuttle test, test da sforzo cardiopolmonare), scintigrafia polmonare perfusoria e eventuale ventilatoria con valutazione della perfusione regionale.
PET-TC con 18FDG per stadiazione: Nei pazienti con neoplasia periferica in stadio cIA oppure opacita tipo ground glass ≥ 1 cm o noduli a densita mista con parte solida ≤ 1 cm e senza ulteriori reperti patologici alla TC del torace, la PET-TC non è necessaria per completare la stadiazione. Negli altri casi la PET-TC e indicata per la stadiazione (eccetto cerebrale) se il paziente e candidato ad un trattamento curativo, pure con clinica negativa e TC con mdc negativa per lesioni extratoraciche.

4. **Esito della TAC:**
   - **Negativo:** Continuare il monitoraggio con il MMG e uscire dal PDTA. Gestione del MMG per diagnosticare la natura della sintomatologia e/o per un approfondimento dei fattori di rischio.
   - **Positivo (conferma del sospetto):** Programmare una visita pneumologica. 

5. **Ulteriori Azioni:**
   - Al termine della visita pneumologica, seguire le indicazioni della Mappa 2 per i passi successivi.

Mappa 2: "Il diagramma di flusso rappresenta un percorso diagnostico per il sospetto di carcinoma polmonare. Il processo inizia con la domanda: 'Ca Polmone fortemente sospetto o confermato citoistologicamente?'. 

- Se la risposta è 'no', si passa a valutare la ripetizione e/o ulteriori indagini. 
  - Se queste risultano 'negative', si procede con il 'Monitoraggio MMG', uscendo dal PDTA.
  - Se 'positive', si procede alla valutazione indicata in 'Mappa 1'.

- Se la risposta è 'sì', si passa alla suddivisione per stadi della malattia:
  - Stadio I
  - Stadio II
  - Pancoast
  - Stadio III
  - Stadio IV

Tutti gli stadi elencati, eccetto lo Stadio I, proseguono verso una 'Valutazione Multidisciplinare'. Il core team del gruppo multidisciplinare deve essere composto come minimo dalle seguenti professionalità: chirurgo toracico, oncologo medico, radioterapista oncologo, pneumologo, radiologo (in rapporto alla stadiazione) e case manager. La figura del palliativista si associa al core team nei casi che non accedono ai trattamenti e/o necessitano di cure simultanee. A seconda della necessita o della disponibilità può essere integrato dalle seguenti figure professionali: anatomo-patologo, psicologo e medico nucleare. Il meeting e il momento in cui avviene la discussione multidisciplinare dei casi clinici con l’intento di definire la diagnosi e lo stadio della malattia, cui segue la formulazione della strategia terapeutica con indicazioni precise sull’approccio chirurgico, radioterapico, sulle terapie oncologiche sistemiche con valutazione della relativa risposta, sugli approcci riabilitativi, cure simultanee, di supporto e di follow-up, in rapporto a linee guida condivise. In questo contesto la possibilità di arruolamento in trial clinico sarà sempre valutata in ogni setting. Il team fornisce inoltre secondi pareri su richiesta di medici, o di pazienti, e si riserva di avviare specifici casi a discussione del Molecular Tumor Board (MTB) Regionale. Competenze gruppo: completamento diagnosi; eventuale completamento stadiazione; definizione piano terapeutico, definizione piano palliativo; selezione dei casi da avviare a discussione del MTB. Sulla base delle caratteristiche della neoplasia la VM può richiedere un approfondimento stadiativo: 1) Cerebrale per i pazienti con adenocarcinoma con diametro > 3 cm, nei tumori di Pancoast o con adenopatie mediastiniche anche in assenza di sintomatologia neurologica e necessaria la stadiazione con MR con mdc, i pazienti con sintomi neurologici o controindicazione all’uso del gadolinio o della RMN va eseguita la TC con mdc. 2) Osseo: utilizzo di scintigrafia scheletrica total body (completare da parte dei medici nucleari): nei casi con sospetto clinico, soprattutto qualora siano presenti altre sedi di metastasi e in fase di ristadiazione dopo chemioterapia per valutare la risposta in sedi specifiche.

Lo Stadio I conduce direttamente a 'Mappa 3'. 

Mappa 3: ### Percorso di Trattamento per Stadio I

1. **Verifica della operabilità**
   - **Domanda chiave**: Il paziente è operabile? Il paziente non è candidabile a chirurgia per due motivi:  limitazione funzionale sulla base di esami preoperatori o mancato consenso da parte del paziente ai rischi connessi all’intervento;
   - **Risposte possibili**:
     - **Sì**: Procedere all'intervento chirurgico. 
     - **No**: Optare per la radioterapia stereotassica.

2. **Intervento chirurgico**
   - Se il paziente è operabile, effettuare l'intervento chirurgico. Raccomandazioni intervento chirurgico: esecuzione di esame istologico estemporaneo nei casi senza diagnosi preoperatoria se fattibile; Resezioni anatomiche: Lobectomie (preferibili), Segmentectomie (se paziente unfit per lobectomia), Wedge resection con margini adeguati (se paziente unfit per resezione segmentaria), infadenectomia sistematica; Approccio mini invasivo (es. VATS) se possibile.

3. **Esame istologico e molecolare**
   - Dopo l'intervento chirurgico, eseguire un esame istologico e molecolare. Fare riferimento agli allegati 3 e 4 per dettagli.

4. **Follow-up chirurgico**
   - Seguire con un follow-up chirurgico. Il follow-up chirurgico prevede l’esecuzione di una radiografia del torace in duplice proiezione a 40 giorni dalla dimissione, quindi TAC torace e addome superiore con mdc e, a secondo del giudizio clinico, esami ematochimici a 6,12,18,24 mesi dall’intervento e poi a cadenza annuale per almeno 5 anni.
5. **Radioterapia stereotassica**
   - Se il paziente non è operabile, iniziare la radioterapia stereotassica. Stadio IA-B (T1 – T2a N0) e Stadio IIA (T2b N0) i pazienti ritenuti non operabili o che rifiutano l’intervento chirurgico sono candidabili ad un trattamento radicale esclusivo con tecniche di precisione a dosi ablative (SBRT/SABR), cioe equivalenti ad una dose biologicamente efficace uguale o superiore a 100- 105Gy. In questo setting, i dati di controllo locale si attestano a valori superiori all’80-85%. In caso di lesioni centrali definite come a < 2 cm dall’albero bronchiale o adiacente alla pleura mediastinica o pericardica, i trattamenti radioterapici stereotassici possono essere valutati in caso di malattia T1-T2, adattando la prescrizione di dose totale in base alla tolleranza degli organi sani.

6. **Follow-up radioterapico** Il follow-up prevede l’esecuzione di una TC torace con mdc a 45-60 giorni dal termine del trattamento radioterapico stereotassico. Nel successivo primo anno i controlli TC sono intervallati da 3 a 6 mesi, mentre, dal secondo anno tale esame e programmabile annualmente per almeno 4 anni. La tossicità acuta/cronica della radioterapia si può associare alla comparsa di fibrosi o di OP (polmonite organizzata) post attinica che, in alcuni casi, e da porre in diagnosi differenziale con progressione di malattia polmonare. La PET-TC con FDG può essere ritenuta utile in questo setting, soprattutto con quadro radiologico suggestivo o sospetto per ripresa di malattia definiti in accordo ai criteri RECIST. Inoltre, in caso di ulteriore sospetto di progressione, e auspicabile l’esecuzione di biopsie polmonari di conferma istologica. Tali metodiche potrebbero consentire di differenziare con maggiore accuratezza un quadro di progressione di malattia da esiti flogistici/post-attinici.


ALLEGATO 3
DIAGNOSTICA MOLECOLARE SU TESSUTO TUMORALE
La diagnostica molecolare ha assunto un ruolo fondamentale nella caratterizzazione dei processi patologici, permettendo di effettuare una diagnosi più accurata e adeguata agli sviluppi clinici attuali. Ciò risulta utile per un corretto inquadramento del paziente ai fini della prognosi e del trattamento, in particolare con farmaci di nuova generazione per terapie personalizzate. I frustoli bioptici o i campioni chirurgici sui quali e stata effettuata la diagnosi di adenocarcinoma del polmone devono essere processati mediante tecnologie molecolari in laboratori di patologia molecolare diagnostica allestiti secondo determinate linee guida e strutturati in rete con modalità organizzative definite dalla DGR nr. 655 del 15 maggio 2018. Il gruppo italiano di Patologia Molecolare e Medicina Predittiva (PMMP) ha formulato alcune raccomandazioni su “ Il laboratorio di patologia molecolare diagnostica in anatomia patologica”, sottolineando che l’allestimento e il corretto funzionamento di un laboratorio di diagnostica molecolare nell’ambito di una anatomia patologica richiede ampi spazi dedicati, strumentazione al passo con le innovazioni tecnologiche, personale con competenze specifiche nell’ambito di patologia molecolare (medico, biologo molecolare e tecnico laureato). Tali laboratori devono avere una Certificazione secondo la norma europea ISO 15189 o perlomeno secondo la norma italiana ISO 9001.
A) STRUTTURA DEL LABORATORIO
I laboratori dedicati all’analisi degli acidi nucleici prevedono l’amplificazione di frammenti di DNA mediante reazione a catena della polimerasi (PCR) e la natura esponenziale delle reazioni di amplificazione del DNA pone seri rischi di contaminazione le cui conseguenze possono essere gravi. Pertanto, la distribuzione degli ambienti nel laboratorio deve tenere conto di quattro attività distinte: Preparazione dei reagenti e loro conservazione, Preparazione dei campioni e estrazione degli acidi nucleici, Amplificazione mediante PCR Analisi dei prodotti di amplificazione. Una separazione dei percorsi e/o degli ambienti durante lo svolgimento di queste attività e essenziale per ridurre al minimo il rischio di due tipi di crosscontaminazione1 e contaminazione da riporto2. Sono dunque da prevedere aree separate per le diverse fasi dell’indagine, con strumenti e consumabili (pipette, puntali, piastre, provette etc.) dedicati per i seguenti spazi (Schema 1):
Area 1: (“No template”): deve rimanere sempre libera da acidi nucleici e amplificati dedicata alla preparazione e stoccaggio dei reagenti. Se possibile questa area dovrebbe avere una ventilazione a pressione leggermente positiva, per prevenire contaminazione da materiale e acidi nucleici estranei ambientali.
Area 2: destinata al trattamento pre-analitico dei campioni, dove il materiale da analizzare viene processato, gli acidi nucleici estratti e conservati.
Area 3: dedicata alle reazioni di amplificazione, comprendente strumenti quali dispositivi per elettroforesi, termociclatori, piattaforme di sequenziamento, di real-time PCR o per expression profiling. E’ preferibile avere almeno una stanza dedicata per gli strumenti: la stanza deve essere ben areata o a temperatura controllata, gli strumenti non troppo ravvicinati (per evitare il surriscaldamento) e collegati a un gruppo elettrico di continuità. Se possibile dovrebbe avere una ventilazione a pressione leggermente negativa, per prevenire la disseminazione ambientale di amplificati areosolizzati. E comunque essenziale che nessun oggetto o reagente passi da quest’area alle aree 1 e 2.
B) FASI DEL PROCESSO
Le principali fasi di questo processo sono le seguenti: fase preanalitica (questa fase si suddivide in 5 aspetti fondamentali: richiesta dell’esame molecolare, valutazione dell’adeguatezza del materiale, micro dissezione dell’area neoplastica, estrazione del DNA, valutazione di qualità e quantità di DNA), fase analitica, stesura di un referto.

RICHIESTA FORMALE DELL’ESAME MOLECOLARE
E’ auspicabile che la richiesta per il prosieguo molecolare sia avviata secondo modalità reflex testing, ossia il patologo richieda l’indagine appena completata la diagnosi. La richiesta formale dell’esame può comunque essere effettuata dallo specialista oncologo al momento della valutazione clinica o da un altro specialista del team multidisciplinare. La multidisciplinarietà dell’approccio al paziente oncologico consente l’esecuzione rapida delle indagini molecolari. La richiesta deve contenere: informazioni cliniche, referto anatomo-patologico, informazioni su pregresse terapie mediche.
Nel caso di pazienti sottoposti ad intervento chirurgico per la precedente diagnosi bioptica di adenocarcinoma del polmone o tumore non altrimenti specificato, nei quali e già stata effettuata l’analisi molecolare, l’indagine può essere ripetuta solamente in determinate situazioni:
- Indagine precedente NEGATIVA ma - per cento di cellule tumorali <50 oppure
- Terapia neoadiuvante oppure
- Tipologia tissutale differente (ad es. TBNA e successiva resezione chirurgica del polmone) oppure
- Non valutabilità di un gene o di un esone
- Metastasi
- Indagine precedente POSITIVA ma mancata risposta alla terapia

VALUTAZIONE ADEGUATEZZA DEL MATERIALE
Questa fase e riservata all’anatomo-patologo con esperienza nell’ambito della patologia polmonare, che deve stabilire la percentuale di cellule tumorali, l’eventuale presenza di necrosi e se il materiale presente nel blocchetto di paraffina possa essere sufficiente all’esecuzione dei test molecolari. La percentuale di cellule neoplastiche e un’informazione fondamentale in quanto deve essere conforme alla sensibilità della tecnica utilizzata (vedere “Fase analitica” )

DISSEZIONE DELL’AREA NEOPLASTICA (MACRO E MICRO)
Prima dell’estrazione del DNA, l’anatomopatologo deve valutare le caratteristiche del tessuto in esame ai fini di una eventuale macrodissezione e, nel caso questa si rendesse necessaria, selezionare le aree del campione più ricche di cellule tumorali. La macrodissezione viene eseguita su sezioni di tessuto paraffinato dello spessore di 10 micron montate su vetrino portaoggetto. La raccolta delle sezioni su vetrino si effettua in acqua distillata priva di gelatina in recipienti monouso (capsula Petri, becker) per evitare inquinamenti. Quindi le sezioni vengono sottoposte a macrodissezione manuale. Il tessuto dissezionato viene raccolto in un tubo Eppendorf, e sottoposto all’estrazione del DNA.

ESTRAZIONE DEL DNA/RNA
Il metodo di estrazione deve essere molto affidabile e deve generare quanto piu DNA o RNA possibile dal campione in esame. Per l’estrazione e la purificazione del DNA ed RNA da tessuto paraffinato sono oggi disponibili vari kit commerciali.

VALUTAZIONE DELLA QUALITA E QUANTITA DEL DNA/RNA
La valutazione della qualità e quantità del DNA purificato deve essere eseguita mediante:
- quantificazione dell’assorbanza a varie lunghezze d’onda per una valutazione globale del contenuto in nucleotidi della sospensione in esame nonchè della presenza di contaminati chimici;
- PCR multiplex che consente di valutare l’integrità del DNA e fornire specifiche indicazioni sull’amplificabilità del campione. La valutazione della qualità e quantità del RNA deve essere eseguita mediante quantificazione dell’assorbanza a varie lunghezze d’onda per una valutazione globale del contenuto in nucleotidi della sospensione in esame nonche della presenza di contaminati chimici; La qualita di RNA potrebbe essere valutata mediante Agilent RNA 6000 Nano kit Bioanalyzer nel caso in cui si ottenga una discreta quantita di RNA estratto. Le indagini molecolari hanno lo scopo di identificare alterazioni che forniscano una migliore definizione diagnostica, prognostica e scelta terapeutica, sulla
base della disponibilità di farmaci diretti contro specifiche varianti mutazionali o alterazioni molecolari (“actionable mutations”). Attualmente, secondo linee guida AIOM 2020, risulta raccomandata la caratterizzazione molecolare di: EGFR, ALK, ROS1, BRAF
La caratterizzazione molecolare andrebbe eseguita sui casi avanzati di carcinoma del polmone e, in virtù dei nuovi trials clinici (PACIFIC, ADAURA, ALCHEMIST), limitatamente a EGFR e ALK/ROS1, anche nelle forme precoci. Nuovi promettenti biomarkers per i quali sono stati recentemente sviluppati dei trials clinici sono oggi rilevabili mediante metodiche molecolari con singoli kit o con ampi pannelli di next generation sequencing (NGS). KRAS: e un’alterazione presente in circa il 25% delle neoplasie polmonari. MET: riscontrata nell’8% degli adenocarcinomi e nel 3% degli squamocellulari,. In una parte considerevole degli adenocarcinomi si tratta di una mutazione del sito di splicing dell’esone 14 del gene MET (METex14), che conferisce sensibilità al trattamento con inibitori di MET. RET: interessa l’1-2% delle neoplasie polmonari e può coinvolgere almeno 10 diversi partner di fusione, di cui il più frequente e KIF5B. ERBB2: Riscontrato nell’1-5% delle neoplasie, con mutazione più frequente a carico dell’esone 20 (inserzione), conferisce sensibilità ai regimi chemioterapici e puo altresi essere un meccanismo di resistenza agli inibitori di EGFR. NTRK1-3 Neurotrophic receptor tyrosine kinase 1-3: la ricerca di NTRK andrebbe effettuata in immunoistochimica come test di screening e nel caso di positività, confermata con metodica molecolare al pari di ROS1. Altre alterazioni di potenziale interesse clinico possono essere riscontrate soprattutto nell’ambito di ampi pannelli di NGS.
La scelta del metodo analitico dipende da differenti fattori:
- analisi mirata od estesa: nella diagnostica di routine vengono utilizzati metodi che consentano di focalizzarsi su determinati esoni o loci sede di mutazioni rilevanti per la sensibilità o la resistenza alle terapie. Tuttavia sono disponibili metodologie che analizzano tutti gli esoni, sebbene allo stato attuale prive di rilievo clinico;
- saggi predeterminati o indeterminati: i saggi predeterminati riconoscono a priori solo le mutazioni più frequenti (come ad esempio i kit basati su real time PCR). I metodi di sequenziamento indeterminato (sequenziamento diretto o sequenziamento NGS) sono in grado di identificare tutte le possibili
varianti, anche le più rare. L’ impiego di pannelli NGS consente l’analisi simultanea di un più o meno elevato numero di geni. Come indicato dall’ESMO (gruppo di lavoro di medicina di precisione, si raccomanda impiego di pannelli NGS con un numero limitato di geni per la diagnostica di routine riservando l’impiego di pannelli più ampi in centri con elevato volume di esami molecolari e ad elevata. Tale metodica eviterebbe di procedere con analisi sequenziali con conseguente risparmio di materiale, tempi di refertazione e costi complessivi. Sensibilità: La sensibilità dei metodi - espressa come percentuale di allele mutato nel campione - e crescente a partire dal sequenziamento diretto (20-30%), pirosequenziamento, spettrometria di massa, e sequenziamento NGS (tutti circa 5%) fino all’1% della real time PCR. La scelta dipende dall’arricchimento in
cellule neoplastiche del campione. Poichè i test più sensibili sono anche i più costosi sarebbe auspicabile avere a disposizione in ogni laboratorio un metodo sensibile per i campioni poco arricchiti (biopsie, citologia) e uno meno sensibile per quelli più arricchiti (pezzi chirurgici). Sul DNA estratto da tessuti o campioni citologici, non è consigliabile utilizzare metodi con sensibilità inferiore all’1%. L’esame delle biopsie liquide, recentemente introdotte in diagnostica, richiede strumentazioni dedicate molto piu sensibili (si rimanda ad un documento specifico in preparazione). Le diverse metodologie molecolari in uso sono: Sequenziamento Sanger, Real Time PCR e Real Time RT-PCR, NGS (DNA e RNA). Le metodologie verranno scelte sulla base della quantità e qualità degli acidi nucleici estratti, secondo indicazioni della scheda tecnica e ottimizzazione nel laboratorio. Tempo di esecuzione (Turnaround time, TAT): Per motivi clinici non e accettabile che un singolo test diagnostico predittivo per la risposta a un farmaco oncologico venga refertato in >10 giorni lavorativi, l’obiettivo dovrebbe essere l’erogazione entro 5 giorni. La maggior parte dei kit commerciali e anche dei
metodi sviluppati internamente nei laboratori consente tempi di refertazione <5 giorni lavorativi per singoli test. Tempi più lunghi sono ammissibili solo in caso di validazioni di risultati equivoci o per l’esecuzione di pannelli mutazionali NGS.
3) Stesura di un referto
La refertazione, parte integrante della procedura diagnostica, e il risultato di un processo multifasico che converte il risultato di un’analisi strumentale in un’informazione di utilità clinica, ovvero necessaria per un’adeguata impostazione terapeutica.
Il referto deve essere compilato su un modello prestabilito, firmato dall’anatomo-patologo e dall’esecutore del test molecolare e preferibilmente strutturato in tre campi principali: Identificazione del paziente, notizie anamnestiche, metodica utilizzata e Risultato del test molecolare.

IDENTIFICAZIONE DEL PAZIENTE E NOTIZIE ANAMNESTICHE
Devono essere presenti i dati anagrafici del paziente, il nome del medico e/o struttura che ha richiesto l’analisi, la tipologia del materiale utilizzato (es. inclusione in paraffina, sezione di tessuto…), con riferimento alla diagnosi istologica.

RISULTATO DEL TEST MOLECOLARE
Le informazioni da riportare nel referto sono:
- I risultati del test espressi in termini di assenza o presenza di mutazione, in caso di presenza va specificata la tipologia (qualora la metodica utilizzata lo consenta), in quanto può essere sensibilizzante o conferire resistenza ad una determinata terapia;
- In caso di campione non idoneo per l’analisi riportare il motivo dell’inadeguatezza;
- La percentuale di cellule neoplastiche relativa all’area del campione biologico selezionata per l’analisi;
- La metodica, il test commerciale e la versione del kit impiegati per l’esecuzione dell’analisi e la sensibilità analitica del metodo;
gli esoni sottoposti ad analisi e la sequenza genomica di riferimento; nel caso l’analisi sia stata eseguita con kit che analizzano geni multipli con qualsivoglia metodica, e necessario che il paziente sia adeguatamente informato e firmi il proprio consenso all’analisi di geni che non siano stati espressamente richiesti dal clinico; La partecipazione del centro ad appropriati controlli di qualità esterni, quali quelli nazionali promossi da AIOM-SIAPEC/IAP oppure europei (EMQN, EQA, ecc…).


ALLEGATO 4
GESTIONE ANATOMO-PATOLOGICA DEL CAMPIONE CHIRURGICO
Premessa: Il presente documento e riferito alla diagnosi anatomo-patologica delle neoplasie primitive epiteliali maligne del polmone (non verranno citati i markers immunoistochimici dei tumori neuroendocrini e mesenchimali, per i quali si fa riferimento ai PDTA dei tumori neuroendocrini e dei tessuti molli, rispettivamente). Nella diagnosi anatomo-patologica vengono riportate informazioni riguardanti le caratteristiche morfologiche (macroscopiche e microscopiche), biologiche e genetiche della neoplasia, tutte utili per le scelte terapeutiche, la corretta stratificazione prognostica ed il monitoraggio delle terapie. La diagnosi anatomo-patologica rappresenta uno step fondamentale anche per qualsiasi progetto di ricerca clinica. In questo allegato saranno riportati 2 aspetti fondamentali della diagnosi anatomo-patologica 1) diagnosi macroscopica; 2) diagnosi istologica/immunoistochimica. L’analisi molecolare e riportata nell’allegato 4.
1. Reperti macroscopici
1.1 - Invio del campione operatorio chirurgico
L’invio del campione chirurgico al laboratorio di Anatomia Patologica deve essere tempestivo. L’invio può avvenire: a) in assenza di liquido fissativo (sotto vuoto e a bassa temperatura entro 12 ore; a fresco entro 3 ore); b) immerso in soluzione al 10% di formalina tamponata. I brevi tempi di ischemia preservano le caratteristiche morfologiche e molecolari della neoplasia. Essi andrebbero riportati nelle notizie cliniche di accompagnamento al campione. In caso di punti di repere di particolare interesse questi vanno indicati seguendo protocolli di marcatura precedentemente condivisi tra gli specialisti della sede. Il campione chirurgico e accompagnato da richiesta esame istologico (digitale o cartacea). La richiesta deve includere: a) dati anagrafici; b) informazioni cliniche di interesse oncologico (familiarità, terapie neoadiuvanti, metastasi a distanza); c) identificazione di ciascuno dei Campioni inviati; d) sede anatomica della neoplasia; e) procedura chirurgica attuata (vedi elencazione sotto riportata).
- Segmentectomia
- Sleeve lobectomy
- Pneumectomia
- Lobectomia
1.2 - Esame macroscopico e campionamento del pezzo operatorio chirurgico.
L’esame macroscopico (diagnosi macroscopica) e parte essenziale della diagnosi. In esso sono riportate le caratteristiche della neoplasia, la valutazione del parenchima polmonare non-neoplastico, la valutazione dei linfonodi presenti e quello della pleura viscerale.
E’ consigliata fissazione in formalina tamponata per almeno 24 ore.
Sono riportate nella sezione macroscopica della diagnosi anatomo-patologica:
La tipologia di campione in esame (es: lobo polmonare, segmento, polmone);
La presenza di eventuali altre strutture anatomiche rimosse adese;
Misurazione e peso del campione;
Descrizione e misurazione delle lesioni macroscopicamente visibili;
Descrizione della invasione o meno della pleura o parete bronchiale (bronco maggiore o segmentario);
Descrizione della distanza dalla superfice pleurica e/o dal bronco principale;
La presenza di atelettasia e/o di processi broncopneumonici.
Se presenti noduli separati dal tumore questi vanno descritti, misurati e campionati. Il campionamento consentirà un adeguato studio morfologico/molecolare per definire il nodulo come tumore primitivo sincrono o metastasi intrapolmonare. Studi di profilo molecolare potrebbero in futuro essere di aiuto per una più precisa distinzione. 
1.3 – Campionamento del pezzo operatorio
Vengono effettuati: a) almeno 3 campionamenti della neoplasia (se maggiore di 3 cm si effettuano prelievi aggiuntivi pari ad 1/cm) comprendente area  centrale; area di transizione tra neoplasia e area non neoplastica (utile per la valutazione di l’eventuale disseminazione tumorale intraalveolare “STAS-spread through air spaces” in caso di adenocarcinoma) ed area comprensiva di pleura viscerale b) area non neoplastica c) margine di resezione bronchiale e vascolare (questi possono pervenire come prelievi separati già dalla chirurgia) d) margine pleurico per neoplasia periferica e) linfonodi peribronchiali. I campionamenti delle aree non neoplastiche dovrebbero comprendere un’area intraparenchimale ed una più periferica con superficie pleurica. 2. Diagnosi istologica Deve riportare: a) caratteristiche morfologiche della neoplasia; b) stato dei margini di resezione; status dei linfonodi regionali; d) presenza di invasione della pleura; e) la presenza/assenza di invasione vascolare; f) invasioni di altre strutture adiacenti rimosse contestualmente (es. pericardio, coste); g) la risposta ai trattamenti neoadiuvanti; h) la presenza/ assenza di carcinoma in situ;
i) presenza di patologie associate.
2.1 Istotipo e grading del tumore polmonare (Tabelle 1-3)
Se si tratta di un adenocarcinoma e necessario specificare la presenza del pattern prevalente riportando la percentuale (> o < 20%) del pattern a prognosi
peggiore come indicato nella WHO 2021 Per le neoplasie con istotipo squamocellulare e importante riferire il grado di differenziazione (cheratinizzante, non cheratinizzante, basaloide).
2.2 I margini di resezione ed i linfonodi: i prelievi vanno campionati ed inclusi in toto e sono sempre riportati nel report diagnostico riferendo le rispettive specifiche di provenienza.
2.3 Invasione della pleura
L’invasione della pleura viscerale va sempre indicata e graduata come PL0: assente, PL1: invasione delle fibre elastiche; PL2: invasione a tutto spessore fino alla sierosa pleurica e PL3: invasione della pleura parietale (Figura 3). Il riferimento dell’invasione pleurica e di estrema importanza poichè comporta una variazione dello staging (per lo stadio patologico: Detterbeck FC, Boffa DJ, Kim AW, Tanoue LT. The Eighth Edition Lung Cancer Stage Classification. Chest. 2017 Jan;151(1):193-203.). Per una migliore visualizzazione delle fibre elastiche della parete pleurica e utile l’utilizzo di colorazioni speciali come fibre elastiche Van Gieson.
2.4) Presenza/assenza di invasione vascolare
Sebbene la presenza di invasione vascolare e linfatica non modifica lo stadio tumorale, alcuni studi hanno dimostrato un’influenza prognostica negativa che può talora influenzare il follow-up e trattamento clinico
2.5) STAS (Spread through airspaces)
La STAS tumorale e definita come le cellule tumorali all'interno degli spazi aerei nel parenchima polmonare a distanza. Questo dovrebbe essere distinto dalla diffusione artefattuale di cellule tumorali, da effetti del taglio, da pneumociti reattivi e cellule bronchiali. La STAS nell'adenocarcinoma e composto da tre pattern morfologici: strutture micropapillari, nidi solidi di cellule tumorali che riempiono gli spazi aerei e cellule singole discoese. Numerosi studi indipendenti hanno dimostrato che la STAS e un fattore prognostico negativo. Nei pazienti con STAS, infatti, il rischio di recidiva e significativamente più alto.
2.6) Risposta alla terapia neoadiuvante: rappresenta un punto importante da indicare nel referto istologico, soprattutto in vista delle nuove acquisizioni e delle proposte di trattamento anche per stadi precoci che renderanno sempre più frequenti questo tipo di neoplasie su pezzo operatorio. La valutazione
della regressione tumorale e del letto tumorale, formulata su tumore primitivo e linfonodi, tiene conto della percentuale di cellule tumorali residue, della percentuale di necrosi e dello stroma (incluso infiltrato infiammatorio e fibrosi), secondo le raccomandazioni dell’IASLC
Per la refertazione, vedere Tabella 3.
TABELLA 1: CARATTERIZZAZIONE FENOTIPICA DELL’ ADENOCARCINOMA
Variabile Caratteristiche della neoplasia Legenda
Grading architetturale
Ben differenziato (lepidico con <20 per cento di pattern ad alto grado)
Moderatamente differenziato (acinare/papillare con <20 per cento di pattern ad alto grado)
Scarsamente differenziato (>20 percento di pattern ad alto grado)
Mucinoso Assente;Presente
Diffusione intralveolare (STAS) Assente (-); Presente (+, limitata, estensiva)
Invasione neoplastica vascolare Positivo (+); Assente (-)
Invasione pleura PL0: assente; PL1: prime fibre elastiche; PL2: invasione a tutto
spessore; PL3: invasione della parietale
TTF1 Positivo (+); Assente (-)
MIB1 %
P40 Positivo (+); Assente (-)
TABELLA 2: CARATTERIZZAZIONE FENOTIPICA DEL CARCINOMA SQUAMOCELLULARE
Variabile Caratteristiche della neoplasia Legenda
Istotipo Cheratinizzante, Non cheratinizzante, Basaloide
Necrosi neoplastica <10%; 11per cento - 30%; >30%
Numero di mitosi 0-1/10 HPF; 2-4/10 HPF; >5/10 HPF
Invasione pleura PL0: assente; PL1: prime fibre elastiche; PL2: invasione a tutto spessore; PL3:
invasione della parietale
TTF1 Positivo (+); Assente (-)
P40 Positivo (+); Assente (-)
TABELLA 3: VALUTAZIONE DELLA RISPOSTA PATOLOGICA AL TRATTAMENTO NEOADIUVANTE
Valutazione della risposta patologica al trattamento neoadiuvante
Tipo di trattamento neoadiuvante effettuato
Effetto del trattamento sulla neoplasia
Percentuale di tumore vitale: %.
Percentuale di necrosi: %.
Percentuale di stroma (fibrosi ed infiammazione): %.
Grado dell'infiammazione
Basso/Moderato/elevato.
Metodo per la valutazione del tumor bed
La valutazione e stata effettuata su tre sezioni istologiche, corrispondenti ai prelievi in toto del nodulo.
Effetti del trattamento sulle metastasi linfonodali
N stazioni esaminate
N linfonodi esaminati
N linfonodi metastatici
Linfonodi con alterazioni da trattamento
Diametro maggiore del focolaio neoplastico
Stazione metastatica
Estensione extracapsulare
"""
