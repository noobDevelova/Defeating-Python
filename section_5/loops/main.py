student_scores = [180, 124, 165, 173, 189, 169, 146]

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)