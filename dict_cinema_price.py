print('Пятница, Чемпионы, Пернатая банда')

movies={'Пятница':{12:250,16:350,20:450},
       'Чемпионы':{10:250,13:350,16:350},
       'Пернатая банда':{10:350,14:450,18:450}}

film=input('Выберите фильм: ')
data=input('Выберите дату (сегодня, завтра): ')
time=int(input('Выберите время: '))
a=int(input('Укажите количество человек: '))
price=movies[film][time]

if data=='завтра':
    price=price*0.95
if a>19:
    price=price*0.8

print(film,data,'в',time,price,'рублей')
