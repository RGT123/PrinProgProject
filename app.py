import Driver
import Scraper
from flask import Flask, render_template, request, redirect
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
    Scraper.main()
    finalDoge=Driver.main()
    if finalDoge == "breed0":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/golden-retriever/thomas")
    elif finalDoge == "breed1":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/akita/magic")
    elif finalDoge == "breed2":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/rottweiler/cody-0")
    elif finalDoge == "breed3":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/pomeranian/winston")
    elif finalDoge == "breed4":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/chihuahua/buddy")
    elif finalDoge == "breed5":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/yorkshire-terrier/misty-2")
    elif finalDoge == "breed6":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/poodles-standard/rachel-akc")
    elif finalDoge == "breed7":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/dachshund/quest")
    elif finalDoge == "breed8":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/schnoodle/goldie")
    elif finalDoge == "breed9":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/pomsky/aspen-4")
    elif finalDoge == "breed10":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/shih-tzu/sam-0")
    elif finalDoge == "breed11":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/labrador-retriever/kelly-3")
    elif finalDoge == "breed12":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/siberian-husky/sierra-3")
    elif finalDoge == "breed13":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/german-shepherd/reba-2")
    elif finalDoge == "breed14":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/boxer/cole")
    elif finalDoge == "breed15":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/australian-shepherd/teddy")
    elif finalDoge == "breed16":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/great-dane/larry")
    elif finalDoge == "breed17":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/doberman-pinscher/kara")
    elif finalDoge == "breed18":
        return redirect("https://www.lancasterpuppies.com/puppy-for-sale/cavalier-king-charles-spaniel/max-aca-registered")





if __name__ == '__main__':

    app.run(debug=True)
