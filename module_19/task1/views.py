from django.shortcuts import render
from django.http import HttpResponse

from task1.forms import UserRegister
from .models import *

def index(request):
    title = 'Главная страница'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'
    reg = 'Регистрация'

    context = {
        'title': title,
        'games': games,
        'carts': carts,
        'home': home,
        'reg': reg,
    }
    return render(request, 'task1/menu.html', context)

def games(request):

    title = 'Игры'
    game = Game.objects.all()
    sell = 'Купить'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'
    reg = 'Регистрация'

    context1={
        'title': title,
        'game': game,
        'sell': sell,
        'games': games,
        'carts': carts,
        'home': home,
        'reg': reg,
    }
    return render(request, 'task1/games.html', context1)

def cart(request):
    title = 'Корзина'
    error = 'Извините, Ваша корзина пуста'
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'
    reg = 'Регистрация'

    context2={
        'title': title,
        'error': error,
        'games': games,
        'carts': carts,
        'home': home,
        'reg': reg,
    }
    return render(request, 'task1/cart.html', context2)

def registration(request):
    users = Buyer.objects.all()
    games = 'Магазин'
    carts = 'Корзина'
    home = 'Главная страница'
    reg = 'Регистрация'
    info = {
        'form': UserRegister(),
        'games': games,
        'carts': carts,
        'home': home,
        'reg': reg,

    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for buyer in users:
                if buyer.name == name:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, 'task1/registration_page.html', info)

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            else:
                Buyer.objects.create(name=name, balance=3000.00, age=age)
                return HttpResponse(f'Приветствуем, {name}!')

    return render(request, 'task1/registration_page.html', info)