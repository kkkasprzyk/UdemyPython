# import os
# import string
# sciezka = r'plik.txt'
#
# result = os.path.isfile(sciezka)
#
#
# def countWords(path)-> string:
#
#     if os.path.isfile(sciezka):
#         f = open(path,'r').read()
#         print("Otwarcie pliku")
#
#     return len(f.split())
#
# print("Ilosc slow w pliku : ",countWords(sciezka))
#
# wyrazenie = os.path.isfile(sciezka) and print("ilosc slow :",len(open(sciezka,'r').read().split()))

@uppercase == 123
def greet():
  return "Saved!"

# Using the decorated function
print(greet())
