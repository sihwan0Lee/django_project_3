import os
import uuid

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')

    class Meta:
        # 최신글 먼저나오게
        ordering = ['-created_at']
        verbose_name_plural = "컨텐츠"


def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    print(uuid.uuid4(), ext)
    return os.path.join(instance.UPLOAD_PATH, "%s.%s" % (uuid.uuid4(), ext))

    # 16자리 고유한 아이디 생성


class Image(BaseModel):
    UPLOAD_PATH = 'user-upload'

    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)
    order = models.SmallIntegerField()  # image numbering

    class Meta:
        unique_together = ['content', 'order']
        ordering = ['order']
        verbose_name_plural = "이미지"


class FollowRelation(BaseModel):
    follower = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ManyToManyField(User, related_name='followee')
