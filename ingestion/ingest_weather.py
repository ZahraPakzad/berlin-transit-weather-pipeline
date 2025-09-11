import requests, datetime, io
import pandas as pd
import pyarrow as pa, pyarrow.parquet as pq
from google.cloud import storage

def main():
    dt = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    url = ("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41"
           "&hourly=temperature_2m,precipitation,wind_speed_10m")
    r = requests.get(url, timeout=30); r.raise_for_status()
    data = r.json()
    df = pd.DataFrame({
        "ts": pd.to_datetime(data["hourly"]["time"]),
        "temperature": data["hourly"]["temperature_2m"],
        "precipitation": data["hourly"]["precipitation"],
        "wind_speed": data["hourly"]["wind_speed_10m"]
    })
    df["dt"] = df["ts"].dt.date.astype(str)

    table = pa.Table.from_pandas(df)
    buf = io.BytesIO(); pq.write_table(table, buf, compression="snappy")
    client = storage.Client()
    bucket = client.bucket("mm-analytics-raw")
    blob = bucket.blob(f"weather/dt={dt}/part-000.parquet")
    blob.upload_from_file(buf, rewind=True)

if __name__ == "__main__":
    main()
