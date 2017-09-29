from flask import Flask, render_template
from utils import occupations
myapp = Flask(__name__)
    
filename = 'data/occupations.csv'
f = open(filename,'rU')
text = f.read()

@myapp.route('/')
def root():
    return render_template("template.html")

@myapp.route('/occupations')
def occup():
    return render_template("occupations.html", occupation = occupations.makeDict(2), randoccupation = occupations.rand())

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
    

