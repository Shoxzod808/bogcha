import os
import django

# Установка переменной окружения, указывающей Django, какой файл settings.py использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrIU.settings')

# Инициализация среды Django
django.setup()
4

from backend.models import Product
a = '''
Хочу;1200;70;0
Киви;1200;70;0
Джаззй;2300;50;0
СССР 1кг;23000;6;0
Фруитс мева;1200;50;0
Лух;2100;50;0
Избушка;6300;14;0
Гигантик;2200;48;0
Айс 1кг;22000;6;0
7 севен айс;5300;22;0
Бумба ок;2800;40;0
Зарли;3000;50;0
Челак 0,5;15000;6;0
Пломбир урома;2600;40;0
Евро;2600;48;0
Чйорний рожок;5000;20;0
Тошкент;3000;42;0
Челак 1кг;25000;2;0
Простокваша;6300;18;0
Миронда;3000;50;0
Лове;5000;30;0
Вега;5400;50;0
Супер голд;3700;30;0
Супер шок;5400;50;0
Мохибон;3700;30;0
Бумба шоколад;3700;40;0
Брикет Хива;2300;52;0
Конус;4700;45;0
Боост;4500;30;0
Зимушка;5000;28;0
Кругляшка;6200;20;0
Попа;3700;24;0
Айс пломбир;5500;14;0
Ссср рожок;3700;18;0
Орео;6000;24;0
Реал рожок;3500;20;0
Сити дом;6500;12;0
Ковичук;2200;40;0
Бамбей;6200;20;0
Натурол;3500;20;0
Вкус айс;6000;30;0
Хива покет;3000;48;0
Тендер;4500;30;0
Золотая голд;3500;30;0
8065;9800;20;0
Нежний;6000;30;0
8066;9800;20;0
Сохирний рожок;4800;20;0
Айс милк;6000;30;0
Матроскин;6000;18;0
8228;11000;26;0
Понсаке;5500;27;0
8247;11000;26;0
Айс банг;6000;30;0
Маршал;1300;50;0
Банан кофе;3000;42;0
8248;11000;26;0
Ковун;1500;50;0
8250;11000;26;0
Тарвуз;1500;50;0
8062;14000;20;0
Сендивич примал;0;30;0
Пломбир молочний реки;0;50;0
8063;14000;20;0
Колизей;0;30;0
8202;14000;26;0
Айс вентура;0;30;0
8203;14000;26;0
Сун плаза;0;30;0
Мих;0;30;0
Сенсатион;0;30;0
Вива;0;30;0
Муз 100;500;100;0
Муз 120;500;120;0
Брикет;13000;40;0
Дода;5400;20;0
Пресент;5400;24;0
Сендивич имкон;5500;28;0
'''
for s in a.split('\n')[1:]:
    name, price, case, count = s.split(';')
    print(name, price, case, count)
    Product.objects.create(
        name=name,
        price=price,
        case=case,
        count=0
    )