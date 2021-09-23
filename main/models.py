from django.db import models
from datetime import date

class Record(models.Model):
    title=models.CharField('Название',max_length=32)
    anons=models.TextField('Анонс')
    text=models.TextField('Содержание')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    picture=models.ImageField(blank=True,upload_to='images/')
    def __repr__(self):
        return self.title
    class Meta:
        verbose_name='Запись'
        verbose_name_plural='Записи'
class Comment(models.Model):
    content=models.TextField('Содержание')
    record=models.ForeignKey(Record,on_delete=models.CASCADE,
                             related_name='comments')
    user=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user.username)
