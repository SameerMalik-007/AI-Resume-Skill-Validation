import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Simple skill database 
SKILLS_DB = [
    "python", "java", "c++", "machine learning",
    "data analysis", "sql", "html", "css", "javascript"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

def calculate_score(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    if len(job_skills) == 0:
        return 0, []

    score = int((len(matched) / len(job_skills)) * 100)
    return score, list(matched)
