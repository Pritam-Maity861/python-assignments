'''
1. Student Result Analyzer 
Create a program that accepts multiple students: 
students = [ 
{"name": "Tarun", "marks": [80, 72, 91]}, 
{"name": "Ashmita", "marks": [65, 88, 79]}, 
{"name": "Alinda", "marks": [35, 42, 38]}, 
{"name": "Pritam", "marks": [79, 41, 26]}, 
{"name": "Anirban", "marks": [81, 91, 31]}, 
] 
Create functions to: 
● Calculate average marks 
● Determine PASS/FAIL 
● Find the topper 
● Find the lowest-performing student 
● Calculate class average 

'''

'''
Functional Approach
'''

def average_marks(studentsList:list[dict]):
    avg_marks_of_students=[]
    for student in studentsList:
        avg_mark=sum(student["marks"])/len(student["marks"])
        name=student["name"]
        print(f"Average marks for {name} is : {avg_mark}")
        avg_marks_of_students.append({name: avg_mark})
    return avg_marks_of_students



def determine_pass_fail(studentsList:list[dict]):
    list_of_pass_fail=[]
    for student in studentsList:
        avg_mark=sum(student["marks"])/len(student["marks"])
        name=student["name"]
        if avg_mark>=50:
            isPass="Pass"
        else:
            isPass="Fail"

        print(f"{name} -> Status : {isPass}")
        list_of_pass_fail.append({name: isPass})
    return list_of_pass_fail



def find_topper(studentsList:list[dict]):
    highestMark=0
    TopperList=[]
    for student in studentsList:
        avg_mark=sum(student["marks"])/len(student["marks"])
        name=student["name"]
        if avg_mark>=highestMark:
            highestMark=avg_mark
            TopperList.append(name)
            
    print(f"Topper list : {TopperList}")
    return TopperList



def find_lowest_performing_student(studentsList:list[dict]):
    lowestMark=100.0
    lowest_student =""
    for student in studentsList:
        avg_mark=sum(student["marks"])/len(student["marks"])
        name=student["name"]
        if avg_mark<lowestMark:
            lowestMark=avg_mark
            lowest_student =name
            
    print(f"Lowest performig students list : {lowest_student }")
    return lowest_student 



def calculate_class_avg(studentsList:list[dict]):
    total_avg =0
    class_avg =0
    for student in studentsList:
        avg_mark=sum(student["marks"])/len(student["marks"])
        total_avg+=avg_mark
    
    class_avg=total_avg/len(studentsList)
        
            
    print(f"class avg : {class_avg}")
    return class_avg 



students = [ 
{"name": "Tarun", "marks": [80, 72, 91]}, 
{"name": "Ashmita", "marks": [65, 88, 79]}, 
{"name": "Alinda", "marks": [80, 72, 91]}, 
{"name": "Pritam", "marks": [79, 41, 26]}, 
{"name": "Anirban", "marks": [81, 91, 31]}, 
] 


avg_marks_list=average_marks(students)
print(avg_marks_list)

pass_fail_status=determine_pass_fail(students)
print(pass_fail_status)

Topper_student_list=find_topper(students)
print(Topper_student_list)

Lowwest_performing_student_list=find_lowest_performing_student(students)
print(Lowwest_performing_student_list)

class_avg=calculate_class_avg(students)
print(class_avg)
