# PDTA Assistant - Supporto all'Interpretazione dei PDTA

Un assistente conversazionale progettato per aiutare i professionisti sanitari nell'interpretazione dei Percorsi Diagnostico Terapeutici Assistenziali (PDTA) per le lesioni polmonari.

## Funzionalità

- 🏥 Assistenza nell'interpretazione dei PDTA per lesioni polmonari
- 💬 Interfaccia di chat interattiva
- 📝 Gestione della cronologia delle conversazioni
- 🔄 Sessioni di chat persistenti
- ⚡ Risposte in tempo reale

## Prerequisiti

- OpenAI API key

## Installazione

1. Clona il repository:
```bash
git clone https://gitlab.com/laifereply/pdta-agent.git
cd pdta-agent
```

2. Crea e attiva un ambiente virtuale:
```bash
python -m venv .venv
source .venv/bin/activate  # Su Windows, usa: .venv\Scripts\activate
```

3. Installa i pacchetti richiesti:
```bash
pip install -r requirements.txt
```

4. Copia il file `.env.example` in `.env` e aggiungi la tua OpenAI API key:
```bash
cp .env.example .env
```

Modifica il file `.env` con la tua OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Utilizzo

1. Avvia l'applicazione Streamlit:
```bash
streamlit run main.py
```

2. Apri il browser web e naviga all'URL mostrato nel terminale (tipicamente http://localhost:8501)

3. Inizia una conversazione con l'assistente fornendo:
   - Sintomatologia del paziente
   - Fattori di rischio
   - Indagini diagnostiche effettuate
   - Risultati delle indagini

4. L'assistente ti aiuterà a interpretare il PDTA in base al contesto clinico fornito

## Struttura del Progetto

```
pdta-agent/
├── agent/
│   ├── __init__.py
│   └── agent.py          # OpenAI agent configuration and logic
├── main.py               # Main Streamlit application
├── requirements.txt      # Project dependencies
├── .env.example         # Example environment variables
├── .env                 # Environment variables (not tracked in git)
└── README.md            # This file
```

## Configurazione

Puoi personalizzare il comportamento dell'assistente modificando il file `agent/agent.py` e il file `agent/prompts/agent_instructions.py`

## Modalità di Risposta

L'assistente supporta due modalità di risposta:

### Modalità Streaming (Predefinita)
- Le risposte appaiono in tempo reale mentre vengono generate
- Esperienza più interattiva e coinvolgente
- Indicata da un cursore lampeggiante (▌) durante la generazione

### Modalità Non-Streaming
- Le risposte appaiono tutte insieme una volta completate
- Mostra "Thinking..." durante la generazione
- Utile quando si preferiscono risposte complete

È possibile passare tra le modalità in qualsiasi momento utilizzando il toggle "Use Streaming Response" nella barra laterale.