if __name__ == '__main__':
    students = []  # Initialize the list for storing [name, grade]
    for _ in range(int(input())):  # Read number of students
        name = input()  # Read student's name
        score = float(input())  # Read student's score
        students.append([name, score])  # Append [name, score] to students list
    
    # Extract unique grades and find the second lowest
    unique_grades = sorted(set(grade for name, grade in students))
    second_lowest = unique_grades[1]  # Second lowest grade
    
    # Get all students with the second lowest grade
    second_lowest_students = sorted(name for name, grade in students if grade == second_lowest)
    
    # Print each name
    for name in second_lowest_students:
        print(name)
