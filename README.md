# Daily Sales ETL Pipeline (Native Python)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![ETL](https://img.shields.io/badge/ETL_Process-success.svg)
![Data Cleaning](https://img.shields.io/badge/Data_Cleaning-Active-orange.svg)

## Project Overview
This project is an **ETL (Extract, Transform, Load) Pipeline** built entirely with native Python (standard library, no external dependencies like Pandas). 

It simulates a real-world business scenario: processing a "dirty" daily sales CSV file generated at 7:00 AM, cleaning the data, calculating key business metrics (average ticket, totals by category, top products), and generating an automated executive report in JSON format before the 9:00 AM daily meeting.

## Technical Features
* **Fault Tolerance:** Implementation of `try-except` blocks and data validation to ensure that a corrupt record does not stop the program execution.
* **Data Cleaning:** Handling of null fields, default value imputation (e.g., quantity = 1), and string formatting.
* **Efficient Data Structures:** Use of `defaultdict` from the `collections` module for metrics aggregation and revenue grouping by category without nested loops.
* **Modular Architecture:** Clear separation of concerns between the main entry point (`Main.py`) and the business/transformation logic (`Proceso.py`).
* **Error Logging:** Generation of a parallel file (`errores_dia.json`) that isolates defective records for further review by the support team.

## Project Structure

```text
📁 Proyecto_ETL_Ventas/
├── 📁 data/
│   ├── ventas_dia.csv       # Simulated raw data (Generated input)
│   ├── resumen_dia.json     # Generated executive report (Output)
│   └── errores_dia.json     # Failed records log (Logs)
├── Datos_Ejemplos.py        # Script to generate the simulated "dirty" CSV
├── Main.py                  # Main script controller
└── Proceso.py               # Extraction, transformation, and load logic