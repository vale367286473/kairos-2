# CONTESTO PROGETTO — Kairòs Automation
**Documento di handoff per AI. Ultima revisione: marzo 2026.**

---

## 1. CHI È VALERIO E COSA FA

**Nome:** Valerio Rossi
**Email:** valeriorossi884@gmail.com
**Città:** Milano

Valerio è il fondatore di **Kairòs Automation**, una startup italiana che vende ecosistemi di automazione AI alle piccole e medie imprese (PMI). All'inizio del progetto si era presentato come "consulente web freelance" (siti a €50, menù web a €30, pacchetto a €70), ma in realtà il web design è solo uno dei servizi che rientra nell'offerta più ampia di Kairòs.

---

## 2. KAIRÒS — COS'È E COSA FA

**Sito:** kairos-24.com
**Ragione sociale:** Kairòs Automation
**Tagline:** "Automazione per l'Italia che lavora"
**Anno:** 2026

### Missione e filosofia

Kairòs nasce per colmare il gap tra le grandi aziende (che hanno 12+ dipendenti dedicati: receptionist, marketing manager, data analyst, IT, social media…) e i titolari di PMI che devono fare tutto da soli. La promessa è: "rendere l'AI accessibile a chi non può permettersi i team delle multinazionali della Silicon Valley."

Il prodotto non è un singolo software. È un **"Ecosistema di Automazione Premium"** configurato su misura per ogni cliente. L'approccio è consulenziale: Kairòs entra nell'attività, analizza i processi, e costruisce il sistema.

**Differenziatore chiave vs. portali come TheFork, Fresha, OpenTable:**
- Zero commissioni per prenotazione/coperto
- Il database clienti appartiene al titolare, non a Kairòs
- Le regole (prezzi, orari, acconti, sconti) le decide il titolare

---

## 3. I SEI MODULI DELL'ECOSISTEMA

Presentati sul sito come accordion interattiva (homepage index.html):

### 3.1 Risposta Automatica AI *(Servizio Principale)*
Un centralinista virtuale che risponde al telefono H24/7. Legge l'agenda in tempo reale, prenota/modifica/cancella appuntamenti. Può clonare la voce del titolare. Reindirizza al titolare quando serve il tocco umano. Tecnologia: **ElevenLabs** (widget ConvAI embedded, agent_id diverso per verticale).

### 3.2 Lista d'Attesa Intelligente *(Automazione)*
Se uno slot è pieno, il cliente viene auto-inserito in lista. Quando si libera un posto, il sistema avvisa chi è in coda e riempie il buco. Agenda sempre piena, zero sforzo manuale.

### 3.3 Recupero Clienti Dinamico *(Marketing)*
Il sistema rileva quando un cliente abituale sparisce (es. non viene da 40 giorni). Invia automaticamente un messaggio personalizzato per riportarlo, con eventuale sconto su misura. "Clienti che avresti perso, tornano automaticamente."

### 3.4 L'Orchestratore della Tua Azienda *(Integrazione)*
Fa dialogare tra loro i software che il cliente già usa. Flussi multi-agente AI, elimina copia-incolla e operazioni ripetitive. Si integra con **oltre 1.300 app** (Google Workspace, Microsoft 365, HubSpot, Stripe, WhatsApp, ElevenLabs, OpenAI, Telegram, ecc.).

### 3.5 Web & Menù Digitali *(Presenza Digitale)*
Siti web ad alta conversione integrati con la segreteria virtuale. Menù digitali con QR code, eleganti, studiati per aumentare lo scontrino medio. Per i ristoranti: aggiornabili in un click, con foto, opzionalmente con ordinazione/pagamento al tavolo. Definiti internamente come "motore e carrozzeria, tutto curato".

### 3.6 Analista AI su Telegram *(Business Intelligence)*
Report giornalieri/settimanali via bot Telegram: numeri reali, suggerimenti, allarmi. Il titolare può gestire appuntamenti direttamente in chat ("come mandare un messaggio a un amico"). Storico annuale completo del business. Niente più Excel o calendari manuali.

---

## 4. I TRE VERTICALI DI MERCATO

Il sito ha una pagina dedicata a ciascun target, con hook narrativo specifico.

