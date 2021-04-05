        #to add text to a function 
        # when its returning another part of the class
        # (f{"I can talk! "}self.name)

class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
       

    def talk(self):
        #message = "I can talk!"
        return "I can talk!"


    # def say_favourite_language(self, language):
    #     return self.language