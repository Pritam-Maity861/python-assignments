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

class StudentResultAnalyzer:
    def __init__(self, students):
        self.students = students

    def average_marks(self):
        avg_marks_of_students = []
        for student in self.students:
            avg_mark = sum(student["marks"]) / len(student["marks"])
            name = student["name"]

            print(f"Average marks for {name} is : {avg_mark}")

            avg_marks_of_students.append({
                name: avg_mark
            })

        return avg_marks_of_students

    def determine_pass_fail(self):
        list_of_pass_fail = []
        for student in self.students:
            avg_mark = sum(student["marks"]) / len(student["marks"])
            name = student["name"]

            if avg_mark >= 50:
                isPass = "Pass"
            else:
                isPass = "Fail"

            print(f"{name} -> Status : {isPass}")

            list_of_pass_fail.append({
                name: isPass
            })
        return list_of_pass_fail

    def find_topper(self):
        highest_mark = -1
        topper = ""
        for student in self.students:
            avg_mark = sum(student["marks"]) / len(student["marks"])
            name = student["name"]

            if avg_mark > highest_mark:
                highest_mark = avg_mark
                topper = name

        print(f"Topper : {topper}")
        print(f"Topper average : {highest_mark}")
        return topper


    def find_lowest_performing_student(self):
        lowest_mark = 101
        lowest_student = ""
        for student in self.students:
            avg_mark = sum(student["marks"]) / len(student["marks"])
            name = student["name"]
            if avg_mark < lowest_mark:
                lowest_mark = avg_mark
                lowest_student = name
        print(f"Lowest performing student : {lowest_student}")
        print(f"Lowest average : {lowest_mark}")

        return lowest_student


    def calculate_class_avg(self):
        total_avg = 0
        for student in self.students:
            avg_mark = sum(student["marks"]) / len(student["marks"])
            total_avg += avg_mark
        class_avg = total_avg / len(self.students)
        print(f"Class average : {class_avg}")
        return class_avg


students = [
    {"name": "Tarun", "marks": [80, 72, 91]},
    {"name": "Ashmita", "marks": [65, 88, 79]},
    {"name": "Alinda", "marks": [80, 72, 91]},
    {"name": "Pritam", "marks": [79, 41, 26]},
    {"name": "Anirban", "marks": [81, 91, 31]},
]

analyzer = StudentResultAnalyzer(students)

print("\naverage marks:")
avg_marks_list = analyzer.average_marks()
print(avg_marks_list)


print("\npass or fail")
pass_fail_status = analyzer.determine_pass_fail()
print(pass_fail_status)


print("\n topper name ")
topper_student = analyzer.find_topper()
print(topper_student)


print("\n lowest performing student")
lowest_student = analyzer.find_lowest_performing_student()
print(lowest_student)


print("\n class avg")
class_avg = analyzer.calculate_class_avg()
print(class_avg)
