i = 0
score = []
total = 0

while i < 10:
    marks = int(input("Judge "+str(i+1)+": "))
    if marks < 0 or marks > 10:
        print("Out of range")
        continue

    score.append(marks)
    i += 1

print()

for x in range(len(score)):
    print("Judge ", x+1, ": ", score[x])
    total += score[x]

print("Total Score: ", total)
print("Average: ", (total/i))
