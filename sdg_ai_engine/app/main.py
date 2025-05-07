from fastapi import FastAPI, UploadFile, File
from app.routers import sdg


app = FastAPI(title="SDG AI Engine")

# Include routes
app.include_router(sdg.router)

@app.get("/")
def read_root():
    return {"message": "SDG AI Engine is up!"}
