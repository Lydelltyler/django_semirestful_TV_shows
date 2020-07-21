from django.db import models

class ShowManager (models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Show title should be at least 5 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name should be at least 3 characters"
        if len(postData['release_date']) < 5:
            errors['release'] = "release date needs to be filled"
        if len(postData['desc']) < 5:
            errors["desc"] = "Show description should be at least 5 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.CharField(max_length=10)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
