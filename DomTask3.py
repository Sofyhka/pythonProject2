one = ['А','В','Е','И','Н','О','Р','C','Т','A','E','I','O','U','L','N','S','T','R']
two = ['Д','К','Л','М','П','У','D','G']
three = ['Б','Г','Ё','Ь','Я','B','C','M','P']
four = ['Й','Ы','F','H','V','W','Y']
five = ['Ж','З','Х','Ц','Ч','K']
six = ['Ш','Э','Ю','J','X']
seven = ['Ф','Щ','Ъ','Q','Z']

us_string = input()
us_string = us_string.upper()

us_list = list(us_string)

print(us_list)

s = 0
for i in us_list:
    if i in one:
        s = s + 1
    elif i in two:
        s = s + 2
    elif i in three:
        s = s + 3
    elif i in four:
        s = s + 4
    elif i in five:
        s = s + 5
    elif i in six:
        s = s + 6
    elif i in seven:
        s = s + 7

print(s)