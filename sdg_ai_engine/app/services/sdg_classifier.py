import io
from pdfminer.high_level import extract_text
from fastapi import UploadFile

# Dummy keywords for classification
SDG_KEYWORDS = {
    "01": ["poverty", "inequality"],
    "02": ["hunger", "agriculture"],
    "03": ["health", "well-being"],
}

async def classify_research_file(file: UploadFile):
    contents = await file.read()
    text = extract_text(io.BytesIO(contents))
    
    matches = []
    for sdg_number, keywords in SDG_KEYWORDS.items():
        if any(keyword.lower() in text.lower() for keyword in keywords):
            matches.append({"sdg_number": sdg_number, "matched_keywords": keywords})

    return {"matched_sdgs": matches}
