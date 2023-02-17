from flask import Flask, render_template
import pandas as pd
import flask
import os
import csv
from flask import Flask, render_template, request, url_for, redirect

dataframe = pd.read_csv("menu.csv")
maindictionary = {}
categories = []
for i in range(len(dataframe)):
        row = dataframe.iloc[i]
        category = row[0]
        print(category)
        if category not in maindictionary:
            maindictionary[category] = {}
            maindictionary[category][row[1]] = row[2]
            categories.append(category)
        else:
            maindictionary[category][row[1]] = row[2]
            print(maindictionary)

print(categories)

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return render_template('menu.html', cats = categories)

    if request.method == "POST":
     chosencategory = flask.request.form['chosencat']
     print(chosencategory)
     options = maindictionary[chosencategory].keys()
     print(options)
     return render_template('options.html', opts = options)



if __name__ == "__main__":
    app.run(debug=True)

print(maindictionary)