from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://logicuser:NPqw0fk6!pz7+@localhost/logicpanel_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)