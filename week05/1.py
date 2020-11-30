exam_score = []
total_score = 0
num = int(input("Enter number of students: "))

print("\nEnter score for -")

i=0
while i < num:
    print("Student", (i+1), ":")
    score = int(input())
    exam_score.append(int(score))
    i+=1

print("\nScores entered for -")

z = 0

while z < num:
    print("Student", (z+1), ":", exam_score[z])
    total_score+=exam_score[z]
    z += 1

print("\nAverage marks for", num, "students:", total_score/num)
