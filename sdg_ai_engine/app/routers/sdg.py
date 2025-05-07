from fastapi import APIRouter, UploadFile, File
from app.services.sdg_classifier import classify_research_file


router = APIRouter(prefix="/sdg", tags=["SDG Classification"])

@router.post("/analyze")
async def analyze_research_file(file: UploadFile = File(...)):
    result = await classify_research_file(file)
    return result
