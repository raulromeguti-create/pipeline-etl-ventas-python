# Daily Sales ETL Pipeline with Python

A beginner Data Engineering project that implements an ETL pipeline using Python's standard library to process, clean, and analyze daily sales data.

## 📌 Project Overview

This project simulates a business scenario in which an online store needs to process daily sales data before a management meeting.

The input CSV contains inconsistent and invalid records, such as missing fields, empty values, and invalid prices. The pipeline validates and transforms the data, calculates business metrics, and generates an executive report in JSON format.

The main goal is to understand the fundamentals of ETL pipelines before moving on to tools such as Pandas, SQL, or Apache Spark.

## 🎯 Objectives

- Build a modular ETL pipeline using native Python.
- Process CSV files containing inconsistent data.
- Validate records and handle invalid values.
- Calculate sales metrics and aggregate revenue.
- Export results to JSON files.
- Separate valid records from records that cannot be processed.

## ⚙️ Pipeline Workflow

### 1. Extract

- Read sales data from a CSV file.
- Load the records for further processing.
- Simulate a daily sales dataset using sample data.

### 2. Transform

- Validate required fields.
- Convert prices and quantities to numeric values.
- Apply the required default value when quantity is missing (`quantity = 1`).
- Handle invalid records using exception handling.
- Continue processing when an individual record cannot be processed.

### 3. Analyze & Load

Calculate business metrics, including:

- Total revenue.
- Average transaction value.
- Revenue by category.
- Top-selling products.
- Number of unique customers.
- Processing statistics and rejected records.

The results are exported to JSON files for further analysis.

## 🛠️ Technologies

- **Python 3**
- `csv` — CSV file processing.
- `json` — JSON report generation.
- `collections.defaultdict` — Data aggregation.
- `datetime` — Date and time handling.
- `try-except` — Exception handling and fault tolerance.

**Dependencies:** None. The project uses Python's standard library.

## 📂 Project Structure

```text
pipeline-etl-ventas-python/
├── data/
│   ├── ventas_dia.csv
│   ├── resumen_dia.json
│   └── errores_dia.json
├── Datos_Ejemplos.py
├── Enunciado.txt
├── Main.py
├── Proceso.py
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `Datos_Ejemplos.py` | Generates the sample sales CSV, including intentionally incorrect data. |
| `Main.py` | Coordinates the execution of the pipeline. |
| `Proceso.py` | Implements data extraction, validation, transformation, aggregation, and report generation. |
| `data/ventas_dia.csv` | Input sales dataset. |
| `data/resumen_dia.json` | Generated executive report. |
| `data/errores_dia.json` | Information about records that could not be processed. |

## ▶️ How to Run

### Requirements

- Python 3 installed.
- No external libraries required.

### Execution

Clone the repository:

```bash
git clone https://github.com/raulromeguti-create/pipeline-etl-ventas-python.git
cd pipeline-etl-ventas-python
```

Generate the sample dataset:

```bash
python Datos_Ejemplos.py
```

Run the ETL pipeline:

```bash
python Main.py
```

The generated reports are saved in the `data/` directory.

> Run the commands from the project root directory so that the relative file paths work correctly.

## 📊 Outputs

### Executive report — `resumen_dia.json`

Contains the business metrics calculated from the valid sales records, including revenue, average transaction value, category totals, and top products.

### Error report — `errores_dia.json`

Contains information about records that could not be processed, allowing invalid data to be reviewed separately.

## 📚 Key Learnings

Through this project, I have practised:

- Designing a modular ETL workflow.
- Reading and writing CSV and JSON files.
- Cleaning and validating inconsistent data.
- Handling exceptions without stopping the entire pipeline.
- Aggregating business metrics with Python data structures.
- Separating pipeline orchestration from transformation logic.

## 🚀 Future Improvements

Potential next steps for this project include:

- Adding automated tests with `unittest` or `pytest`.
- Improving error reporting with specific rejection reasons.
- Handling empty datasets and cases where no valid records remain.
- Improving monetary calculations to avoid floating-point precision issues.
- Adding configurable input and output paths.
- Extending the pipeline with SQL, Pandas, or an orchestration tool.

## 👨‍💻 About

This is an initial project in my Data Engineering learning journey. I built it to strengthen my Python fundamentals and understand how data moves through an ETL process before introducing more advanced technologies.

**Feedback and suggestions are welcome!**
