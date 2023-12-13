from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/ricemill"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/ricemill2"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/testing_rice_mill"
# URL_DATABASE = "mysql+pymysql://root:MyN3wP4ssw0rd@localhost:3306/testing"
# URL_DATABASE = "mysql+pymysql://root:Chirag3949@localhost:3306/ricemill"


engine = create_engine(URL_DATABASE)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# # Replace the values with your actual credentials
# DB_USER = "avnadmin"
# DB_PASSWORD = "AVNS_XyV7dFHYHlGWaEHZ5rW"
# DB_HOST = "mysql-28668b5e-chiragsinghchauhan3949323-cc60.a.aivencloud.com"
# DB_PORT = "25076"
# DB_NAME = "defaultdb"

# # Construct the MySQL connection URL
# URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# engine = create_engine(URL_DATABASE)

# # You can keep the rest of your code as it is
# sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
