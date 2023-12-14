#CTI-110
#P4HW1 - Score List
#Raven Sullivan
#11/09/2023
#
scores_amount = int(input("How many scores do you want to enter? "))

collected_scores = []
valid_score = True
score_number = 0
while score_number < scores_amount:
  
    if (valid_score):
        score = int(input(f"Enter score #{len(collected_scores) + 1}: "))
    else:
        score = int(input(f"Enter score #{len(collected_scores) + 1} again: "))
   
    if score in range(101):
        collected_scores.append(score)
        valid_score = True
        score_number += 1
    else:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        valid_score = False
        continue

print("----------------Results----------------")
print(f"Lowest Score   : {min(collected_scores):.1f}")

collected_scores.remove(min(collected_scores))

print(f"Modified List  : {collected_scores}")

score_sum = sum(collected_scores)
score_average = score_sum / len(collected_scores)

print(f"Scores Average : {score_average:.2f}")


if score_average >= 90:
    letter_grade = 'A'
elif score_average >= 80:
    letter_grade = 'B'
elif score_average >= 70:
    letter_grade = 'C'
elif score_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Grade          : {letter_grade}")
print("---------------------------------------")
