import io
from pdfminer.high_level import extract_text
from fastapi import UploadFile
from typing import Dict, List, Tuple

# SDG subcategories with keywords
SDG_SUBCATEGORIES = {
    "01": {
        "1.1": ["extreme poverty", "absolute poverty", "$1.25 a day", "$1.90 a day"],
        "1.2": ["poverty reduction", "poverty line", "national poverty"],
        "1.3": ["social protection", "social security", "safety nets", "vulnerable populations"],
        "1.4": ["equal rights", "economic resources", "basic services", "microfinance"],
        "1.5": ["resilience", "climate-related events", "economic shocks", "disasters"],
        "1.A": ["resource mobilization", "development assistance", "poverty programs"],
        "1.B": ["policy frameworks", "pro-poor", "gender-sensitive development"]
    },
    "02": {
        "2.1": ["hunger", "food security", "malnutrition", "stunting", "wasting"],
        "2.2": ["malnutrition", "nutritional needs", "adolescent girls", "pregnant women"],
        "2.3": ["agricultural productivity", "small-scale food producers", "family farmers"],
        "2.4": ["sustainable food production", "resilient agriculture", "ecosystem"],
        "2.5": ["genetic diversity", "seeds", "cultivated plants", "equitable sharing"],
        "2.A": ["rural infrastructure", "agricultural research", "technology", "gene banks"],
        "2.B": ["trade restrictions", "agricultural subsidies", "export subsidies"],
        "2.C": ["food commodity markets", "price volatility", "food reserves"]
    },
    "03": {
        "3.1": ["maternal mortality", "childbirth", "reproductive health"],
        "3.2": ["newborn", "infant mortality", "under-5 mortality", "preventable deaths"],
        "3.3": ["AIDS", "tuberculosis", "malaria", "tropical diseases", "hepatitis"],
        "3.4": ["non-communicable diseases", "mental health", "well-being"],
        "3.5": ["substance abuse", "narcotic drug", "alcohol", "addiction"],
        "3.6": ["road traffic", "accidents", "road safety"],
        "3.7": ["sexual health", "reproductive health", "family planning", "contraceptive"],
        "3.8": ["universal health coverage", "health services", "medicines", "vaccines"],
        "3.9": ["hazardous chemicals", "air pollution", "water pollution", "contamination"],
        "3.A": ["tobacco control", "smoking"],
        "3.B": ["vaccines", "medicines", "TRIPS", "doha declaration"],
        "3.C": ["health financing", "health workforce", "health training"],
        "3.D": ["early warning", "health risks", "national and global health"]
    },
    "04": {
        "4.1": ["free education", "primary education", "secondary education", "equitable education"],
        "4.2": ["early childhood development", "pre-primary education", "early childhood care"],
        "4.3": ["technical education", "vocational training", "university", "affordable education"],
        "4.4": ["relevant skills", "technical skills", "vocational skills", "entrepreneurship"],
        "4.5": ["gender disparities", "education equality", "vulnerable", "persons with disabilities"],
        "4.6": ["literacy", "numeracy", "adult literacy", "functional skills"],
        "4.7": ["sustainable development", "global citizenship", "cultural diversity", "culture of peace"],
        "4.A": ["education facilities", "inclusive learning environments", "safe schools"],
        "4.B": ["scholarships", "developing countries", "higher education", "vocational training"],
        "4.C": ["qualified teachers", "teacher training", "international cooperation"]
    },
    "05": {
        "5.1": ["discrimination against women", "gender discrimination", "gender equality"],
        "5.2": ["violence against women", "trafficking", "sexual exploitation"],
        "5.3": ["harmful practices", "child marriage", "forced marriage", "female genital mutilation"],
        "5.4": ["unpaid care", "domestic work", "public services", "social protection"],
        "5.5": ["women's participation", "leadership", "political participation", "economic decisions"],
        "5.6": ["sexual and reproductive health", "reproductive rights", "family planning"],
        "5.A": ["equal rights", "economic resources", "property ownership", "financial services"],
        "5.B": ["technology", "women's empowerment", "ICT", "digital inclusion"],
        "5.C": ["gender equality policies", "women's empowerment", "legislation"]
    },
    "06": {
        "6.1": ["safe drinking water", "affordable drinking water", "universal access to water"],
        "6.2": ["sanitation", "hygiene", "open defecation", "women and girls"],
        "6.3": ["water quality", "pollution reduction", "wastewater", "recycling"],
        "6.4": ["water-use efficiency", "water scarcity", "sustainable withdrawals"],
        "6.5": ["integrated water resources management", "transboundary cooperation", "IWRM"],
        "6.6": ["water-related ecosystems", "wetlands", "rivers", "aquifers", "lakes"],
        "6.A": ["international cooperation", "water harvesting", "desalination", "wastewater treatment"],
        "6.B": ["local community participation", "water management", "sanitation management"]
    },
    "07": {
        "7.1": ["universal access to energy", "modern energy services", "reliable energy"],
        "7.2": ["renewable energy", "clean energy", "solar", "wind", "hydroelectric"],
        "7.3": ["energy efficiency", "energy intensity", "energy conservation"],
        "7.A": ["clean energy research", "renewable energy technology", "energy investment"],
        "7.B": ["energy infrastructure", "sustainable energy services", "developing countries"]
    },
    "08": {
        "8.1": ["economic growth", "per capita growth", "GDP growth", "national circumstances"],
        "8.2": ["economic productivity", "diversification", "technological upgrading", "innovation"],
        "8.3": ["development-oriented policies", "productive activities", "entrepreneurship", "SMEs"],
        "8.4": ["resource efficiency", "sustainable consumption", "sustainable production", "decoupling"],
        "8.5": ["full employment", "decent work", "equal pay", "people with disabilities"],
        "8.6": ["youth employment", "education", "training", "NEET"],
        "8.7": ["forced labour", "modern slavery", "human trafficking", "child soldiers", "child labour"],
        "8.8": ["labour rights", "safe working environments", "migrant workers", "precarious employment"],
        "8.9": ["sustainable tourism", "local culture", "tourism jobs", "local products"],
        "8.10": ["domestic financial institutions", "banking", "insurance", "financial services"],
        "8.A": ["aid for trade", "trade-related assistance", "developing countries"],
        "8.B": ["global jobs strategy", "youth employment", "ILO global jobs pact"]
    },
    "09": {
        "9.1": ["infrastructure", "sustainable infrastructure", "regional infrastructure", "affordable access"],
        "9.2": ["sustainable industrialization", "industrial employment", "GDP share"],
        "9.3": ["small-scale enterprises", "financial services", "value chains", "markets"],
        "9.4": ["clean technologies", "resource efficiency", "industrial processes"],
        "9.5": ["scientific research", "technological capabilities", "innovation", "R&D workers"],
        "9.A": ["sustainable infrastructure development", "financial support", "technological support"],
        "9.B": ["domestic technology development", "industrial diversification", "value addition"],
        "9.C": ["ICT access", "universal internet", "affordable internet", "least developed countries"]
    },
    "10": {
        "10.1": ["income growth", "bottom 40 percent", "income inequality"],
        "10.2": ["social inclusion", "economic inclusion", "political inclusion", "empowerment"],
        "10.3": ["equal opportunity", "discriminatory laws", "policies", "practices"],
        "10.4": ["fiscal policy", "wage policy", "social protection", "equality"],
        "10.5": ["global financial markets", "financial institutions", "regulations"],
        "10.6": ["representation of developing countries", "international decision-making", "global institutions"],
        "10.7": ["migration", "mobility", "migration policies", "planned migration"],
        "10.A": ["special and differential treatment", "developing countries", "WTO", "trade"],
        "10.B": ["official development assistance", "foreign direct investment", "financial flows"],
        "10.C": ["migrant remittances", "transaction costs", "remittance corridors"]
    },
    "11": {
        "11.1": ["adequate housing", "slums", "basic services", "affordable housing"],
        "11.2": ["transport systems", "public transport", "road safety", "vulnerable people"],
        "11.3": ["sustainable urbanization", "participatory planning", "settlement planning"],
        "11.4": ["cultural heritage", "natural heritage", "world heritage"],
        "11.5": ["disaster deaths", "disaster economic losses", "water-related disasters"],
        "11.6": ["urban environmental impact", "air quality", "municipal waste", "waste management"],
        "11.7": ["green spaces", "public spaces", "persons with disabilities", "women and children"],
        "11.A": ["urban-rural links", "national and regional development planning"],
        "11.B": ["disaster risk management", "resilience", "climate adaptation"],
        "11.C": ["sustainable buildings", "resilient buildings", "least developed countries"]
    },
    "12": {
        "12.1": ["sustainable consumption", "sustainable production", "10YFP", "developed countries"],
        "12.2": ["natural resources", "sustainable management", "efficient use"],
        "12.3": ["food waste", "food loss", "supply chains", "harvest losses"],
        "12.4": ["chemicals", "wastes", "life cycle", "air, water and soil pollution"],
        "12.5": ["waste reduction", "prevention", "reduction", "recycling", "reuse"],
        "12.6": ["sustainability information", "reporting cycle", "corporate sustainability"],
        "12.7": ["public procurement", "sustainable procurement", "national policies"],
        "12.8": ["awareness", "sustainable development", "lifestyles in harmony with nature"],
        "12.A": ["scientific capacity", "technological capacity", "sustainable patterns"],
        "12.B": ["sustainable tourism", "monitoring impacts", "job creation", "local culture"],
        "12.C": ["fossil-fuel subsidies", "tax restructuring", "harmful subsidies"]
    },
    "13": {
        "13.1": ["climate resilience", "adaptive capacity", "natural disasters"],
        "13.2": ["climate change measures", "national policies", "planning", "strategies"],
        "13.3": ["climate change education", "awareness", "human and institutional capacity"],
        "13.A": ["climate finance", "Green Climate Fund", "UNFCCC", "$100 billion commitment"],
        "13.B": ["climate planning", "management", "least developed countries", "SIDS"]
    },
    "14": {
        "14.1": ["marine pollution", "nutrient pollution", "land-based activities"],
        "14.2": ["marine ecosystems", "coastal ecosystems", "resilience", "restoration"],
        "14.3": ["ocean acidification", "scientific cooperation", "pH levels"],
        "14.4": ["overfishing", "illegal fishing", "destructive fishing", "fish stocks"],
        "14.5": ["marine protected areas", "coastal conservation", "area-based conservation"],
        "14.6": ["fisheries subsidies", "overcapacity", "illegal fishing", "WTO"],
        "14.7": ["marine resources", "SIDS", "least developed countries", "economic benefits"],
        "14.A": ["marine technology", "ocean health", "marine biodiversity", "research capacity"],
        "14.B": ["small-scale fishers", "market access", "marine resources", "artisanal fishing"],
        "14.C": ["UNCLOS", "ocean conservation", "sustainable use", "law of the sea"]
    },
    "15": {
        "15.1": ["terrestrial ecosystems", "freshwater ecosystems", "conservation", "sustainable use"],
        "15.2": ["sustainable forest management", "deforestation", "reforestation", "degraded forests"],
        "15.3": ["desertification", "degraded land", "drought", "land degradation neutrality"],
        "15.4": ["mountain ecosystems", "biodiversity", "capacity for sustainability"],
        "15.5": ["biodiversity loss", "threatened species", "extinction", "habitat degradation"],
        "15.6": ["genetic resources", "fair sharing", "appropriate access", "traditional knowledge"],
        "15.7": ["protected species", "poaching", "trafficking", "illegal wildlife products"],
        "15.8": ["invasive alien species", "ecosystems", "land water ecosystems"],
        "15.9": ["ecosystem values", "biodiversity values", "planning processes", "poverty reduction"],
        "15.A": ["financial resources", "biodiversity", "ecosystems", "sustainable use"],
        "15.B": ["forest management", "conservation finance", "sustainable forestry"],
        "15.C": ["poaching", "trafficking", "local communities", "sustainable livelihoods"]
    },
    "16": {
        "16.1": ["violence reduction", "violent deaths", "conflict-related deaths"],
        "16.2": ["child abuse", "exploitation", "trafficking", "violence against children"],
        "16.3": ["rule of law", "justice for all", "equal access to justice"],
        "16.4": ["illicit financial flows", "arms flows", "stolen assets", "organized crime"],
        "16.5": ["corruption", "bribery", "public officials", "illicit enrichment"],
        "16.6": ["effective institutions", "accountable institutions", "transparent institutions"],
        "16.7": ["responsive decision-making", "inclusive decision-making", "participatory decision-making"],
        "16.8": ["developing countries in global governance", "global institutions", "inclusive institutions"],
        "16.9": ["legal identity", "birth registration", "documentation"],
        "16.10": ["public access to information", "fundamental freedoms", "protection of journalists"],
        "16.A": ["violent extremism", "national institutions", "terrorism prevention"],
        "16.B": ["non-discriminatory laws", "sustainable development policies"]
    },
    "17": {
        "17.1": ["tax collection", "domestic revenue", "domestic capacity"],
        "17.2": ["official development assistance", "GNI", "development commitments"],
        "17.3": ["financial resources", "multiple sources", "developing countries"],
        "17.4": ["debt sustainability", "debt financing", "debt relief", "debt restructuring"],
        "17.5": ["investment promotion", "least developed countries", "incentive regimes"],
        "17.6": ["science cooperation", "technology cooperation", "knowledge sharing"],
        "17.7": ["environmentally sound technologies", "favorable terms", "mutual agreement"],
        "17.8": ["technology bank", "capacity building", "ICT", "least developed countries"],
        "17.9": ["capacity building", "national plans", "sustainable development"],
        "17.10": ["multilateral trading", "WTO", "doha development agenda"],
        "17.11": ["developing countries' exports", "least developed countries' exports", "trade share"],
        "17.12": ["duty-free market access", "quota-free market access", "least developed countries"],
        "17.13": ["global macroeconomic stability", "policy coordination", "policy coherence"],
        "17.14": ["policy coherence", "sustainable development"],
        "17.15": ["policy space", "country ownership", "poverty eradication", "sustainable development"],
        "17.16": ["global partnership", "multi-stakeholder partnerships", "knowledge sharing"],
        "17.17": ["public partnerships", "private partnerships", "civil society partnerships"],
        "17.18": ["data availability", "data quality", "data disaggregation", "statistical capacity"],
        "17.19": ["statistical capacity", "measuring progress", "GDP alternatives"]
    }
}

