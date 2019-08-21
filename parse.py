# -*- coding: utf-8 -*-

# przedmiot obecnosc_3 = nieobecny xx
# przedmiot obecnosc_0 = obecny yy
# przedmiot obecnosc_1 = nieobecnosc usprawiedliwiona xx
# przedmiot obecnosc_5 = zajecia nie odbyly sie zz
# przedmiot obecnosc_2 = spoznienie zz
# przedmiot obecnosc_4 = zwolnienie xx
# przedmiot obecnosc_9 = zwolniony/obecny yy
# przedmiot obecnosc_7 = ferie zz

# xx - nieobecnosc
# yy- obecnosc
# zz - not in loop

from bs4 import BeautifulSoup
import os
from time import sleep as wait



def pobierz_frekfencje():

    data = []
    file = open('files/obecnosci.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(file, 'html.parser')
    obecnosci = {}
    for subject in soup.select('[class*="obecnosc_"]'):
       if 'obecnosc_3' in subject.attrs['class'] or 'obecnosc_1' in subject.attrs['class'] or 'obecnosc_4' in subject.attrs['class'] or 'obecnosc_0' in subject.attrs['class'] or 'obecnosc_9' in subject.attrs['class']:
            nieobecny = 'obecnosc_3' in subject.attrs['class'] or 'obecnosc_1' in subject.attrs['class'] or 'obecnosc_4' in subject.attrs['class']
            name_of_subject = subject.get_text(strip=True)
            obecnosci.setdefault(name_of_subject, [0, 0])[nieobecny] +=1

    file.close()

    for line in obecnosci:
        data.append(line[4:] + '|' + str(obecnosci.get(line)))

    przedmioty = []
    obecnosci = []
    nieobecnosci = []
    frekfencja = []

    for line in data:
        var = line.split('|')
        przedmiot = var[0]
        if przedmiot not in przedmioty:
            przedmioty.append(przedmiot)

    for line in range(len(przedmioty)):
        obecnosci.append(0)
        nieobecnosci.append(0)
        frekfencja.append(0)

    for line in data:
        var = line.split('|')
        przedmiot = var[0]
        obecny = var[1].split(',')[0][1:]
        nieobecny = var[1].split(',')[1][1:-1]
        index = przedmioty.index(przedmiot)
        obecnosci[index] = int(obecnosci[index]) + int(obecny)
        nieobecnosci[index] = int(nieobecnosci[index]) + int(nieobecny)

    for i in range(len(przedmioty)):
        frekfencja[i] = int((obecnosci[i] / (nieobecnosci[i] + obecnosci[i])) * 100)

    wynik = open('files/wyniki_frekfencja', 'w+' , encoding='utf-8')

    for i in range(len(przedmioty)):
        wynik.write(
            '<span charset="UTF-8">' + str(przedmioty[i]).title() + ' </span> ' + '<p align="right"> <b style="color: #78961D;" >' + str(obecnosci[i]) + '</b>  | <b style="color: #D94A3D;">' + str(nieobecnosci[i]) + ' </b> | <b style="color: #F2F2F2">' + str(frekfencja[i]) + '%' + ' </p> </b>')

    print('frekfencja przetworzona')


def pobierz_oceny():

    file = open('files/oceny.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(file, 'html.parser')
    tbody = soup.find('tbody')
    wynik = open('files/wyniki_oceny', 'w+', encoding='utf-8')
    for tr in tbody.find_all(class_='styl_wiersza1'):
        td = tr.find_all('td')[0].text.strip()
        ocena_sem1 = tr.find_all('td')[2].text.strip()
        ocena_sem2 = tr.find_all('td')[5].text.strip()
        ocena_koncowa = tr.find_all('td')[7].text.strip()
        wynik.write(str(td).title() + '     ' + '<b> <p align="right"> ' +ocena_sem1 + '  |  ' + ocena_sem2 + '  |  ' + ocena_koncowa + '</p> </b> ')

    for tr in tbody.find_all(class_='styl_wiersza2'):
        td = tr.find_all('td')[0].text.strip()
        ocena_sem1 = tr.find_all('td')[2].text.strip()
        ocena_sem2 = tr.find_all('td')[5].text.strip()
        ocena_koncowa = tr.find_all('td')[7].text.strip()
        wynik.write(str(td).title() + '     ' + '<b> <p align="right"> ' +ocena_sem1 + '  |  ' + ocena_sem2 + '  |  ' + ocena_koncowa + '</p> </b> ')

    print('oceny przetworzone')


