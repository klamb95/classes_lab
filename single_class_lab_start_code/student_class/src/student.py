

class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
       

    def talk(self):
        #message = "I can talk!"
        return "I can talk!"


    def say_favourite_language(self, language):
        return (f"I love {language}")