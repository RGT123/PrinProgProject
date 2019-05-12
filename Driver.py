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
    #print (ourDogs['breed0'].temperature)


    for dog in ourDogs:
    #freeTime
        if int(user1.freeTime)<2 and ourDogs[dog].time=="low":
            ourDogs[dog].points+=5
        elif int(user1.freeTime) >=2 and int(user1.freeTime)<4 and ourDogs[dog].time=="moderate":
            ourDogs[dog].points+=5
        else:
            ourDogs[dog].points+=5

    #alonetime
        if user1.alone=="yes" and int(ourDogs[dog].alone[0])>2:
            ourDogs[dog].points+=5
        else:
            ourDogs[dog].points += 5

    #exercise
        if int(user1.exercise) <2 and int(ourDogs[dog].exerciseTime[0]) < 2:
            ourDogs[dog].points+=3

            #give 3 points to dog with less than 20
        elif int(user1.exercise) >=2 and int(user1.exercise) <=5 and int(ourDogs[dog].exerciseTime[0]) <=4:
            ourDogs[dog].points+=3
        else:
            ourDogs[dog].points+=3
    #allergies
        if user1.allergies=="yes" and int(ourDogs[dog].allergies)<4:
            ourDogs[dog].points+=4
        else:
            ourDogs[dog].points+=4
    #money
        if int(user1.salary)<200 and int(ourDogs[dog].salary[0]) <2 :
            ourDogs[dog].points+=4
        elif int(user1.salary) <400 and int(ourDogs[dog].salary[0]) <4:
            ourDogs[dog].points+=4
        else:
            ourDogs[dog].points+=4
    #children
        if (user1.children =="I love kids" or user1.children == "I don't mind them") and ourDogs[dog].children=="often":
            ourDogs[dog].points+=2
        elif (user1.children =="If they are behaved" or user1.children == "I hate kids") and ourDogs[dog].children=="sometimes":
            ourDogs[dog].points+=2
    #reaction
        if user1.reaction == "Excited" and int(ourDogs[dog].personality)>=4:
            ourDogs[dog].points+=3
        elif user1.reaction == "Curious" and int(ourDogs[dog].personality)==3:
            ourDogs[dog].points+=3
        elif user1.reaction == "Calm" and int(ourDogs[dog].personality)==2:
            ourDogs[dog].points+=3
        else:
            ourDogs[dog].points+=3
    #fatskinny
        if user1.fatSkinny == "I don't mind":
            ourDogs[dog].points+=2
        elif user1.fatSkinny == "Skinny" and int(ourDogs[dog].size[0])<=2:
            ourDogs[dog].points +=2
        elif user1.fatSkinny == "Fat" and int(ourDogs[dog].size[0]) >=4:
            ourDogs[dog].points+=2

    #patience
        if (user1.patience == "Leave after 10 minutes" or user1.patience== "Leave after 20 minutes") and ourDogs[dog].dentistTime=="moderate":
            ourDogs[dog].points+=2
        else:
            ourDogs[dog].points+=2

    #temperature
        if int(ourDogs[dog].temperature) >=4:
            ourDogs[dog].points+=3
        elif int(user1.temperature) <40 and int(ourDogs[dog].temperature) ==3:
            ourDogs[dog].points+=3
        elif int(user1.temperature)  <60 and int(ourDogs[dog].temperature)==2:
            ourDogs[dog].points+=3
        else:
            ourDogs[dog].points+=3

    #grooming
        if user1.grooming=="I think that's dumb" and int(ourDogs[dog].dogClothing[0])==1:
            ourDogs[dog].points+=2
        elif user1.grooming== "If it's cheap" and int(ourDogs[dog].dogClothing[0])<=3:
            ourDogs[dog].points+=2
        else:
            ourDogs[dog].points +=2

    maxpoints=0
    key=""
    for dog in ourDogs:
        if ourDogs[dog].points>maxpoints:
            maxpoints=ourDogs[dog].points
            key=dog

    return key


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
