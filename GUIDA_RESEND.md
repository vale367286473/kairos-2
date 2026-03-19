# Guida Setup Resend.com — Kairos Outreach

Resend è il servizio di invio email via API che usiamo al posto di Register.it SMTP.
Piano gratuito: **3.000 email/mese** — più che sufficienti per i 140 contatti.

---

## Passo 1 — Crea l'account Resend

1. Vai su **[resend.com](https://resend.com)** e clicca **Sign Up**
2. Registrati con la tua email (es. `valeriorossi884@gmail.com`)
3. Conferma l'email e accedi alla dashboard

---

## Passo 2 — Verifica il dominio kairos-24.it

Questo serve per inviare email con mittente `business@kairos-24.it`.

1. Nella dashboard Resend, clicca **Domains** nel menu a sinistra
2. Clicca **Add Domain**
3. Inserisci: `kairos-24.it`
4. Resend ti mostrerà **3 record DNS** da aggiungere (tipo TXT e MX)

### Aggiungi i record DNS su Register.it

5. Vai su **[register.it](https://www.register.it)** → accedi al pannello
6. Vai su **Domini** → `kairos-24.it` → **Gestione DNS** (o "Zone DNS")
7. Aggiungi uno per uno i 3 record che Resend ti ha dato:

   | Tipo | Nome / Host | Valore |
   |------|-------------|--------|
   | TXT  | `resend._domainkey` | `p=MIGf...` (chiave lunga) |
   | TXT  | `@` oppure il dominio stesso | `v=spf1 include:amazonses.com ~all` |
   | MX   | `bounce` | `feedback-smtp.us-east-1.amazonses.com` |

   *(i valori esatti te li dà Resend — usa quelli, non questi)*

8. Salva e torna su Resend → clicca **Verify DNS Records**
9. ⏳ Possono volerci da 5 minuti a 24 ore. Di solito meno di 30 minuti.
10. Quando vedi ✅ verde accanto al dominio, sei pronto.

---

## Passo 3 — Crea la chiave API

1. In Resend, clicca **API Keys** nel menu a sinistra
2. Clicca **Create API Key**
3. Dai un nome (es. "Kairos Outreach")
4. Permessi: seleziona **Sending access**
5. Clicca **Add** — ti mostra la chiave **una sola volta**, copiala subito!

   La chiave ha questo formato: `re_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## Passo 4 — Aggiorna credenziali_mail.txt

Apri il file `credenziali_mail.txt` nella cartella del progetto e incolla la chiave:

```
EMAIL=business@kairos-24.it
NOME_MITTENTE=Raul Colombo — Kairos
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ← qui la tua chiave
```

Salva il file.

---

## Passo 5 — Installa il pacchetto Python

Apri **PowerShell** e lancia:

```powershell
pip install resend pandas openpyxl
```

*(se già hai pandas e openpyxl installati, basta `pip install resend`)*

---

## Passo 6 — Test di invio

Dalla cartella del progetto (`outreach_milano`), lancia:

```powershell
python invia_email_resend.py --test
```

Questo invia **una sola email a te stesso** (`business@kairos-24.it`).
Controlla la casella — se arriva, sei pronto per l'invio reale.

---

## Passo 7 — Invio reale

```powershell
python invia_email_resend.py
```

Lo script:
- Legge i contatti dall'Excel (foglio "📊 Contatti Prioritizzati")
- Invia fino a 100 email per sessione, partendo dai punteggi più alti
- Aspetta 35-65 secondi tra un'email e l'altra (evita i filtri antispam)
- Salva tutto nel log `log_email_inviate.csv` (non manda due volte la stessa email)

### Comandi utili

| Comando | Cosa fa |
|---------|---------|
| `python invia_email_resend.py` | Invia fino a 100 email |
| `python invia_email_resend.py --test` | Invia 1 email di test a te stesso |
| `python invia_email_resend.py --stato` | Mostra quante email hai già inviato |

---

## Monitoraggio

Nella dashboard Resend puoi vedere in tempo reale:
- **Emails** → ogni email inviata, con stato (consegnata, aperta, errore)
- **Logs** → log completo con timestamp

---

## Risoluzione problemi

| Problema | Soluzione |
|----------|-----------|
| `RESEND_API_KEY mancante` | Controlla che la chiave sia nel file `credenziali_mail.txt` senza spazi |
| `Domain not verified` | Il dominio su Resend non è ancora verificato — aspetta o ricontrolla i DNS |
| `ModuleNotFoundError: resend` | Esegui `pip install resend` in PowerShell |
| Il test arriva nello spam | Normale all'inizio — verifica che il dominio sia correttamente verificato su Resend |

---

*Guida generata per il progetto Kairòs Automation — Milano, marzo 2026*
