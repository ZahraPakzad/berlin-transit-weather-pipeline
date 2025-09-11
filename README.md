# Berlin Transit & Weather Data Pipeline

End-to-end data pipeline on GCP (Cloud Run, GCS, Prefect, Great Expectations) to ingest and validate Berlin public transport delays and weather data.


## Project outline

mm-analytics-ingestion/
├── ingestion/
│   ├── ingest_weather.py
│   ├── ingest_transport.py     # add later
│   ├── requirements.txt
│   └── Dockerfile
├── ge/
│   ├── great_expectations/
│   │   ├── expectations/
│   │   └── checkpoints/
│   └── Dockerfile              # containerize GE run
├── prefect_flows/
│   └── pipeline.py             # Prefect flow (ingestion → GE → dbt Cloud)
├── infra/                      # optional Terraform for buckets, IAM, etc.
│   └── main.tf
├── .github/workflows/ci.yml    # lint, unit tests, build+deploy images
└── README.md