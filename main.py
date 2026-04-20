from pyscript import display, document # type: ignore

#This is the class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    #This is the format it will display
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

#This is the list of my classmates
class_mates = [
    Classmate("Ebtisam", "10-Ruby", "Math"),
    Classmate("Aeiou", "10-Ruby", "Science"),
    Classmate("Ethan", "10-Ruby", "Science"),
    Classmate("Koreen", "10-Ruby", "ICT"),
    Classmate("Jamie", "10-Ruby", "Music")
]

#This below is the function code for the add classmate button
def add_new_classmate(e):
    name = document.getElementById("nameInput").value
    section = document.getElementById("sectionInput").value
    subject = document.getElementById("subjectInput").value

    #The one below is the format that will be displayed once the user types in the name, section, and subject.
    if name and section and subject:
        new_student = Classmate(name, section, subject)
        class_mates.append(new_student)
        
        #Makes sure that there aren't any duplicates
        document.getElementById("nameInput").value = ""
        document.getElementById("sectionInput").value = ""
        document.getElementById("subjectInput").value = ""
        
        #Original list (not updated)
        render_list(None)

def render_list(e):
    #This will be displayed where I want it to be displayed.
    output_div = document.querySelector("#displayArea")
    output_div.innerHTML = ""
    
    #This is the looping code
    for student in class_mates:
        p = document.createElement("p")
        p.innerText = student.introduce()
        output_div.appendChild(p)

#Updated list with the user's inputs
render_list(None)