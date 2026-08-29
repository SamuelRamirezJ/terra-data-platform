# Terra Data Platform 🚛

A data engineering platform for processing and analyzing logistics and trucking operations data.

## Overview

Terra Data Platform demonstrates an end-to-end data engineering workflow using realistic logistics data such as loads, mileage, fuel consumption, revenue, customers, and delivery routes.

## Tech Stack

- Python
- SQL
- PostgreSQL
- ETL / ELT
- REST APIs
- Docker
- Cloud Architecture

## Architecture

Raw Data → Python ETL → PostgreSQL → Analytics → API

## Planned Features

- Automated data ingestion
- Data cleaning and validation
- Dimensional data modeling
- Revenue and fuel-cost analytics
- Route profitability analysis
- REST API
- Automated testing
- Cloud deployment

## Status

🚧 Currently under development.

## Run Locally

```bash
git clone https://github.com/SamuelRamirezJ/terra-data-platform.git
cd terra-data-platform

pip install -r requirements.txt

python src/generate_data.py
python src/etl.py

uvicorn src.api:app --reload