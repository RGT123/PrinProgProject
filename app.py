from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    freeTime = request.form['freeTime']
    alone = request.form['alone?']
    exercise = request.form['exercise']
    allergies= request.form['allergies']
    salary=request.form['salary']
    children=request.form['children?']
    reaction=request.form['reaction']
    fatSkinny=request.form['fatSkinny']
    patience=request.form['patience']
    temperature=request.form['temperature']
    grooming=request.form['grooming']
    print(fatSkinny)
    return freeTime




if __name__ == '__main__':
    app.run(debug=True)
