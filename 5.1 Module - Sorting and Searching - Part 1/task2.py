grades = []
for i in range(10):
    while True:
        user = int(input("Enter grade: "))
        if user >= 1 and user <= 12:
                grades.append(user)
                break
        else:
            print("Try again. Grades should be in range 1 - 12")

choice = int(input("""\nType number in bracket for
(1) Output grades
(2) Retake exam
(3) Whether the student will get a scholarship
(4) Output a sorted list of grades: in ascending order
(5) Output a sorted list of grades: in descending order\n"""))

sorted_grades = grades.copy()
sorted = False
while not sorted:
    sorted = True
    for i in range(len(sorted_grades)-1):
        if sorted_grades[i] > sorted_grades[i+1]:
            sorted = False
            sorted_grades[i], sorted_grades[i+1] = sorted_grades[i+1], sorted_grades[i]

if choice == 1:
    print(grades)
elif choice == 2:
    index = int(input("Index: "))
    new_grade = int(input("New Grade: "))
    grades[index] = new_grade
    print(grades)
elif choice == 3:
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print("Student will get Scholarship")
    else:
        print("Student will not get Scholarship!!!")

elif choice == 4:
    print(sorted_grades)
elif choice == 5:
    print(sorted_grades[::-1])
    