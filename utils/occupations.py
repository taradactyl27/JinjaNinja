import random

filename = 'data/occupations.csv'
f = open(filename,'rU')
text = f.read()


def makeDict(num):
    dict = {}
    dict2 = {}
    L1 = text.split("\n")
    L = filter(None, L1)
    i = 1
    count = 0
    while i < len(L)-1:
        if L[i][0] == '"':
            index = L[i].find('"', 1, len(L[i]))
            count += float(L[i][index+2:]) * 10
            dict[count] = L[i][1:index]
            dict2[L[i][1:index]] = float(L[i][index+2:]) 
            i += 1
        else:
            line = L[i].split(",")
            count += float(line[1]) * 10
            dict[count] = line[0]
            dict2[line[0]] = float(line[1]) 
            i += 1
    if num == 2:
        return dict2
    return dict

def rand():
    dict = makeDict(1)
    ans = 0
    number = random.randint(1,998)
    for thing in dict:
        if ans == 0:
            if number <= thing:
                ans = thing
        elif number <= thing:
            if thing < ans:
                ans = thing
    return dict[ans]
