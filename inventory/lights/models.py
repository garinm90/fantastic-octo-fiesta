from django.db import models
from django.utils.text import slugify


class Light(models.Model):
    light_type = models.CharField(max_length=100)
    in_stock = models.IntegerField(default=0)
    on_order = models.IntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.light_type

    def save(self, *args, **kwargs):
        self.slug = slugify(self.light_type)
        super(Light, self).save(*args, **kwargs)


class LightLog(models.Model):
    light = models.ForeignKey(Light, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now_add=True)
    lights_added = models.IntegerField(default=0)
    lights_pulled = models.IntegerField(default=0)
    lights_before = models.IntegerField(default=0)    
    lights_after = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.date_modified.strftime("%b %-d %Y")}'

    def add_lights(self):
        my_light = self.light
        my_light.in_stock += self.lights_added
        my_light.save(update_fields=['in_stock'])

    def remove_lights(self):
        my_light = self.light
        my_light.in_stock -= self.lights_pulled
        my_light.save(update_fields=['in_stock'])

    def save(self, *args, **kwargs):
        self.lights_before = self.light.in_stock
        if self.lights_added > 0:
            self.add_lights()
            self.lights_after = self.lights_added + self.lights_before
        elif self.lights_pulled > 0:
            self.remove_lights()
            self.lights_after =  self.lights_before - self.lights_pulled 
        super(LightLog, self).save(*args, **kwargs)

