from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import sys
import os

# Add the scripts folder to the system path so Airflow can import them
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import your Python scripts
import ingest_data
import etl
import train_model

# Optional: If you add a recommendation generator script
try:
    import generate_recommendations
    has_recommender = True
except ImportError:
    has_recommender = False

# Define default arguments for the DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

# Define the DAG
with DAG(
    'anime_recommender_pipeline',
    default_args=default_args,
    description='Anime Recommendation ETL + Model Training DAG',
    schedule_interval='@daily',  # Run daily
    tags=['anime', 'recommender', 'ETL']
) as dag:

    # Ingest raw data (copy files to data_raw/)
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data.ingest_data
    )

    # Transform raw data into clean format (Parquet)
    etl_task = PythonOperator(
        task_id='transform_data',
        python_callable=etl.etl
    )

    # Train recommendation model and save
    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model.train_model
    )

    # (Optional) Generate recommendations after training
    if has_recommender:
        recommend_task = PythonOperator(
            task_id='generate_recommendations',
            python_callable=generate_recommendations.main
        )
        # Define task dependencies with recommendation step
        ingest_task >> etl_task >> train_task >> recommend_task
    else:
        # Define task dependencies without recommendation step
        ingest_task >> etl_task >> train_task
