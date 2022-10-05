numbers_divided = []
numbers_to_third_power = []

for i in range(101):
     if i % 5 == 0:
         numbers_divided.append(i)
         numbers_to_third_power.append(i**3)
print(numbers_divided)
print(numbers_to_third_power)

#Wrzuciłem dane w listę, żeby łatwiej było odczytać ze screen shota :> poniżej kodzik bardziej kompaktowy, ale wyrzucający dane w formie kolumny
'''for i in range(1, 101):
     if i % 5 == 0:
         print(i)
         print(i**3)'''