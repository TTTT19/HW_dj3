from csv import DictReader

from django.shortcuts import render





def inflation_view(request):
    template_name = 'inflation.html'
    row_names_list = ('Год;Янв;Фев;Мар;Апр;Май;Июн;Июл;Авг;Сен;Окт;Ноя;Дек;Суммарная').split(sep=';')
    # чтение csv-файла и заполнение контекста
    DATA = []
    with open('inflation_russia.csv', encoding='utf-8') as f:
        reader = DictReader(f)
        for row in reader:
            row = row['Год;Янв;Фев;Мар;Апр;Май;Июн;Июл;Авг;Сен;Окт;Ноя;Дек;Суммарная'].split(sep=';')
            DATA.append(row)
    context = {'row_names_list': row_names_list, 'DATA':DATA}

    return render(request, template_name,
                  context)





