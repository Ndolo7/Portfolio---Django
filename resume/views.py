from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show=[
        { "title":"Portfolio Website",
            'path':"images/portfolio.jpg",
            'url':"https://imaniportfolio-lpbmow4i.b4a.run/",
        },

        {
            "title":"Resume Creator",
            'path':"images/Resumegen.jpg",
            'url':"https://freeonlineresumegenerator.vercel.app/",
        },

        {
            "title":"Amazon E-Commerce Clone",
            'path':"images/amazon.jpg",
            'url':"https://ndolo7.github.io/Amazon-project/",
        },

        {
            "title":"USSD App Dashboard",
            'path':"images/dashboard.jpg",
            'url':"https://github.com/Ndolo7/testing-Ussd111",
        },

        {
            "title":"Ubuntu Fund Web App (Django Backend)",
            'path':"images/ubuntu.jpg",
            'url':"https://github.com/Ndolo7/ubuntufinal",
        },

        {
            "title":"project6",
            'path':"images/project6.jpg",
            'url':"https://github.com/Ndolo7/Portfolio---Django",
        },
    ]
    return render(request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience=[
        {
            "company":"Cloud90 Software Solutions",
            'position':"Full Stack Software Engineer",
        },

        {
            "company":"Redwaters Consultancy",
            'position':"PHP/mySql developer",
            'link':"https://www.redwatersconsultancy.com/"
        },

        {
            "company":"Private Bureau of Investigation",
            'position':"Software Engineer and Algorithm designer",
        },

    ]
    return render(request,"experience.html",{"experience": experience})



def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Prepare email content
        subject = f'New Contact Form Message from {name}'
        email_message = f"""
        New message from your website contact form.

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        try:
            # Send email
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # You'll receive the email
                fail_silently=False,
            )
            
            # Add success message
            messages.success(request, 'Thank you! Your message has been sent successfully. I will reach out to you.')
            return redirect('contact')  # Redirect to same page after success
            
        except Exception as e:
            print(f"Error sending email: {e}")  # For debugging
            messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
    
    return render(request, 'contact.html')

def resume(request):
    resume_path="myfiles/resume1.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="Imani_SoftwareDev_Resume.pdf"
            return response
    else:
        return HttpResponse("Resume not found", status=404)