from fastapi import APIRouter, UploadFile, File
from app.services.sdg_subcategory_classifier import analyze_with_subcategories

router = APIRouter(prefix="/sdg", tags=["SDG Classification"])

@router.post("/analyze")
async def analyze_research_file_with_subcategories(file: UploadFile = File(...)):
    """
    Analyze a research file and classify it according to relevant SDGs and subcategories
    """
    result = await analyze_with_subcategories(file)
    return result