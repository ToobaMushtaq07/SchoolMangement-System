class Person:

    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_person(self):
        print("\nPerson Details")
        print(f"ID   : {self.person_id}")
        print(f"Name : {self.name}")