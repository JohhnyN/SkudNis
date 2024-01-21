from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from .arduino_handler import arduino_reader
import _sqlite3

from .models import *
from .forms import *


def index(request):
    historys = CardHistory.objects.all()
    return render(request, "main/index.html", {"historys": historys})


def takeCard(request):
    # if request.method == "POST":
    #     form = AddCardHistory(request.POST)
    #     if form.is_valid():
    #         office = form.cleaned_data["office"]
    #         if CardHistory.objects.filter(office=office, returned=False).exists():
    #             form.add_error("office", "Кабинет уже занят")
    #             return render(request, "main/take_card.html", {"form": form})
    #         else:
    #             try:
    #                 CardHistory.objects.create(**form.cleaned_data)
    #                 Office.objects.filter(office=office).update(busy=True)
    #                 return redirect("index")
    #             except:
    #                 return HttpResponse("Возникла ошибка при взятии карточки")
    #
    # else:
    #     form = AddCardHistory()
    office_card, teacher_card = arduino_reader()
    office = Office.objects.get(card_number=office_card)
    teacher = Teacher.objects.get(card_number=teacher_card)
    office_name = Office.objects.filter(card_number=office_card).values('office')[0]['office']
    teacher_name = Teacher.objects.filter(card_number=teacher_card).values('name')[0]['name']
    new_card_history = CardHistory(office=office, teacher=teacher, 
                                   start_time=datetime.now(), end_time=datetime.now(), returned=False)
    new_card_history.save()
    return render(request, "main/take_card.html", {"my_arguments": (office_name, teacher_name)})


def returnCards(request):
    # if request.method == "POST":
    #     form = ReturnCardHistory(request.POST)
    #
    #     if form.is_valid():
    #         # Получить данные из формы
    #         teacher = form.cleaned_data["teacher"]
    #         office = form.cleaned_data["office"]
    #
    #         # проверить, есть ли записи в таблице и выбрать последнюю
    #         historys = CardHistory.objects.filter(
    #             office=office, teacher=teacher, returned=False
    #         )
    #         history = historys.last()
    #
    #         if history:
    #
    #             # Изменить данные в найденной записи
    #             history.end_time = datetime.now()
    #             history.returned = True
    #
    #             # Сохранить изменения
    #             Office.objects.filter(office=office).update(busy=False)
    #             history.save()
    #
    #             # Вернуть успешный результат
    #             return redirect("index")
    #
    #         else:
    #             form.add_error("office", "Запись не найдена")
    #             return render(request, "main/return_card.html", {"form": form})
    #
    # else:
    #     form = ReturnCardHistory()

    office_card, teacher_card = arduino_reader()
    office = Office.objects.get(card_number=office_card)
    teacher = Teacher.objects.get(card_number=teacher_card)
    office_name = Office.objects.filter(card_number=office_card).values('office')[0]['office']
    teacher_name = Teacher.objects.filter(card_number=teacher_card).values('name')[0]['name']
    CardHistory.objects.filter(office=office, teacher=teacher).update(returned=True)
    return render(request, "main/return_card.html", {"my_arguments": (office_name, teacher_name)})


def about(request):
    return render(request, "main/about.html")


def info(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, "main/teacher_info.html", {"teacher": teacher})
