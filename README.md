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

```

2. Set `YOUTUBE_API_KEY` in your shell using a newly issued, restricted key. `.env.example` lists the variable name; this project does not automatically load `.env` files. Never commit credentials.
3. From the repository root, run each stage:

```bash
python extract/fetch_youtube_data.py
python transform/transform_youtube_data.py
python load/load_to_sqlite.py
streamlit run dashboard/youtube_dashboard.py
```

## Scope and limitations

This is an educational prototype. Extraction currently retrieves up to 10 upload entries (video ID, title and publication time) plus channel metadata. It does not implement pagination or per-video likes/views collection. The loader replaces its table rather than performing incremental upserts. The provided batch script can be configured in Windows Task Scheduler; scheduling is not established by the repository alone. The entry-point imports are not a validated end-to-end runner; use the explicit stages above.

## Credential remediation

The previously hard-coded Google API key must be revoked or rotated in its owning Google Cloud project. Removing it from the latest source does not revoke it, and older Git commits can still contain it. Restrict any replacement to the YouTube Data API and the appropriate application context. Do not paste replacement credentials into issues, commits or chat.
