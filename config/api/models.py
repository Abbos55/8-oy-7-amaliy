from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Kategoriya(models.Model):
    nomi = models.CharField(max_length=200, unique=True)
    davomiyligi = models.PositiveSmallIntegerField(default=4)

    def __str__(self):
        return self.nomi


class Vakansiya(models.Model):
    sarlavha = models.CharField(max_length=200)
    tavsif = models.CharField(max_length=300, blank=True, null=True)
    maosh = models.IntegerField()
    kategoriya = models.ForeignKey(
        Kategoriya, on_delete=models.CASCADE, related_name='vakansiyalar', null=True
    )

    def __str__(self):
        return self.sarlavha


class Fikr(models.Model):
    muallif = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    matn = models.TextField()
    yaratilgan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.muallif.username} - {self.matn[:30]}"
