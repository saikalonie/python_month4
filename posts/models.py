from django.db import models
"""CREATE TABLE posts (id=int primary key, title=varchar(100), desription=varcar)"""
"all objects - Post.objects.all()----> SELECT * FROM posts"
"""SELECT * FROM posts WHERE id=1"""
"one object - Post.objects.get(id=1)----> SELECT * FROM posts WHERE id=1"
"""SELECT * FROM posts WHERE title ILIKE '%a%'"""
"few items by condition- Post.objects.filter(title='title')----> SELECT * FROM posts WHERE id=1"
<<<<<<< HEAD
"""INSERT into posts(title, description) values('title', 'description') """
"create object - Post.objects.create()"
=======
>>>>>>> d0a8e2e1d6f04fff339d55bbc5e72f56566b62bb

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
<<<<<<< HEAD
    tags = models.ManyToManyField(Tag, blank=True )
=======
    tags = models.ManyToManyField(Tag, blank=True)
>>>>>>> d0a8e2e1d6f04fff339d55bbc5e72f56566b62bb
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