### 4.1 Ristorazione & Food (`ristorazione.html`)
**Hook:** "Il telefono squilla proprio mentre la sala è piena. Rispondi o servi i clienti al tavolo?"
**Pain points:** chiamate perse durante il servizio, prenotazioni manuali, nessun database clienti proprietario, commissioni TheFork/OpenTable
**Soluzioni verticali:**
- Sito web + menù digitale QR (foto, aggiornabile in 1 click, ordinazione/pagamento al tavolo opzionale)
- AI telefonica che gestisce prenotazioni e costruisce database proprietario (nome+telefono di ogni prenotazione)
- Gestione reputazione Google Maps: post-cena il sistema contatta il cliente → soddisfatto = nudge a recensione 5 stelle; insoddisfatto = intercetto privato
**Report Telegram:** coperti, incasso, nuove recensioni, nuovi contatti, campagne re-engagement
**Differenziatore dichiarato:** "Zero commissioni. Paghi il servizio, non il coperto."
**ElevenLabs agent_id:** `agent_3601kj1aw79ee91a9pyht3zge875`
**Colore accent:** oro (#D4A574)

### 4.2 Centro Estetico & Parrucchiere (`centro-estetico.html`)
**Hook:** "Quante volte hai dovuto smettere di lavorare su una cliente per rispondere al telefono?"
**Prezzo comunicato:** "meno di un gelato al giorno"
**Pain points:** telefono che squilla mentre si lavora, buchi in agenda, clienti abituali che spariscono senza motivo, nessun dato su performance staff
**Soluzioni verticali:**
- Agente vocale H24: gestisce agenda mentre sei in cabina/al lavaggio, reindirizza in caso di emergenza
- Recupero clienti: cliente non viene da 40 giorni → messaggio personalizzato automatico
- Business intelligence Telegram: scontrino medio (es. 32€), performance staff per operatore (es. 85% vs 70%), allarme appuntamenti sovrapposti
**Report Telegram esempio:** 75 appuntamenti/settimana, scontrino medio 32€, promo lampo consigliata per operatore meno pieno
**Value prop:** database proprietario, regole tue, integrazione gestionale esistente, sito web su misura se serve
**Confronto costo:** segretaria full-time 25.000€/anno vs Kairòs H24/7 a pochi euro/giorno
**ElevenLabs agent_id:** embedded nella pagina (widget presente)
**Colore accent:** oro (#D4A574)

### 4.3 Studio Medico & Dentistico (`studio-medico.html`)
**Hook:** "Il paziente non si è presentato e tu hai perso un'ora di lavoro. Quanto ti costa una poltrona vuota?"
**Confronto costo esplicito:** segretaria full-time CCNL ~25.000€/anno vs Kairòs **2,80€/giorno** (oltre 25x meno)
**Pain points:** urgenze serali senza risposta, 3 no-show a settimana, receptionist 3 ore/giorno al telefono per conferme, nessun sistema di recall automatico per igiene semestrale
**Soluzioni verticali:**
- Segreteria H24 notturna e festiva: filtra urgenze vere (chiama il medico) da richieste semplici (gestisce da sola)
- Gestione no-show: reminder WhatsApp automatici + opzione pagamento anticipato visita
- Analista clinico Telegram: % occupazione poltrona, trend igiene vs cure, campagna recall automatica (es. 50 messaggi → 12 prenotati)
**Value prop:** integrazione gestionale medico esistente, rispetto privacy pazienti (GDPR), libera lo staff per l'accoglienza
**CTA:** "Riduci i costi fissi. Libera il tuo tempo clinico."
**ElevenLabs agent_id:** `agent_4401kj1cc06rfgbv69vtmb6v4n20`
**Colore accent:** teal (#4ECDC4)

---

## 5. MODELLO COMMERCIALE

- **Nessun prezzo pubblico sul sito** — strategia di lead qualification sulla call
- **Unica cifra mostrata:** 2,80€/giorno per il medicale ("meno di un gelato al giorno" per gli altri verticali)
- **Modello:** verosimilmente abbonamento mensile/annuale (servizio gestito, non self-service)
- **Acquisizione clienti:** form "Prenota la tua Call Gratuita" sul sito (backend: web3forms, access_key: af9752a7-6d1a-4d54-ba5c-af0791875577)
- **Campi form:** Nome e Cognome, Nome dell'Attività, Email o Telefono + consenso privacy

---

## 6. STATISTICHE USATE NEL PITCH (homepage)

Dati citati sul sito con fonte:
- **85%** dei chiamanti che non ricevono risposta non richiama; va da un concorrente. (Fonte: KPMG)
- **51%** dei consumatori è già aperto all'IA conversazionale; **73%** cerca attivamente tecnologie che semplifichino le decisioni. (Fonte: Accenture)
- **60-70%** delle attività di una receptionist sono automatizzabili. (Fonte: British Telecom)

---

## 7. STACK TECNICO DEL SITO (kairos-24.com)

- HTML/CSS/JS puro (no framework server-side)
- TailwindCSS via CDN
- GSAP + ScrollTrigger (animazioni scroll)
- Vanilla Tilt (effetto 3D sulle card)
- Inter font (Google Fonts)
- ElevenLabs ConvAI widget (agente vocale interattivo sul sito)
- Web3Forms (form submissions)
- Iubenda (cookie banner + privacy policy)
- Hosting: presumibilmente Cloudflare/Netlify/Vercel (CNAME in repo)

---

## 8. IL PROGETTO DI OUTREACH — DATABASE CONTATTI MILANO

### Contesto
In parallelo al sito, Valerio ha costruito un database di potenziali clienti a Milano per fare outreach via email. Il progetto è gestito con Python in una cartella chiamata `outreach_milano` sul desktop.

### Architettura del sistema (file Python)
Il sistema è multi-file:
- **`priority_filter.py`** — script principale: carica i contatti, applica filtri, calcola score, genera Excel
- **`priority_filter_part1.py` / `_part2.py` / `_part3.py` / `_part4.py`** — segmenti dati (contatti 1-95 nel file principale + resto in 4 parti)
- **`cerca_email_da_siti.py`** — script standalone per trovare email dai siti web (gira sul PC di Valerio, non in sandbox)
- **`apply_emails.py`** — applica le email trovate ai file sorgente

### Pipeline di filtraggio (in ordine di applicazione)
1. `is_michelin()` — esclude ristoranti stellati (target sbagliato per Kairòs)
2. `is_chain()` — esclude catene (McDonald's, Zara, ecc.)
3. `is_luxury_hotel()` — esclude hotel di lusso con concierge dedicato
4. `is_clinic()` — esclude cliniche grandi/ospedaliere
5. `is_ghost_kitchen()` — esclude ghost kitchen (no front-of-house)
6. `geo_ok()` — solo zona centrale Milano (dentro la circonvallazione + zone premium adiacenti)

### Sistema di scoring (max 100 punti)
| Criterio | Punti |
|---|---|
| Ha email trovata | +30 |
| Nessun sito web (o sito datato) | +25 |
| Attività indipendente | +20 |
| Zona premium (Brera, Navigli, Porta Romana…) | +15 |
| Categoria target primaria | +10 |

### Tier di priorità
- **P1** ≥ 75 punti → outreach immediato
- **P2** ≥ 55 punti → outreach prioritario
- **P3** ≥ 35 punti → outreach secondario
- **Bassa** < 35 punti → bassa priorità

### Risultati ultima run
- **Totale contatti:** 314 tenuti, 141 esclusi
- **P1:** 98 contatti (tutti con email)
- **P2:** 175 contatti (26 con email)
- **P3:** 34 contatti
- **Bassa:** 7 contatti
- **Outreach-ready (P1+P2 con email):** 124 contatti

### Categorie target nel database
Ristoranti, pizzerie, bar, trattorie, osterie, enoteche, cocktail bar, centri estetici, parrucchieri, barbieri, nail bar, centri benessere, escape room, centri fitness/yoga (alcune), studi medici (potenziale espansione futura).

### Zone geografiche coperte
Centro storico Milano (dentro le Mura Spagnole), Brera, Navigli, Porta Romana, Porta Venezia, Isola, Tortona, Moscova, Magenta, CityLife, Garibaldi. Sono **escluse** zone periferiche (Bicocca, Sesto, Cinisello, ecc.) salvo eccezioni con altissimo score.

### File di output
- `contatti_prioritizzati.xlsx` — Excel principale con color-coding per priorità (verde P1, giallo P2, arancione P3, rosso Bassa), colonne: Nome, Indirizzo, CAP, Categoria, Email, Score, Priorità, Note
- `top_targets_outreach.txt` — lista dei 124 contatti P1+P2 con email, pronta per outreach

---

## 9. VERTICALIZZAZIONE DELL'OUTREACH

Per i **ristoranti/bar/pizzerie** nel database, gli angoli di attacco più forti sono:
1. Menù digitale QR + AI telefonica (combo immediata, valore tangibile)
2. Zero commissioni vs TheFork
3. Database clienti proprietario (ogni prenotazione = contatto tuo)
4. Gestione reputazione Google Maps automatica

Per i **centri estetici/parrucchieri/barbieri**:
1. Receptionist AI che risponde mentre lavori
2. Recupero automatico clienti scomparsi
3. Report Telegram con performance staff
4. "Meno di un gelato al giorno"

Per gli **studi medici/dentistici** (espansione futura database):
1. Confronto costo segretaria (25.000€/anno vs 2,80€/giorno)
2. Gestione no-show + WhatsApp reminder
3. Recall automatico pazienti per controlli periodici

---

## 10. INFORMAZIONI TECNICHE PER L'AI

- Linguaggio comunicazione con Valerio: **italiano**
- Valerio è a Milano, conosce bene le zone e i locali
- È pratico di Python (riesce a eseguire script ma non a scriverli da solo)
- Usa Windows con PowerShell
- La cartella progetto outreach è `C:\Users\valer\Desktop\outreach_milano`
- La cartella sito web è `C:\Users\valer\Desktop\kairos-repo-backup`
- Ha già configurato Python + pip sul suo PC
- Può eseguire script Python dal terminale

---

## 11. COSE DA NON DIMENTICARE

1. Il **database clienti** e il **sito kairos-24.com** sono due progetti separati ma connessi: il database serve per contattare i potenziali clienti di Kairòs.
2. Valerio ha già **124 contatti con email** pronti per l'outreach.
3. La **web design** (siti a €50, menù web a €30) è uno dei servizi offerti da Kairòs come modulo "Web & Menù Digitali" — non è un servizio standalone.
4. Il modello di business di Kairòs è B2B locale: PMI milanesi (poi espansione italiana).
5. Il sito usa un **form di prenotazione call gratuita** come principale punto di conversione — nessun acquisto online diretto.
6. Ogni verticale ha un **agente vocale ElevenLabs** diverso embedded nel sito (dimostrativo).

---

*Fine documento — generato da AI assistant, basato sull'analisi completa del sito kairos-24.com e delle sessioni di lavoro con Valerio Rossi.*
