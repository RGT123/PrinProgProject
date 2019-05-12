class doggie:
    def __init__(self, time, alone, exerciseTime, allergies, salary, children, personality, size, dentistTime, temperature, dogClothing):
        self.time=time
        self.alone=alone
        self.exerciseTime=exerciseTime
        self.allergies=allergies
        self.salary=salary
        self.children=children
        self.personality=personality
        self.size=size
        self.dentistTime=dentistTime
        self.temperature=temperature
        self.dogClothing=dogClothing
        self.points = 0
        
    def printinfo(self):
        print("Activity Level: "+self.time)
        print("Tolerates alone: "+self.alone)
        print("Exercise Needs: "+self.exerciseTime)
        print("Allergies: "+self.allergies)
        print("Cost: "+self.salary)
        print("Kid friendly: "+self.children)
        print("Home reaction: "+self.personality)
        print("Size: "+self.size)
        print("Trainability: "+self.dentistTime)
        print("Tolerates cold weather: "+self.temperature)
        print("Grooming Needs: "+self.dogClothing)

