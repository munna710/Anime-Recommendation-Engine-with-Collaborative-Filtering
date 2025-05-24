# Anime-Recommendation-Engine-with-Collaborative-Filtering

A complete automated pipeline for generating personalized anime recommendations using **collaborative filtering (SVD)**. This project demonstrates a modular and scalable workflow built with **Apache Airflow**, **Pandas**, **Surprise**, and **Parquet**.

## 🚀 Features

- 📥 Ingests anime & ratings data
- 🛠️ Cleans & transforms data to efficient Parquet format
- 🤖 Trains a matrix factorization model (SVD)
- 🎯 Optionally generates personalized recommendations
- 🔄 Fully orchestrated with Apache Airflow DAGs

## ⚙️ Pipeline Overview

### Step 1: Data Ingestion (`scripts/ingest_data.py`)
Loads raw `anime.csv` and `rating.csv` into `data_raw/`.

### Step 2: ETL Transformation (`scripts/etl.py`)
Cleans and converts data to `Parquet` format → saved in `data_processed/`.

### Step 3: Model Training (`scripts/train_model.py`)
Trains an SVD model (Collaborative Filtering) using the Surprise library.

### Step 4: Generate Recommendations (`scripts/generate_recommendations.py`)
Loads the model and generates top-N recommendations per user (optional).

## 🛠️ Setting Up

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
