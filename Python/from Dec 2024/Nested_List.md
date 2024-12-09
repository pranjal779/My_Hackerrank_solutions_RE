Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade. 

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
records = [["chi",20.0],["beta",50.0],["alpha",50.0],]


The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0. 
There are two students with that score: ["beta","alpha"]. Ordered alphabetically, the names are printed as: 

alpha
beta
Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines. 
- The first line contains a student's name.
- The second line contains their grade.

Constraints
- 2<=N<=5 
- There will always be one or more students having the second lowest grade. 
Output Format

Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list: 

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
 so we order their names alphabetically and print each name on a new line.


---

### **Steps**

1. Initialize an empty list to store the names and scores:
   ```python
   students = []
   ```

2. Use the provided `for` loop to read each student's data:
   - Append each name and score as a sub-list to `students`.

3. Follow the logic to:
   - Extract unique grades.
   - Identify the second lowest grade.
   - Find names of students with the second lowest grade.
   - Sort these names alphabetically and print them.

---

### **Completed Code**
```python
if __name__ == '__main__':
    students = []  # Step 1: Initialize an empty list
    for _ in range(int(input())):  # Read number of students
        name = input()  # Read student's name
        score = float(input())  # Read student's score
        students.append([name, score])  # Append as a sublist to `students`

    # Step 2: Extract unique grades and sort
    unique_grades = sorted(set(grade for name, grade in students))
    
    # Step 3: Identify the second lowest grade
    second_lowest = unique_grades[1]

    # Step 4: Find students with the second lowest grade
    second_lowest_students = [name for name, grade in students if grade == second_lowest]

    # Step 5: Sort names alphabetically
    second_lowest_students.sort()

    # Step 6: Print each name
    for name in second_lowest_students:
        print(name)
```

---

### **Explanation**
1. **Reading Input**:
   - The `for` loop provided is used to collect `N` students' names and scores.
   - Each `[name, score]` is stored as a sublist in `students`.

2. **Finding Unique Grades**:
   - Extract grades using a generator expression: `grade for name, grade in students`.
   - Use `set()` to get unique grades, then sort them.

3. **Identifying Second Lowest Grade**:
   - The second element of the sorted `unique_grades` list is the second lowest grade.

4. **Filtering Students**:
   - Use a list comprehension to collect names of students whose grades match the second lowest grade.

5. **Sorting and Printing**:
   - Sort the names alphabetically and print them.

---

### **Example Walkthrough**

**Input**:
```plaintext
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

1. **Collected Data**:
   ```python
   students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
   ```

2. **Unique Grades**:
   ```python
   unique_grades = [37.2, 37.21, 39, 41]
   ```

3. **Second Lowest Grade**:
   ```python
   second_lowest = 37.21
   ```

4. **Students with Second Lowest Grade**:
   ```python
   second_lowest_students = ['Harry', 'Berry']
   ```

5. **Sorted Names**:
   ```python
   second_lowest_students.sort()  # ['Berry', 'Harry']
   ```

**Output**:
```plaintext
Berry
Harry
```

---

it's an important concept in Python list comprehensions and how data structures like lists are used.

### Why `grade for name, grade in students` Works

The key lies in understanding how **list destructuring (unpacking)** works in Python.

#### **Breaking It Down:**
When we write:
```python
students.append([name, score])
```
We are appending a list `[name, score]` into the `students` list. For example:
```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2]]
```

#### **List Unpacking in `for name, grade in students`:**
When iterating over `students`, **each element** (which is a sublist like `['Harry', 37.21]`) is **unpacked** into two variables: `name` and `grade`.

Here's how it works:
```python
for name, grade in students:
    # 'name' gets the first element of the sublist (e.g., 'Harry')
    # 'grade' gets the second element of the sublist (e.g., 37.21)
```

This unpacking is the same as:
```python
sublist = ['Harry', 37.21]
name, grade = sublist
# name -> 'Harry'
# grade -> 37.21
```

---

### Application in Your Doubts

1. **`unique_grades = sorted(set(grade for name, grade in students))`:**
   - The `for name, grade in students` part unpacks each sublist.
   - `grade` refers to the second element of each sublist.
   - The generator expression `(grade for name, grade in students)` yields only the grades.
   - `set()` collects unique grades, and `sorted()` organizes them in ascending order.

   **Example**:
   ```python
   students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2]]
   grades = (grade for name, grade in students)  # Yields: 37.21, 37.21, 37.2
   unique_grades = sorted(set(grades))  # Result: [37.2, 37.21]
   ```

2. **`second_lowest_students = [name for name, grade in students if grade == second_lowest]`:**
   - The `for name, grade in students` again unpacks each sublist.
   - `name` refers to the first element of the sublist.
   - The condition `if grade == second_lowest` checks if the second element of the sublist matches `second_lowest`.
   - If the condition is true, only the `name` is included in the list comprehension.

   **Example**:
   ```python
   second_lowest = 37.21
   students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2]]
   second_lowest_students = [name for name, grade in students if grade == second_lowest]
   # Iteration:
   # 'Harry', 37.21 -> Matches -> Add 'Harry'
   # 'Berry', 37.21 -> Matches -> Add 'Berry'
   # 'Tina', 37.2   -> Doesn't Match -> Skip
   # Result: ['Harry', 'Berry']
   ```

---

### Why It Works in Lists but Isn’t Explicitly a Dictionary
You're right that a dictionary (e.g., `{'Harry': 37.21}`) explicitly maps keys to values. However, with nested lists like `[['Harry', 37.21], ...]`, Python's **unpacking** provides a similar mechanism when iterating.

This behavior is a feature of Python's ability to destructure sequences. It works because each sublist has exactly **two elements**, so Python knows how to split them into two variables (`name` and `grade`).

---

### Comparison with Dictionaries
If `students` were a dictionary:
```python
students = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2}
```
You would write:
```python
grades = students.values()  # To get all grades
second_lowest_students = [name for name, grade in students.items() if grade == second_lowest]
```
But because we’re using lists, unpacking allows the same logic without requiring explicit keys.

---

### Recap
1. **Unpacking Works on Lists with Fixed-Length Elements**: Each sublist `[name, score]` is unpacked into `name` and `grade` when iterating.
2. **`for name, grade in students` Unpacks Elements**: Python splits each sublist into two parts automatically.
3. **List Comprehensions Leverage This**: We extract just the data we need (names or grades) by iterating and filtering using conditions.

😊
