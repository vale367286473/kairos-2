#!/usr/bin/env python3
"""
KAIROS — Script invio email outreach B2B  [versione Resend.com]
===============================================================
Legge i contatti dall'Excel, seleziona il template corretto per categoria,
personalizza nome attività e invia tramite API Resend.com

PRIMA DI USARE:
  pip install resend pandas openpyxl

USO:
  python invia_email_resend.py           → invia fino a 100 email (prima sessione)
  python invia_email_resend.py --test    → invia SOLO UNA email di test a te stesso
  python invia_email_resend.py --stato   → mostra quante email sono già state inviate
"""

import os, csv, time, base64, random, sys
import pandas as pd
import resend
from pathlib import Path
from datetime import datetime

# ─── PERCORSI ────────────────────────────────────────────────────────────────
BASE  = Path(__file__).parent
EXCEL = BASE / "contatti_prioritizzati.xlsx"
LOG   = BASE / "log_email_inviate.csv"
LOGO  = BASE / "PHOTO-2026-03-19-01-00-17.jpg"
CRED  = BASE / "credenziali_mail.txt"

# ─── CONFIGURAZIONE ───────────────────────────────────────────────────────────
MAX_PER_SESSIONE = 100   # max email per ogni volta che lanci lo script
DELAY_MIN        = 35    # secondi minimi tra un'email e l'altra
DELAY_MAX        = 65    # secondi massimi (variazione random = meno sospetto spam)
SHEET            = "📊 Contatti Prioritizzati"

