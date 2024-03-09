# var1= 2
# var2= var1 +0
#
# print(var1 is var2)
# print(id(var1),id(var2))

## Zadanie 4.LAB zmienne,funkcje id() i operator is
a,b,c=20,10,10
print(f"a = {a,id(a)}, b = {b,id(b)}, c = {c,id(c)}")

print("######")
a = b = c = [1, 2, 3]

print(a, b, c)
print(id(a), id(b), id(c))

a.append(4)

print(a, b, c)
print(id(a), id(b), id(c))
print('-----------------------------')

x = 10
y = 10
print(f"x = {x,id(x)}, y = {y,id(y)}")

y=y-1234567890+1234567890

print(f"x = {x,id(x)}, y = {y,id(y)}")
print('Czy identyfikatory są takie same ?',id(x) == id(y))
#
# LAB - Typy zmienne (mutable) i niezmienne (immutable)

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
del workdays[5:7]
print("days - > ",days)
print("workdays - > ",workdays)


