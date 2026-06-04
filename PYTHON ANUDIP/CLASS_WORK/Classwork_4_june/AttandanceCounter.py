#Problem Statement:Attandance counter
attandance_counter = 0
class_strength = 30
Student_preasent = True
while(attandance_counter<class_strength):
    if(Student_preasent):
        print("student Entered")
        print(" ")
        attandance_counter+=1
        print("Attandance counter:",attandance_counter)
        print(" ")
    else:
        break
