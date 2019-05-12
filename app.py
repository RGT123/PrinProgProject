import Driver
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def getDogs(freeTime,alone,exercise,allergies,salary,children,reaction,fatSkinny,patience,temperature,grooming):
    print (freeTime + alone+exercise+allergies+salary+children+reaction+fatSkinny+patience+temperature+grooming)



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
    #getDogs(freeTime,alone,exercise,allergies,salary,children,reaction,fatSkinny,patience,temperature,grooming)
    Driver.getFreeTime(freeTime)
    Driver.getAlone(alone)
    Driver.getExercise(exercise)
    Driver.getAllergies(allergies)
    Driver.getSalary(salary)
    Driver.getChildren(children)
    Driver.getReaction(reaction)
    Driver.getFatSkinny(fatSkinny)
    Driver.getPatience(patience)
    Driver.getTemperature(temperature)
    Driver.getGrooming(grooming)
    Driver.main()
    return grooming



if __name__ == '__main__':

    app.run(debug=True)
