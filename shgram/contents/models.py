import os
import uuid

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    # 이 클래스 자체가 추상화클래스가 되어  클래스의 클래스라고 생각하자.
    # 메타 옵션에서 abstract = True 를 설정하면 엄마 모델은 실제로 또는
    # 물리적으로 존재하지 않는 가상의 클래스가 된다. 그리고 새끼 모델들은 엄마의 필드와 속성,
    # 함수들을 다 물려받아 실체가 있는 DB 테이블이 된다.
    # 그니까 상속관계 없이 자식이 독립적이게 된다는거임.
    # ❯ python manage.py makemigrations
    #   Migrations for 'contents':
    #   contents/migrations/0001_initial.py
    #   - Create model Content
    #   - Create model Image
    # 보셈 베이스모델은 언급되지않음


class Content(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "컨텐츠"


def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
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
