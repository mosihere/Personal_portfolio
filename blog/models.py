from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name=('posts'))

    def __str__(self):
        return self.title
# Here we use ManyToManyField the first argument is the Model that we want to create a relationship between them
# and the second argument is related_name= 'posts' --> it will help us to access category.posts when even
# we didn't add a field there(in Category Model)



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
# We use another relational field (ForeignKey())
# the difference between 'ForeignKey()' and "ManyToManyField()" is:
# ManyToManyField used for two-way relation like this --> each post can have 2 or more Category
# but here we use ForeignKey() and the reason behind this is --> each post can have so many comments
# many comments can be assigned to one POST :)
# TIP --> ForeignKey First Argument is the Model that we want to link (create a relation)
# and the second tells Django to what to do after a post deleted, in this CASE we don't need comments after a post deleted
