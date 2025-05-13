from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
       return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

                                            class Novel(models.Model):
                                                title = models.CharField(max_length=255)
                                                    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='novels')
                                                        genres = models.ManyToManyField(Genre, related_name='novels')
                                                            summary = models.TextField()
                                                                isbn = models.CharField('ISBN', max_length=13, unique=True)
                                                                    cover_image = models.ImageField(upload_to='novel_covers/', null=True, blank=True)
                                                                        publication_date = models.DateField(null=True, blank=True)
                                                                            added_on = models.DateTimeField(auto_now_add=True)

                                                                                def __str__(self):
                                                                                        return self.title