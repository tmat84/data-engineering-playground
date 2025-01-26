from sqlalchemy import create_engine
from config import config


params = config()
engine = create_engine(f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}/{params['database']}",
                        echo=True)