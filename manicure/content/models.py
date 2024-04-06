from django.db import models
from django.conf import settings
from authorization.models import Master, Client
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    
class ServiceType(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

class Service(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='service_images/')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    

class Blog(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')

    def str(self):
        return self.title

class CommentBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
    
class CommentService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
    
    
class FavoriteService(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

class FavoriteBlog(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)