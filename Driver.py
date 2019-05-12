from flask import Flask, render_template, request
from urllib.request import urlopen, Request
import app
import Scraper
class User:
    def __init__(self,freeTime,alone,exercise,allergies,salary,children,reaction,fatSkinny,patience,temperature,grooming):
        self.freeTime=freeTime
        self.alone=alone
        self.exercise=exercise
        self.allergies=allergies
        self.salary=salary
        self.children=children
        self.reaction=reaction
        self.fatSkinny=fatSkinny
        self.patience=patience
        self.temperature=temperature
        self.grooming=grooming
user1=User(None,None,None,None,None,None,None,None,None,None,None)
def main():
    ourDogs=Scraper.dogs
    print (ourDogs.dogClothing)
    '''
    for doge in doges:
    #freeTime
        if user1.freeTime<2 && doge.activityLevel:
            #give 5 points to do with less
        elif userInput >2 and userInput <4:
            #
        else:
            print ("greater than 4")
    #alonetime
        if user1.alone=="yes" && doge.alone>50:
            #give 5 points to dog with more than 50
        elif user1.alone=="no"&& doge.alone<50:
            #give 5 points to dog with less than 50

        #exercise
        if user1.exercise <2 && doge.exerciseTime <=20:
            #give 3 points to dog with less than 20
        elif userInput >2 and userInput <5:
            print ("2 to 5")
        else:
            print ("more than 5")
        #allergies
        if allergies=="yes":
            print ("yes")
        else:
            print ("no")
        #money
        if money<200 :
            print ("less than 200")
        elif money>=200 and money <400:
            print ("200 to 400")
        else:
            print ("greater than 400")
        #children
        if children =="If they are behaved":
            print ("they are behaved")
        elif child

    print(user1.temperature)
    print(5)
    '''
def getFreeTime(freeTime):
    user1.freeTime=freeTime

def getAlone(alone):
    user1.alone=alone

def getExercise(exercise):
    user1.exercise=exercise

def getAllergies(allergies):
    user1.allergies=allergies
def getSalary(salary):
    user1.salary=salary
def getChildren(children):
    user1.children=children
def getReaction(reaction):
    user1.reaction=reaction
def getFatSkinny(fatSkinny):
    user1.fatSkinny=fatSkinny
def getPatience(patience):
    user1.patience=patience
def getTemperature(temperature):
    user1.temperature=temperature
def getGrooming(grooming):
    user1.grooming=grooming


if __name__ == '__main__':
    main()
