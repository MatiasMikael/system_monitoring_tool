# System Monitoring Tool

## Yleiskatsaus

Tämä projekti monitoroi järjestelmän suorituskykyä (CPU, muistin ja levyn käyttöä) ja tallentaa tiedot CSV-muotoon. Se tuottaa automaattisesti PDF-raportin kerätyistä tiedoista.

## Rakenne

- **`monitor_system_with_csv.py`**: Seuraa järjestelmän suorituskykyä ja tallentaa tiedot CSV-tiedostoon.
- **`generate_pdf_report.py`**: Lukee CSV-tiedoston ja luo siitä PDF-muotoisen raportin.

## Käyttöohjeet

1. **Käynnistä järjestelmän monitorointi**:
   ```bash
   python monitor_system_with_csv.py
   ```
   Tämä skripti seuraa CPU:n, muistin ja levyn käyttöä ja tallentaa tiedot `5_logs/system_metrics.csv` -tiedostoon.

2. **Luo PDF-raportti**:
   ```bash
   python generate_pdf_report.py
   ```
   Tämä skripti lukee CSV-tiedoston ja generoi siitä `3_results/system_report.pdf` -tiedoston.

## Käytetyt kirjastot ja työkalut

- `psutil`: Järjestelmän resurssien monitorointiin.
- `csv`: Tietojen tallentamiseen CSV-muodossa.
- `logging`: Lokitiedostojen hallintaan.
- `reportlab`: PDF-raportin luomiseen.
-  ChatGPT: Projektin suunnitteluun ja toteutukseen.

## Lisenssi

Tämä projekti on lisensoitu **MIT-lisenssillä**, mikä tarkoittaa, että kuka tahansa saa käyttää, kopioida, muokata ja levittää tätä ohjelmistoa **edellyttäen, että alkuperäinen tekijä mainitaan**
