from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/ricemill"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/rice"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/testing_rice_mill"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/testing"
# URL_DATABASE = "mysql+pymysql://root:Chirag3949@localhost:3306/ricemill"
URL_DATABASE = "mysql+pymysql://chirag:zavr65@localhost:3306/ricemill"


engine = create_engine(URL_DATABASE)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
