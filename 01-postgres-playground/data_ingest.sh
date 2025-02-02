#! bin/bash

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

docker run -it \
  --network=01-postgres-playground_default \
  taxi_ingest:v003 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --tb=yellow_taxi_trips_polars \
    --url=${URL}