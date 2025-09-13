from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.

class About(models.Model):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.
    
    **Template**
    :template:`about/about.html`
    """
    title = models.CharField()
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"    

     

