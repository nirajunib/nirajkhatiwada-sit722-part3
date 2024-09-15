from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_part3_y7ef_user:5GjPkPM8ITo0gGbdDlVV4bQVmkyuqqPp@dpg-crejvp3gbbvc73brfdjg-a.oregon-postgres.render.com/sit722_part3_y7ef"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
