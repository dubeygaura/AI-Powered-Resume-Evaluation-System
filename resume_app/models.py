from django.db import models

# Create your models here.


from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField(blank=True, null=True)  # NEW FIELD
    extracted_text = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    ats_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name