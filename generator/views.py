from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'chars': range(6,17)})

def password(request):
    genereated_pass = ''

    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    length = int(request.GET.get('length', 14))

    for i in range(100):
        random.shuffle(chars)

    for x in range(length):
        genereated_pass += random.choice(chars)

    return render(request, 'generator/password.html', { 'password': genereated_pass})