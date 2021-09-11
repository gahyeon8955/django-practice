from django.db import models
import os
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse
from imagekit.models import ImageSpecField  #썸네일 지정
from imagekit.processors import ResizeToFill  #썸네일 크기

class Blog(models.Model):
    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
            ])

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    photo = models.ImageField(upload_to=date_upload_to, blank=True)
    image_thumbnail = ImageSpecField(source = 'photo',processors=[ResizeToFill(120,100)], format="JPEG", options={'quality':60})

    def __str__(self):
        return self.title

    def summary(self):
        return str(self.body)[:100]

    def get_absolute_url(self):
        return reverse('mainapp:detail', args=[self.id])