from django.db import models

# Create your models here.


# Need a signal to send email when contact 


class Project(models.Model):
    name = models.CharField(max_length=250)
    short_description = models.TextField()
    full_description = models.TextField(null=True,blank=True)
    github_repo_link = models.URLField(null=True,blank=True)
    live_link = models.URLField(null=True,blank=True)
    tech_stack = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class ProjectFeature(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    feature = models.TextField()

    def __str__(self):
        return f'{self.project.name}  {self.feature}'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/projects-images/')
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.project.name


class ProjectVideo(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    video = models.FileField(upload_to='media/project-videos/')
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.project.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField( max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.name




class Title(models.Model):
    title = models.CharField( max_length=50)

    def __str__(self):
        return self.title


class Bio(models.Model):
    bio = models.TextField()

    def __str__(self):
        return self.bio

class ContactIcon(models.Model):
    icon = models.CharField(max_length=200)
    link = models.URLField()

