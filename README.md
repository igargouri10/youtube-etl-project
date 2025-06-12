# 📺 YouTube ETL Pipeline Project

An automated ETL pipeline that:
- 📥 Extracts video data from the YouTube Data API
- 🧼 Transforms and cleans the data
- 💾 Loads it into a SQLite database
- 📊 Visualizes it with a Streamlit dashboard
- 🔁 Runs daily via Windows Task Scheduler

## 📁 Project Structure

- `extract/` – Gets raw data from the API
- `transform/` – Cleans and enriches data
- `load/` – Saves data into a SQLite database
- `dashboard/` – Streamlit dashboard for insights
- `main_etl_pipeline.py` – Runs the full ETL pipeline
- `run_etl.bat` – Windows automation script

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
