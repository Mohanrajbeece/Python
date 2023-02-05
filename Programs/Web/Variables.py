#defining class variables
class Studentdata:
    #class Variables
    collage= "PSNA Engineering collage"
    Location="palani road Dindigul"
    
    # constructor method with instance variable [must have 'self' keyword as first parameter]
    def __init__(self,name,age):
        #instance variables
        self.name1=name
        self.age=age
# normal method with instance variable percentage
    def studentpercentage(self,percentage):
      print("This student got" + str(percentage) + "% of marks in UG")
      
#Defining method
def student_data():
    # first object, setting up instance variables of constructor method
    student1=Studentdata("mohan" , 23)
    
if __name__ == "__main__":
    student_data()