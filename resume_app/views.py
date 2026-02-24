from django.shortcuts import render
from .forms import ResumeForm
from .utils import extract_text_from_pdf, extract_skills, calculate_ats_score

def upload_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()

            # Extract Resume Text
            text = extract_text_from_pdf(resume.resume_file)
            resume.extracted_text = text

            # Extract Skills
            skills = extract_skills(text)
            resume.skills = skills

            # Calculate ATS Score
            score = calculate_ats_score(text, resume.job_description)
            resume.ats_score = score

            resume.save()

            return render(request, "upload.html", {
                "form": ResumeForm(),
                "skills": skills,
                "score": score
            })
    else:
        form = ResumeForm()

    return render(request, "upload.html", {"form": form})