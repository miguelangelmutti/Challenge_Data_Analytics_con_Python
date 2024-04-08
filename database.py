from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:postgres@localhost/challenge_data_analytics_con_python')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

if __name__ == '__main__':
    pass 