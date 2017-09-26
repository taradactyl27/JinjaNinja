import random
from flask import Flask, render_template
myapp = Flask(__name__)
    
filename = 'occupations.csv'
f = open(filename,'rU')
text = f.read()

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

def rand():
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

@myapp.route('/')
def root():
    return render_template("template.html")

@myapp.route('/occupations')
def occup():
    return render_template("occupations.html", occupation = dict2, randoccupation = rand())

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
    

