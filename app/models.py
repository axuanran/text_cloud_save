# app/models.py
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 确保db目录存在
db_dir = "./db"
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/test.db"  # Adjust the path as needed
Base = declarative_base()
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class LogData(Base):
    __tablename__ = "logs"
    id = Column(String, primary_key=True, index=True)
    data = Column(String, index=True)

# 函数来初始化数据库（创建表）
def init_db():
    Base.metadata.create_all(bind=engine)