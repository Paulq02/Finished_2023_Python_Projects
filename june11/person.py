class Person:

    def __init__(self,name,age,gender) -> None:
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print(f"Hi my name is {self.name} I'm {self.age} year old {self.gender}")
    

person_1=Person("Paul",37,"male")
person_1.introduce()