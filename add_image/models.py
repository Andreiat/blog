from django.db import models

class ImgAdd(models.Model):
    class Meta:
        db_table = 'img_add'
        verbose_name = "Добавить картинку"

    title = models.CharField("Название", max_length=20)
    img = models.ImageField("Картинка", upload_to='images', blank=True)

    def __str__(self):
        return self.title
