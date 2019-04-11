from django.db import models



class Creator(models.Model):
    name = models.CharField( max_length=50)
    profileUrl = models.URLField( max_length=200)

    def __str__(self):
       return self.name


class Presentation(models.Model):
    ident = models.CharField(verbose_name='id',max_length=25, blank=True,null=True)
    
    title = models.CharField( max_length=50)
    thumbnail = models.URLField( max_length=200)
    author = models.ForeignKey("information.Creator", on_delete=models.CASCADE)
    createdAt = models.DateField( auto_now=False, auto_now_add=False,blank=True,null=True)#,input_formats=DATE_INPUT_FORMATS)

    def __str__(self):
        return self.title