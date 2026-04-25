from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    #read the projects from the csv file and pass them to the template
    df = pd.read_csv('projects.csv', sep=';')
    projects_list = df.to_dict('records')

    projects = []
    for i in range(0, len(projects_list), 4):
        projects.append(projects_list[i:i+4])

    return render_template('index.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

app.run(debug=True)