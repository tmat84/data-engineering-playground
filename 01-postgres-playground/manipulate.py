from connect import engine as postgres_engine
import pandas

def execute_sql(postgres_engine,sql):
    """
    Function to run sql statements in postgres
    """

    connection = postgres_engine.connect()
    trans = connection.begin()

    try:
        connection.execute(sql)
        trans.commit()
        connection.close()

    except Exception as err:
        trans.rollback()

    return True


def load_data(postgres_engine,df_pandas,schema_name,table_name,if_exists="append"):

    """
    Function to load data into postgres
    """
    connection = postgres_engine.connect()
    trans = connection.begin()

    try:

        df_pandas.to_sql(table_name,
                         con=postgres_engine,
                         schema=schema_name,
                         if_exists=if_exists,
                         index=False,
                         chunksize=1000)
    except Exception as err:
        trans.rollback()
        

    return True