# Generated by Django 4.2.2 on 2023-06-10 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Улица")),
            ],
        ),
        migrations.CreateModel(
            name="Notary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "house_number",
                    models.CharField(max_length=15, verbose_name="Номер дома"),
                ),
                ("latitude", models.CharField(max_length=100, verbose_name="Широта")),
                ("longitude", models.CharField(max_length=100, verbose_name="Долгота")),
                (
                    "phone",
                    models.CharField(max_length=12, verbose_name="Номер телефона"),
                ),
                (
                    "whatsapp",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Номер whatsapp",
                    ),
                ),
                (
                    "telegram",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Номер telegram",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Почта"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Сайт"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="notaries/",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "schedule",
                    models.TextField(
                        blank=True, null=True, verbose_name="График работы"
                    ),
                ),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="notary",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Аккаунт",
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="notaries",
                        to="core.address",
                        verbose_name="Адрес",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("slug", models.SlugField(unique=True, verbose_name="Слаг")),
            ],
        ),
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25, verbose_name="Области")),
            ],
        ),
        migrations.CreateModel(
            name="Village",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25, verbose_name="Админ. округ")),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="villages",
                        to="core.province",
                        verbose_name="Райнон",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PageContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Контент")),
                ("footer", models.BooleanField(default=False, verbose_name="Футер")),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="core.page",
                        verbose_name="Страница",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25, verbose_name="Районы")),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="districts",
                        to="core.province",
                        verbose_name="Область",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="village",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to="core.province",
                verbose_name="Райнон",
            ),
        ),
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.IntegerField(verbose_name="Рейтинг")),
                (
                    "notary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="rates",
                        to="core.notary",
                        verbose_name="Нотариус",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rates",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "unique_together": {("notary", "user")},
            },
        ),
    ]