async def classify_sdg_subcategories(text: str, sdg_numbers: List[str]) -> Dict:
    """
    Classify text into SDG subcategories based on matched SDG numbers
    
    Args:
        text: The extracted text from the document
        sdg_numbers: List of matched SDG numbers from the main classifier
        
    Returns:
        Dictionary with matched subcategories and their keywords
    """
    matched_subcategories = {}
    
    for sdg_number in sdg_numbers:
        if sdg_number in SDG_SUBCATEGORIES:
            subcategory_matches = []
            
            for subcategory, keywords in SDG_SUBCATEGORIES[sdg_number].items():
                matched_keywords = [keyword for keyword in keywords if keyword.lower() in text.lower()]
                
                if matched_keywords:
                    subcategory_matches.append({
                        "subcategory": subcategory,
                        "matched_keywords": matched_keywords
                    })
            
            if subcategory_matches:
                matched_subcategories[sdg_number] = subcategory_matches
                
    return matched_subcategories

async def analyze_with_subcategories(file: UploadFile) -> Dict:
    """
    Analyze a file and classify it into both SDG categories and subcategories
    
    Args:
        file: Uploaded file object
        
    Returns:
        Dictionary with matched SDGs and their subcategories
    """
    contents = await file.read()
    text = extract_text(io.BytesIO(contents))
    
    from app.services.sdg_classifier import SDG_KEYWORDS
    
    # First level SDG classification
    matches = []
    matched_sdg_numbers = []
    
    for sdg_number, keywords in SDG_KEYWORDS.items():
        matched_keywords = [keyword for keyword in keywords if keyword.lower() in text.lower()]
        if matched_keywords:
            matches.append({
                "sdg_number": sdg_number, 
                "matched_keywords": matched_keywords
            })
            matched_sdg_numbers.append(sdg_number)
    
    # Subcategory classification
    subcategory_matches = await classify_sdg_subcategories(text, matched_sdg_numbers)
    
    # Combine results
    for match in matches:
        sdg_number = match["sdg_number"]
        if sdg_number in subcategory_matches:
            match["subcategories"] = subcategory_matches[sdg_number]
    
    return {"matched_sdgs": matches}