import pandas as pd
from sqlalchemy import create_engine
from kestra import Kestra
import argparse
from datetime import datetime


def main(params):
    year = params.year
    month = params.month

    methods = [i for i in dir(Kestra) if not i.startswith("_")]
    print(f"Kestra methods: {methods}")

    df = pd.read_csv(filepath_or_buffer=f'data/Lista_operacji_{year}_{month}.csv',sep=';')

    #Clean the columns
    df.columns = df.columns.str.replace('/', '').str.replace('  ', '_').str.replace(' ', '_').str.lower()


    df['unique_row_id'] = pd.util.hash_pandas_object(df['data_księgowania'] + df['data_waluty'] + df['nadawca_odbiorca'] + 
                                                df['adres_nadawcy_odbiorcy'] + df['rachunek_źródłowy'] + df['rachunek_docelowy'] +
                                                df['tytułem'] + df['kwota_operacji'] + df['waluta'] +
                                                df['numer_referencyjny'] + df['typ_operacji'] + df['kategoria'])
    
    df['ingest_date'] = datetime.now()
    
    df['data_księgowania'] = pd.to_datetime(df['data_księgowania'], format='%d.%m.%Y')
    df['data_waluty'] = pd.to_datetime(df['data_waluty'], format='%d.%m.%Y')
    df['kwota_operacji'] = df['kwota_operacji'].str.replace(',','.').str.replace(' ','')
    df['kwota_operacji'] = pd.to_numeric(df['kwota_operacji'])

    engine = create_engine('postgresql://kestra:k3str4@host.docker.internal:5432/dev')

    
    # df.head(n=0).to_sql(name='stg_posting', con=engine, if_exists='replace',schema='raw')

    # df.head(n=0).to_sql(name='posting', con=engine, if_exists='replace',schema='raw')

    df.to_sql(name='stg_posting', con=engine, if_exists='replace',schema='raw')

    # Kestra.outputs({"Total" : "Success"})

if __name__ == '__main__':
    #Parsing arguments 
    parser = argparse.ArgumentParser(description='Loading data from .csv file link to a Postgres datebase.')


    parser.add_argument('--year', help='The year of the file.')
    parser.add_argument('--month', help='The month of the file.')

    args = parser.parse_args()
    main(args)