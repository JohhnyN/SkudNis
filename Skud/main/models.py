from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    card_number = models.CharField(
        max_length=20, verbose_name="Номер карты", unique=True
    )  # card number
    name = models.CharField(max_length=100, verbose_name="ФИО")  # name
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(
        upload_to="teachers/%Y/%m/%d", verbose_name="Фото"
    )  # photo
    job_title = models.CharField(
        max_length=100, blank=True, verbose_name="Должность"
    )  # job title
    phone = models.CharField(max_length=11, blank=True, verbose_name="Телефон")  # phone
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )  # time created
    time_updated = models.DateTimeField(
        auto_now=True, verbose_name="Время обновления"
    )  # time updated
    active = models.BooleanField(default=True, verbose_name="Активен")  # card active

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ["name"]


class Office(models.Model):
    card_number = models.CharField(
        max_length=20, verbose_name="Номер карты", unique=True
    )  # card number
    office = models.CharField(max_length=100, verbose_name="Кабинет")  # office
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )  # time created
    time_updated = models.DateTimeField(
        auto_now=True, verbose_name="Время обновления"
    )  # time updated
    active = models.BooleanField(default=True, verbose_name="Активен")  # card active
    busy = models.BooleanField(default=False, verbose_name="Занято")

    def __str__(self) -> str:
        return self.office

    def get_absolute_url(self):
        return reverse("office_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Офис"
        verbose_name_plural = "Офисы"
        ordering = ["office"]


class CardHistory(models.Model):
    office = models.ForeignKey(
        "Office", on_delete=models.PROTECT, verbose_name="Кабинет"
    )
    teacher = models.ForeignKey(
        "Teacher", on_delete=models.PROTECT, verbose_name="Преподаватель"
    )
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="Время начала")
    end_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Время окончания"
    )
    returned = models.BooleanField(default=False, verbose_name="Возвращен")

    class Meta:
        verbose_name = "История карты"
        verbose_name_plural = "История карт"
        ordering = ["office"]


