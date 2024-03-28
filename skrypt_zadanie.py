import string
from io import open

data_to_chose = ['load data', 'export data', 'analyze & predict']
choice = 'x'

def DisplayOptions(options: list) -> string:
    for index,value in enumerate(options,start=1):
        print(index," - ",value)
    wartosc = input("Podaj wartość liczbową opcji : ")
    return wartosc


#USAGE OF FUNCTION
while choice:
        choice = DisplayOptions(data_to_chose)
        if choice:
            try:
                choice_num = int(choice)
                print("wchodzi do Try")
                if (0< choice_num <= len(data_to_chose)):
                    print("Wybrano liczbe: ", choice_num)
                else:
                    print("Dokonano nieprawidłowego wyboru zakresu liczby")

            except ValueError:
                print("Wprowadź liczbę a nie napis/literke")

        else:
            print(" KONIEC PROGRAMU :) ")





