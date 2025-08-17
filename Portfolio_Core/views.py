from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from Portfolio import settings

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
        sender = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Save to DB
        Contact.objects.create(
            name=sender,
            email=email,
            message=message,
        )

        # Send email
        send_mail(
            subject=f"A work email from {sender} ({email}) on Portfolio",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['osamaelgebaly122@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your email has been sent :)')
        return redirect('home')






def home(request):
    titles = Title.objects.all().order_by('-id')[:4]
    bio = Bio.objects.last()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    icons = ContactIcon.objects.all()
    services = Service.objects.all()
    journeycards = JourneyCard.objects.prefetch_related('contents').all().order_by('-id')


    return render(request,'home.html',{
        'journeycards':journeycards,
        'titles':titles,
        'bio':bio,
        'projects':projects,
        'skills':skills,
        'icons':icons,
        'services':services,

    })


