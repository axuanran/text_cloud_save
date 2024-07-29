# app/main.py
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models
from app.models import SessionLocal,init_db
from pydantic import BaseModel, validator



app = FastAPI()
init_db()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/{id}")
async def read_log(id: str,db: Session = Depends(get_db)):
    db_log = db.query(models.LogData).filter(models.LogData.id == id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return {"id": db_log.id, "data": db_log.data}

@app.post("/")
async def log_data_post(id: str, data: str, db: Session = Depends(get_db)):
    db_log = models.LogData(id=id, data=data)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"id": db_log.id, "data": db_log.data}


@app.get("/")
async def log_data_get(id: str, data: str, db: Session = Depends(get_db)):
    db_log = models.LogData(id=id, data=data)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"id": db_log.id, "data": db_log.data}

