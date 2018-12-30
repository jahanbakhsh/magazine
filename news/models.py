from django.db import models
import uuid
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from froala_editor.fields import FroalaField

class News(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = FroalaField(theme='dark')
    image = models.ImageField(upload_to='img/news/')
    date = models.DateField()
    source = models.CharField(max_length=100)
    international = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='writer')
    updated_by = models.ForeignKey(User, null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='editor')

    @property
    def short_content(self):
        return truncatechars(self.content, 100)

    def get_writer(self):
        return '{} {}'.format(self.created_by.last_name, self.created_by.first_name)
