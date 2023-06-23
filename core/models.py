from django_summernote.fields import SummernoteTextField
from django.db import models
from account.models import Account


class Notary(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    account = models.OneToOneField(Account, verbose_name="Аккаунт", related_name="notary", on_delete=models.PROTECT)
    address = models.CharField(max_length=100, verbose_name="Адрес")
    house_number = models.CharField(max_length=15, verbose_name="Номер дома")
    latitude = models.CharField(max_length=100, verbose_name="Широта")
    longitude = models.CharField(max_length=100, verbose_name="Долгота")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    whatsapp = models.CharField(max_length=20, verbose_name="Номер whatsapp", null=True, blank=True)
    telegram = models.CharField(max_length=20, verbose_name="Номер telegram", null=True, blank=True)
    email = models.EmailField(verbose_name="Почта", null=True, blank=True)
    website = models.URLField(verbose_name="Сайт", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    image = models.ImageField(verbose_name="Фото", upload_to="notaries/", null=True, blank=True)
    schedule = models.TextField(verbose_name="График работы", null=True, blank=True)    

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Нотариус"
        verbose_name_plural = "Нотариусы"
    

class Rate(models.Model):
    rate = models.IntegerField(verbose_name="Рейтинг")
    notary = models.ForeignKey(Notary, verbose_name="Нотариус", related_name="rates", on_delete=models.PROTECT)
    user = models.ForeignKey(Account, verbose_name="Пользователь", related_name="rates", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.rate}"
    
    class Meta:
        unique_together = ("notary", "user")
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Page(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг", unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
    

class PageContent(models.Model):
    page = models.ForeignKey(Page, verbose_name="Страница", related_name="contents", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = SummernoteTextField(verbose_name="Контент")
    footer = models.BooleanField(verbose_name="Футер", default=False)
    body = models.BooleanField(verbose_name="Тело", default=False)
    class_name = models.CharField(max_length=100, verbose_name="Названия класса для фронта", blank=True, null=True)
    order = models.SmallIntegerField("Порядковый номер", default=1)
    style = models.TextField(verbose_name="CSS Стиль", blank=True, null=True)
    user = models.ForeignKey(Account, verbose_name="Пользователь", related_name="contents", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Контент страницы"
        verbose_name_plural = "Контенты страниц"
        ordering = ["page", "order"]
