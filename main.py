text = input("Введите список слов через пробел: ")
number = 0
letter = input("Введите букву: ")
text_on = text.split()
for word in text_on:
  if letter in word:
    number +=1
print("В вашем списке количество слов с буквой",letter,"=",number)