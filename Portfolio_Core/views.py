from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def project_details(request,pk):
    project = Project.objects.get(id=pk)
    features = ProjectFeature.objects.filter(project=project)
    images = ProjectImage.objects.filter(project=project)
    videos = ProjectVideo.objects.filter(project=project)
    return render(request,'project.html',{'project':project,
                                          'features':features,
                                          'images':images,
                                          'videos':videos})


def send_message(request):
    if request.method == 'POST':
        sender = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject= F'A work email from {sender} on Portfolio ',
            message=message,
            from_email=email,
            recipient_list=['osamaelgebaly122@gmail.com'],
            fail_silently=False,
            html_message=None,
        )
        contact = Contact.objects.create(
            name = sender,
            email = email,
            message = message,
        )
        messages.success(request,'Your email is sent :)')
        return redirect('home')

        





def home(request):
    titles = Title.objects.all().order_by('-id')[:4]
    bio = Bio.objects.last()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    icons = ContactIcon.objects.all()

    return render(request,'home.html',{

        'titles':titles,
        'bio':bio,
        'projects':projects,
        'skills':skills,
        'icons':icons

    })


