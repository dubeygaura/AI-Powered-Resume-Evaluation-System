import PyPDF2
import re

SKILL_SET = ["Python", "Django", "JavaScript", "SQL", "HTML", "CSS"]

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def extract_skills(text):
    found_skills = []
    for skill in SKILL_SET:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return ", ".join(found_skills)


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text


def calculate_ats_score(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    resume_words = set(resume_text.split())
    jd_words = set(job_description.split())

    matched_words = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0

    score = (len(matched_words) / len(jd_words)) * 100
    return round(score)