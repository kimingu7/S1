score = {
'python': 85,
'django': 89,
'web': 83,
'algorithm' : 90
}
sum_score = 0
for i in score:
    sum_score = sum_score + score[i]
avg_score = sum_score / len(score)
print(avg_score)