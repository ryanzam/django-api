# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PIL import Image
from django.conf import settings
from django.db import models

import os

# Create your models here.
class gallery(models.Model):
    title = models.CharField(max_length=100, default="unknown")
    thumbnail = models.ImageField("thumbnail",blank=True)
    image = models.ImageField("uploaded image", upload_to="gallery/")

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.thumbnail = generate_thumb(self.image)
        super(gallery, self).save(force_update=force_update)

def generate_thumb(imageTothumb, thumb_size=(200,150)):
    if not imageTothumb or imageTothumb == "":
        return

    image = Image.open(imageTothumb)
    image.thumbnail(thumb_size, Image.ANTIALIAS)

    imagefilename = os.path.basename(imageTothumb.name)

    splitImageName = imagefilename.split(".")
    ext = splitImageName.pop()
    img_name = "".join(splitImageName)

    new_image_name = img_name + "_thmnl." + ext
    print (new_image_name)
    image.save(os.path.join(settings.MEDIA_ROOT, new_image_name))

    return new_image_name