# ─── LEGGI CREDENZIALI ────────────────────────────────────────────────────────
def leggi_credenziali():
    creds = {}
    with open(CRED, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()
    return creds

# ─── MAPPA CATEGORIA → TEMPLATE ──────────────────────────────────────────────
MAPPA_CATEGORIA = {
    # RISTORANTI
    "ristorante":               "ristoranti",
    "osteria":                  "ristoranti",
    "trattoria":                "ristoranti",
    "pizzeria":                 "ristoranti",
    "ristorante fusion":        "ristoranti",
    "ristorante/pizzeria":      "ristoranti",
    "pizzeria/ristorante":      "ristoranti",
    "ristorante bio":           "ristoranti",
    "ristorante giapponese":    "ristoranti",
    "sushi/giapponese":         "ristoranti",
    "ristorante cinese":        "ristoranti",
    "ristorante indonesiano":   "ristoranti",
    "ristorante indiano":       "ristoranti",
    "ristorante spagnolo":      "ristoranti",
    "ristorante napoletano":    "ristoranti",
    "ristorante greco":         "ristoranti",
    "ristorante di pesce":      "ristoranti",
    "ristorante fusion/sushi":  "ristoranti",
    "ristorante vegetariano/vegano": "ristoranti",
    "ristorante contemporaneo": "ristoranti",
    "ristorante/gastronomia":   "ristoranti",
    "ristorante/paninoteca":    "ristoranti",
    "osteria/ristorante":       "ristoranti",
    "bistrot":                  "ristoranti",
    "bistrot/ristorante":       "ristoranti",
    "steakhouse/ristorante":    "ristoranti",
    "churrascaria brasiliana":  "ristoranti",
    "trattoria milanese":       "ristoranti",
    "hamburgheria/birreria":    "ristoranti",
    "birreria artigianale":     "ristoranti",
    "birreria/pub":             "ristoranti",
    "enoteca/wine bar":         "ristoranti",
    "wine bar/enoteca":         "ristoranti",
    "bar/cocktail":             "ristoranti",
    "bar/caffetteria":          "ristoranti",
    "caffè/pasticceria":        "ristoranti",
    "pasticceria":              "ristoranti",
    "pasticceria/bar":          "ristoranti",
    "pasticceria/caffetteria":  "ristoranti",
    "gastronomia/rosticceria":  "ristoranti",
    "pizzeria bio/ristorante":  "ristoranti",
    "ristorante/intrattenimento":"ristoranti",
    # PARRUCCHIERI
    "parrucchiere":             "parrucchieri",
    "hair studio":              "parrucchieri",
    "hair salon":               "parrucchieri",
    "parrucchiere/centro estetico": "parrucchieri",
    "parrucchiere/profumeria":  "parrucchieri",
    # BARBIERI
    "barbiere":                 "barbieri",
    "barbershop":               "barbieri",
    "parrucchiere/barbiere":    "barbieri",
    # DENTISTI
    "studio dentistico":        "dentisti",
    "clinica odontoiatrica":    "dentisti",
    "studio medico":            "dentisti",
    "studio medico-dentistico": "dentisti",
    "brera studio medico":      "dentisti",
    # SPA / MASSAGGI
    "spa/centro benessere":     "spa",
    "spa":                      "spa",
    "centro benessere":         "spa",
    "centro massaggi":          "spa",
    "yoga/pilates":             "pilates",
    # ESTETICO / NAIL
    "centro estetico":          "estetico",
    "centro estetico/laser":    "estetico",
    "nail salon":               "estetico",
    "centro estetico/nail":     "estetico",
    # PILATES / FITNESS
    "studio pilates":           "pilates",
    "studio pilates/fitness":   "pilates",
    "boutique fitness":         "pilates",
    "palestra":                 "pilates",
    "arrampicata indoor":       "entertainment",
    "padel/sport":              "entertainment",
    "sport/intrattenimento":    "entertainment",
    # ENTERTAINMENT
    "escape room":              "entertainment",
    "go-kart":                  "entertainment",
    "go-kart indoor":           "entertainment",
    "go-kart outdoor":          "entertainment",
    "laser game":               "entertainment",
    "laser tag":                "entertainment",
    "laser tag/gaming":         "entertainment",
    "laser tag/team building":  "entertainment",
    "bowling":                  "entertainment",
    "paintball":                "entertainment",
    "vr gaming/intrattenimento":"entertainment",
    "vr/realtà virtuale":       "entertainment",
}

def template_per_categoria(categoria_excel):
    """Restituisce il nome del template basandosi sulla categoria dell'Excel."""
    key = str(categoria_excel).lower().strip()
    if key in MAPPA_CATEGORIA:
        return MAPPA_CATEGORIA[key]
    for parola, template in [
        ("ristorante", "ristoranti"), ("osteria", "ristoranti"),
        ("trattoria", "ristoranti"), ("pizzeria", "ristoranti"),
        ("sushi", "ristoranti"),     ("bistrot", "ristoranti"),
        ("parrucchiere", "parrucchieri"), ("hair", "parrucchieri"),
        ("barbier", "barbieri"),
        ("dentist", "dentisti"),     ("odontoiatr", "dentisti"),
        ("spa", "spa"),              ("massagg", "spa"), ("benessere", "spa"),
        ("estetico", "estetico"),    ("nail", "estetico"),
        ("pilates", "pilates"),      ("fitness", "pilates"), ("yoga", "pilates"),
        ("kart", "entertainment"),   ("laser", "entertainment"),
        ("escape", "entertainment"), ("bowling", "entertainment"),
        ("paintball", "entertainment"),
    ]:
        if parola in key:
            return template
    return "ristoranti"

# ─── TEMPLATE EMAIL ───────────────────────────────────────────────────────────
APERTURA = {
    "ristoranti":    "Buongiorno {nome},",
    "parrucchieri":  "Buongiorno {nome},",
    "barbieri":      "Buongiorno {nome},",
    "dentisti":      "Gentile Dottore/Dottoressa,",
    "spa":           "Buongiorno {nome},",
    "estetico":      "Buongiorno {nome},",
    "pilates":       "Buongiorno {nome},",
    "entertainment": "Buongiorno {nome},",
}

TRIAL = ("Per permetterLe di valutarlo senza rischi, offriamo <strong>una settimana di prova "
         "gratuita — senza impegno, senza carta di credito</strong>. È il modo più semplice per "
         "vedere i risultati prima di qualsiasi decisione.")

CORPO = {
    "ristoranti": """\
Siamo Kairos, una startup italiana che affianca ristoranti come il Suo con un sistema di automazione AI concreto: risponde alle telefonate H24 senza che nessuno in sala debba alzare un dito, gestisce e conferma le prenotazioni in autonomia, riempie i buchi in agenda con una lista d'attesa intelligente, e — il punto che interessa di più — recupera automaticamente i clienti che non si fanno più vivi da un po', con messaggi personalizzati al momento giusto.
<br><br>
Creiamo anche siti web ad alta conversione e menù digitali QR studiati per aumentare lo scontrino medio: tutto pensato perché il Suo ristorante lavori meglio, non di più.
<br><br>
{trial}
<br><br>
Può visitare <strong>kairos-24.com</strong> per una panoramica completa, oppure contattarmi direttamente al <strong>+39 348 872 5260</strong>.""",

    "parrucchieri": """\
Siamo Kairos, una startup che aiuta saloni come il Suo con un assistente AI che lavora mentre Lei è al lavoro: risponde alle chiamate e ai messaggi H24, gestisce appuntamenti e cancellazioni in autonomia, e soprattutto recupera le clienti che non si rifanno vive da qualche settimana — con un messaggio personalizzato e l'offerta giusta al momento giusto.
<br><br>
In parallelo, riempiamo automaticamente i buchi in agenda grazie a una lista d'attesa intelligente, e possiamo creare o aggiornare il sito web del Suo salone per attirare nuove clienti. Meno telefonate interrotte, agenda sempre piena, clienti più fidelizzate.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi contatti al <strong>+39 348 872 5260</strong>.""",

    "barbieri": """\
Siamo Kairos, una startup italiana che aiuta barbershop come il Suo a non perdere nemmeno una prenotazione — nemmeno la sera, nemmeno nel fine settimana. Il nostro assistente AI risponde H24, gestisce appuntamenti in autonomia, riempie i buchi con una lista d'attesa automatica, e recupera i clienti che non si rifanno vivi da qualche settimana con messaggi personalizzati.
<br><br>
Possiamo anche creare o migliorare il sito del Suo shop per convertire meglio i visitatori in prenotazioni reali. Tutto senza che Lei o il Suo staff debbano fare nulla di extra.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi scriva al <strong>+39 348 872 5260</strong>.""",

    "dentisti": """\
Siamo Kairos, una startup che collabora con studi dentistici per risolvere un problema che quasi tutti condividono: la segreteria è spesso occupata, le chiamate vanno perse, e quei pazienti prenotano altrove.
<br><br>
Il nostro centralinista AI risponde H24, prende e gestisce gli appuntamenti leggendo l'agenda in tempo reale, avvisa automaticamente i pazienti in lista d'attesa quando si libera un posto, e recupera chi non si fa vivo da qualche mese con promemoria personalizzati. Realizziamo anche il sito web dello studio, pensato per trasmettere fiducia e convertire le visite in prenotazioni.
<br><br>
Il Suo staff rimane libero di dedicarsi ai pazienti in sala, senza più interrompere le visite per rispondere al telefono.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi contatti al <strong>+39 348 872 5260</strong>.""",

    "spa": """\
Siamo Kairos, una startup che aiuta centri benessere come il Suo a trasformare i clienti occasionali in clienti abituali. Il problema che risolviamo è semplice ma concreto: un cliente prova un trattamento, è soddisfatto, ma non torna — non per scelta definitiva, ma perché nessuno l'ha ricontattato nel momento giusto.
<br><br>
Kairos lo fa in automatico: monitora chi non si fa vivo da qualche settimana e invia messaggi personalizzati con proposte mirate. In parallelo, risponde a chiamate e messaggi H24, gestisce prenotazioni senza occupare il Suo staff, e riempie i buchi con una lista d'attesa intelligente. Realizziamo anche siti web pensati per comunicare l'esperienza del Suo centro e aumentare le prenotazioni dirette.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi scriva al <strong>+39 348 872 5260</strong>.""",

    "estetico": """\
Siamo Kairos, una startup che aiuta centri estetici come il Suo a riportare le clienti che spariscono dopo uno o due trattamenti. Il sistema monitora automaticamente chi non si fa viva da qualche settimana e le invia un messaggio personalizzato al momento giusto — senza che Lei debba pensarci.
<br><br>
In parallelo, risponde a chiamate e messaggi H24, gestisce prenotazioni e lista d'attesa in autonomia, e possiamo creare il sito del Suo centro pensato per convertire le visite in appuntamenti reali. Agenda più piena, clienti più fidelizzate, zero lavoro manuale.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi contatti al <strong>+39 348 872 5260</strong>.""",

    "pilates": """\
Siamo Kairos, una startup italiana che aiuta studi come il Suo a ridurre il turnover delle allieve. Il problema è comune: dopo qualche mese si fermano — spesso non per scelta definitiva, ma perché mancava un piccolo contatto al momento giusto.
<br><br>
Kairos lo fa in automatico: capisce chi non si fa viva da un po' e le invia un messaggio personalizzato con il tono e l'offerta giusti. Risponde anche a chiamate e messaggi H24, gestisce le prenotazioni delle lezioni senza occupare il Suo staff, e possiamo realizzare un sito web che comunichi il valore del Suo studio e attiri nuove iscritte.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi scriva al <strong>+39 348 872 5260</strong>.""",

    "entertainment": """\
Siamo Kairos, una startup che aiuta centri di intrattenimento come il Suo a gestire in modo automatico prenotazioni, conferme e recupero clienti — senza aggiungere lavoro al Suo staff.
<br><br>
Il sistema risponde a chiamate e messaggi H24, invia conferme e reminder automatici per ridurre le cancellazioni last-minute, e recupera i clienti che hanno visitato il centro una volta e non sono più tornati, con messaggi personalizzati al momento giusto. Realizziamo anche siti web pensati per convertire i visitatori in prenotazioni dirette.
<br><br>
{trial}
<br><br>
Visiti <strong>kairos-24.com</strong> o mi contatti al <strong>+39 348 872 5260</strong>.""",
}

OGGETTO = {
    "ristoranti":    "I clienti che non tornano al Suo ristorante? Noi li richiamiamo — in automatico",
    "parrucchieri":  "Le clienti del Suo salone che spariscono? Kairos le ricontatta per Lei",
    "barbieri":      "Il Suo barbershop perde prenotazioni dopo le 18? Con Kairos, no",
    "dentisti":      "La Sua segreteria perde chiamate ogni giorno: ecco come fermarlo",
    "spa":           "Ogni cliente che prova il Suo centro una sola volta è un'opportunità persa",
    "estetico":      "Le Sue clienti del gel tornano da sole? Con Kairos, sì",
    "pilates":       "Le allieve che non hanno rinnovato? Kairos le ricontatta per Lei",
    "entertainment": "Prenotazioni di gruppo che saltano all'ultimo? Kairos le gestisce",
}

# ─── COSTRUISCI HTML EMAIL ────────────────────────────────────────────────────
def costruisci_html(nome_attivita, template, email_dest):
    apertura = APERTURA[template].format(nome=nome_attivita)
    corpo    = CORPO[template].format(trial=TRIAL)

    # Logo come data URI (base64) — funziona con qualsiasi client email e API
    logo_b64 = base64.b64encode(LOGO.read_bytes()).decode()
    logo_src  = f"data:image/jpeg;base64,{logo_b64}"

    html = f"""<!DOCTYPE html>
<html lang="it">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f5f5f5;padding:20px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">

  <!-- HEADER LOGO -->
  <tr><td style="background:#ffffff;padding:28px 40px 16px;text-align:center;border-bottom:3px solid #7B2FBE;">
    <img src="{logo_src}" alt="Kairos" style="width:180px;height:auto;">
  </td></tr>

  <!-- BODY -->
  <tr><td style="padding:32px 40px;color:#1A1A2E;font-size:15px;line-height:1.7;">
    <p style="margin:0 0 18px 0;">{apertura}</p>
    <p style="margin:0 0 18px 0;">{corpo}</p>
    <p style="margin:24px 0 6px 0;">Cordiali saluti,</p>
    <p style="margin:0;"><strong>Raul Colombo</strong><br>
    Co-founder, Kairos<br>
    <a href="tel:+393488725260" style="color:#7B2FBE;text-decoration:none;">+39 348 872 5260</a> &nbsp;|&nbsp;
    <a href="https://kairos-24.com" style="color:#7B2FBE;text-decoration:none;">kairos-24.com</a></p>
  </td></tr>

  <!-- FOOTER LOGO -->
  <tr><td style="background:#f9f6ff;padding:20px 40px;text-align:center;border-top:1px solid #e8e0f0;">
    <img src="{logo_src}" alt="Kairos" style="width:120px;height:auto;opacity:0.85;">
    <p style="margin:10px 0 0;font-size:11px;color:#999;">
      Startup italiana · kairos-24.com · +39 348 872 5260
    </p>
  </td></tr>

  <!-- GDPR -->
  <tr><td style="background:#f0f0f0;padding:12px 40px;font-size:10px;color:#aaa;text-align:center;line-height:1.5;">
    Questa email è stata inviata a {email_dest} perché l'indirizzo è pubblicamente disponibile online.
    Kairos — kairos-24.com — Milano, Italia.
    Per non ricevere ulteriori comunicazioni, risponda con oggetto <em>Cancella</em>.
  </td></tr>

</table>
</td></tr>
</table>
</body></html>"""

    return html

# ─── LOG ─────────────────────────────────────────────────────────────────────
def carica_log():
    """Restituisce set di email già inviate."""
    inviate = set()
    if LOG.exists():
        with open(LOG, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("Stato") == "INVIATA":
                    inviate.add(row["Email"].lower().strip())
    return inviate

def scrivi_log(nome, email, categoria, template, stato, errore=""):
    nuovi = not LOG.exists()
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuovi:
            w.writerow(["Data", "Ora", "Nome Attività", "Email", "Categoria", "Template", "Stato", "Errore"])
        w.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%H:%M:%S"),
            nome, email, categoria, template, stato, errore
        ])

