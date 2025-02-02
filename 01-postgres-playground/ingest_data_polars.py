#Cleaned up version of data-loading.ipynb
import argparse, os, sys
from time import time
import pandas as pd 
import polars as pl
import pyarrow.parquet as pq
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    tb = params.tb
    url = params.url
    
    # Get the name of the file from url
    file_name = url.rsplit('/', 1)[-1].strip()
    print(f'Downloading {file_name} ...')
    # Download file from url
    os.system(f'curl {url.strip()} -o {file_name}')
    print('\n')

    # Create SQL engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Connection uri 
    uri = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # Read file based on csv or parquet
    if '.csv' in file_name:
        df = pd.read_csv(file_name, nrows=10)
        df_iter = pd.read_csv(file_name, iterator=True, chunksize=100000)
    elif '.parquet' in file_name:
        # file = pq.ParquetFile(file_name)
        # df_schema = next(file.iter_batches(batch_size=10)).to_pandas()
        # df_iter = file.iter_batches(batch_size=100000)
        df = pl.scan_parquet(file_name)
    else: 
        print('Error. Only .csv or .parquet files allowed.')
        sys.exit()


    # Create the table
    df.head(0).collect().write_database(table_name=tb, connection=engine, if_table_exists='append')


    # Insert values
    t_start = time()

    df.collect().write_database(table_name=tb, connection=engine, if_table_exists='append')

        
    t_end = time()   
    print(f'Completed! Total time taken was {t_end-t_start:10.3f} seconds.')    



if __name__ == '__main__':
    #Parsing arguments 
    parser = argparse.ArgumentParser(description='Loading data from .paraquet file link to a Postgres datebase.')

    parser.add_argument('--user', help='Username for Postgres.')
    parser.add_argument('--password', help='Password to the username for Postgres.')
    parser.add_argument('--host', help='Hostname for Postgres.')
    parser.add_argument('--port', help='Port for Postgres connection.')
    parser.add_argument('--db', help='Databse name for Postgres')
    parser.add_argument('--tb', help='Destination table name for Postgres.')
    parser.add_argument('--url', help='URL for .paraquet file.')

    args = parser.parse_args()
    main(args)