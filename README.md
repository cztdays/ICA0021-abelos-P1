# ICA0021 — Anton Belosapkin / abelos

**Aine:** ICA0021 Skriptimiskeeled
**Projekt:** P1
**Repository:** ICA0021-Skriptimiskeeled/ICA0021-abelos-P1

---

## P1 skripti idee

### Probleem

Organisatsioonides säilitatakse inimeste andmeid JSON-failides, kuid puudub lihtne viis vaadata, kui palju inimesi elab igas asukohas. Käsitsi loendamine on aeganõudev ja vigadele aldis.

### Sisend

Skript kasutab JSON-faili:

- `people.json` – nimekiri inimestest, kus igal isikul on vähemalt väli `location`

### Väljund

Skript tagastab sõnastiku (Dict), kus:
- **võti** on asukoha nimi
- **väärtus** on selles asukohas elavate inimeste arv

```
{'Tallinn': 3, 'Tartu': 2, 'Pärnu': 1}
```

---

## Testjuhtumid

### Positiivne test — korrektne JSON-formaat

**Sisend:** `people.json` — korrektne JSON-massiiv objektidega, millel on `location` väli
**Oodatav väljund:** Sõnastik asukohtade ja inimeste arvudega arvutatakse õigesti

### Negatiivne test — vale formaat

**Sisend:** fail ei ole korrektne JSON või vale struktuuriga
**Oodatav väljund:** skript tõstab erindi (`ValueError` või `FileNotFoundError`)

---

## Veatöötlus

Skript käsitleb järgmisi vigaseid sisendeid:

- **Fail ei ole JSON** — tekstifail või muu mittesobiv formaat → `ValueError`
- **Rikutud JSON** (corrupt) — poolik või vigane JSON-struktuur → `ValueError`
- **Vale struktuur** — JSON on olemas, aga ei ole massiiv objektidest → `ValueError`
- **Erimärgid** (ä, ö, ü, š, ž jne) — loetakse korrektselt UTF-8 kodeeringuga
- **Fail ei leidu** — → `FileNotFoundError`

---

## Kiirjuhend

```bash
git clone https://github.com/ICA0021-Skriptimiskeeled/ICA0021-abelos-P1.git
cd ICA0021-abelos-P1
```

### Skripti käivitamine

```bash
python Tests/run_tests.py
```

### Testide käivitamine

```bash
pytest Tests/test_people_counter.py -v
```
