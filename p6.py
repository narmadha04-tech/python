#Write a class Student. Use exception handling to read the data of a student.
class Student:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.rollno = ""
        self.percent = ""
        
    def get_input(self):
        while True:
            try:
                name=input("Name:")
                year=int(input("Year of Study(in number):"))
                rollno=input("Rollno:")
                percent=input("Percentage(till current sem in numbers):")
                
                if not name.isalpha():
                 raise Exception("Name is not a string.")
                if year<1 or year>3:
                    raise Exception("Incorrect year of study.")
                if not rollno.isalnum() or len(rollno)!=8:
                    raise Exception("Provide valid Roll no.")
                if not percent.isdigit() or '%' in percent:
                    raise Exception("Invalid or Percentage should not contain symbol.")
                else:
                    self.name = name
                    self.year = year
                    self.rollno = rollno
                    self.percent = percent

                    print("All inputs are valid!")
                    break
                
            except Exception as e:
                print(e)

    def display(self):
        print("\n--- Student Details ---")
        print("Name      :", self.name)
        print("Year      :", self.year)
        print("Roll No   :", self.rollno)
        print("Percentage:", self.percent)

s = Student()
s.get_input()
s.display()


   
        
        
            
        
        
        
