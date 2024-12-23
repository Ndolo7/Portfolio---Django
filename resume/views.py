from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show=[
        { "title":"project1",
            'path':"images/project1.jpg",
        },

        {
            "title":"project2",
            'path':"images/project2.jpg",
        },

        {
            "title":"project3",
            'path':"images/project3.jpg",
        },

        {
            "title":"project4",
            'path':"images/project4.jpg",
        },

        {
            "title":"project5",
            'path':"images/project5.jpg",
        },

        {
            "title":"project6",
            'path':"images/project6.jpg",
        },
    ]
    return render(request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience=[
        {
            "company":"ABC1",
            'position':"python developer",
        },

        {
            "company":"ABC2",
            'position':"python developer",
        },

        {
            "company":"ABC3",
            'position':"python developer",
        },

    ]
    return render(request,"experience.html",{"experience": experience})

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    resume_path="myfiles/resume1.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume1.pdf"
            return response
    else:
        return HttpResponse("Resume not found", status=404)