from django.shortcuts import render


def index(reqest):
    data = {'title': 'Тимошка центр', 'values': ['Some', 'Hellow', '123']}
    return render(reqest, 'main/index.html', data)


def abaut(reqest):
    return render(reqest, 'main/abaut.html')


def telephone(reqest):
    return render(reqest, 'main/telephone.html')