# ─── INVIA SINGOLA EMAIL VIA RESEND ──────────────────────────────────────────
def invia_email(email_da, nome_mittente, nome_attivita, email_dest, template):
    """Invia una email tramite Resend API."""
    oggetto = OGGETTO[template]
    html    = costruisci_html(nome_attivita, template, email_dest)

    params = {
        "from":    f"{nome_mittente} <{email_da}>",
        "to":      [email_dest],
        "subject": oggetto,
        "html":    html,
    }
    # Resend.send() lancia un'eccezione se qualcosa va storto
    resend.Emails.send(params)

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    modo_test  = "--test"  in sys.argv
    solo_stato = "--stato" in sys.argv

    # Carica credenziali
    creds          = leggi_credenziali()
    EMAIL_FROM     = creds["EMAIL"]                        # business@kairos-24.it
    RESEND_API_KEY = creds.get("RESEND_API_KEY", "").strip()
    NOME_MITTENTE  = creds.get("NOME_MITTENTE", "Raul Colombo — Kairos").strip()

    if not RESEND_API_KEY:
        print("\n❌ RESEND_API_KEY mancante in credenziali_mail.txt")
        print("   Segui la GUIDA_RESEND.md per ottenere la chiave API.")
        sys.exit(1)

    # Imposta API key globalmente
    resend.api_key = RESEND_API_KEY

    # Carica Excel
    df = pd.read_excel(EXCEL, sheet_name=SHEET)
    df = df[df["Email"].notna() & (df["Email"].astype(str).str.contains("@"))]
    df = df.sort_values("Score", ascending=False).reset_index(drop=True)

    # Carica log
    gia_inviate = carica_log()

    # Filtra non ancora inviate
    da_inviare = df[~df["Email"].str.lower().str.strip().isin(gia_inviate)].copy()

    print(f"\n{'='*55}")
    print(f"  KAIROS — Invio email outreach  [Resend.com]")
    print(f"{'='*55}")
    print(f"  Mittente:                {EMAIL_FROM}")
    print(f"  Totale contatti Excel:   {len(df)}")
    print(f"  Già inviate:             {len(gia_inviate)}")
    print(f"  Da inviare oggi:         {min(len(da_inviare), MAX_PER_SESSIONE)}")
    print(f"{'='*55}\n")

    if solo_stato:
        return

    if len(da_inviare) == 0:
        print("✅ Tutte le email sono già state inviate!")
        return

    # Modalità test: invia solo a te stesso
    if modo_test:
        print("🧪 MODALITÀ TEST — invio solo a te stesso\n")
        try:
            invia_email(EMAIL_FROM, NOME_MITTENTE, "Ristorante Test", EMAIL_FROM, "ristoranti")
            print(f"✅ Email di test inviata a {EMAIL_FROM}! Controlla la tua casella.")
        except Exception as e:
            print(f"❌ Errore invio test: {e}")
        return

    # Invio reale
    da_inviare  = da_inviare.head(MAX_PER_SESSIONE)
    inviate_ora = 0
    errori      = 0

    for i, row in da_inviare.iterrows():
        nome      = str(row["Nome Attività"]).strip()
        email     = str(row["Email"]).strip()
        categoria = str(row.get("Categoria", "")).strip()
        template  = template_per_categoria(categoria)

        print(f"[{inviate_ora+1}/{len(da_inviare)}] {nome}")
        print(f"         Email:     {email}")
        print(f"         Categoria: {categoria}  →  template: {template}")

        try:
            invia_email(EMAIL_FROM, NOME_MITTENTE, nome, email, template)
            scrivi_log(nome, email, categoria, template, "INVIATA")
            inviate_ora += 1
            print(f"         ✅ Inviata\n")
        except Exception as e:
            scrivi_log(nome, email, categoria, template, "ERRORE", str(e))
            errori += 1
            print(f"         ❌ Errore: {e}\n")

        # Pausa tra email (tranne l'ultima)
        if inviate_ora + errori < len(da_inviare):
            pausa = random.randint(DELAY_MIN, DELAY_MAX)
            print(f"         ⏳ Pausa {pausa} secondi...\n")
            time.sleep(pausa)

    print(f"\n{'='*55}")
    print(f"  ✅ Inviate questa sessione:  {inviate_ora}")
    print(f"  ❌ Errori:                   {errori}")
    print(f"  📋 Log salvato in:           log_email_inviate.csv")
    rimanenti = len(df) - len(gia_inviate) - inviate_ora
    if rimanenti > 0:
        print(f"  📬 Rimanenti per domani:     {rimanenti}")
    else:
        print(f"  🎉 Tutte le email completate!")
    print(f"{'='*55}\n")

if __name__ == "__main__":
    main()
