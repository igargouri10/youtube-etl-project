# main_etl_pipeline.py

import extract.fetch_youtube_data
import transform.transform_youtube_data
import load.load_to_sqlite

print("✅ ETL pipeline completed successfully.")
