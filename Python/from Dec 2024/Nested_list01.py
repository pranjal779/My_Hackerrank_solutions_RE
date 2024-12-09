if __name__ == '__main__':
    for _ in range(int(input())):
        students = []   # Step1: Initialize an empty list
        name = input()  # Reading student's name 
        score = float(input())  # Reading's student's score
        students.append([name, score])  # Append as a sublist to students
        
        # Step2: Extract unique grades(score) and sort them
        unique_grades = sorted(set(grade for name, grade in students))
        
        # Step3: Identify the 2nd lowest score/grade
        second_lowest_grade = unique_grades[1]
        
        # Step4: Find the students with 2nd lowest grade
        second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
        
        # Step5: sort the students with 2nd lowest score/grade
        second_lowest_students.sort()
        
        # Step6: Print the names of each students in secod_lowest_students alphabetically
        for name in second_lowest_students:
            print(name)
