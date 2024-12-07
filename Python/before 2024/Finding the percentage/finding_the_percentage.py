if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
    	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
    query_name = input()
    mark = student_marks[query_name]
    marks = (sum(mark)/3)
    #print(format(sum(marks)/3,'.2f'))
    print(format((marks),'.2f'))



# name, *line = students score, name and the marks in one line
# students score should be in a line and float
# name are the values in Student_marks dict and scores are student_score
# student_marks = {name1:{scores1, scores2, ....}, name2{...}, ...}
