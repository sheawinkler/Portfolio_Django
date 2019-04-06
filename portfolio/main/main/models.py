from django.db import models

## possible classes for my portfolio:
##   images page, blog page, employment history page, fun page
class Tutorials(models.Model):
    # specify columns of 'tutorials'
    # ->django model fields
    tutorial_title = models.CharField(max_length=200) ## set a maximum
    tutorial_content = models.TextField() ## text blob
    tutorial_published = models.DateTimeField("date published")

    ## override str function
    def __str__(self):
        return self.tutorial_title ## makes it easier to read on webpage


    