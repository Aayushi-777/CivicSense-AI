from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from core.database import engine, Base
from api import complaints, dashboard

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CivicSense AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(complaints.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/health")
def health():
    return {"status": "ok"}