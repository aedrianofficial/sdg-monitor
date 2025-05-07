import io
from pdfminer.high_level import extract_text
from fastapi import UploadFile
from typing import Dict, List

# Expanded keywords for SDG classification
SDG_KEYWORDS = {
    "01": ["poverty", "inequality", "poor", "destitute", "impoverished", "low-income", "economic hardship"],
    "02": ["hunger", "agriculture", "food security", "nutrition", "sustainable farming", "malnutrition", "famine"],
    "03": ["health", "well-being", "disease", "mortality", "healthcare", "medical", "wellness", "pandemic"],
    "04": ["education", "learning", "literacy", "teaching", "school", "students", "training", "skills"],
    "05": ["gender equality", "women empowerment", "discrimination", "girls", "feminism", "gender gap"],
    "06": ["water", "sanitation", "hygiene", "clean water", "wastewater", "drinking water", "water scarcity"],
    "07": ["energy", "renewable", "electricity", "solar", "wind power", "clean fuel", "energy efficiency"],
    "08": ["economic growth", "employment", "decent work", "labor rights", "jobs", "entrepreneurship"],
    "09": ["infrastructure", "industrialization", "innovation", "technology", "manufacturing", "sustainable industry"],
    "10": ["inequality", "social inclusion", "discrimination", "marginalized", "income gap", "equal opportunity"],
    "11": ["cities", "urban", "communities", "housing", "slums", "public transport", "urban planning"],
    "12": ["consumption", "production", "recycling", "waste", "sustainability", "resource efficiency"],
    "13": ["climate change", "global warming", "emissions", "carbon", "greenhouse gas", "climate action"],
    "14": ["oceans", "marine", "seas", "fisheries", "coastal", "underwater", "sea life", "aquatic"],
    "15": ["forests", "biodiversity", "ecosystems", "wildlife", "desertification", "land degradation"],
    "16": ["peace", "justice", "institutions", "governance", "rule of law", "corruption", "human rights"],
    "17": ["partnerships", "global cooperation", "development finance", "technology transfer", "capacity building"]
}

async def classify_research_file(file: UploadFile) -> Dict:
    """
    Classify a research file according to relevant SDGs
    
    Args:
        file: Uploaded file object
        
    Returns:
        Dictionary with matched SDGs and their keywords
    """
    contents = await file.read()
    text = extract_text(io.BytesIO(contents))
    
    matches = []
    for sdg_number, keywords in SDG_KEYWORDS.items():
        matched_keywords = [keyword for keyword in keywords if keyword.lower() in text.lower()]
        if matched_keywords:
            matches.append({
                "sdg_number": sdg_number,
                "matched_keywords": matched_keywords
            })
    
    return {"matched_sdgs": matches}