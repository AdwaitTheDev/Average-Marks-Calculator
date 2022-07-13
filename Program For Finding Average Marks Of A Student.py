Maths = int(input('Enter Marks Scored In Maths:'))
Science = int(input('Enter Marks Scored In Science:'))
SST = int(input('Enter Marks Scored In SST:'))
English = int(input('Enter Marks Scored In English:'))
French = int(input('Enter Marks Scored In French:'))

total_marks = Maths + Science + SST + English + French
total_subjects = 5
average_marks = total_marks/total_subjects

print('Average Marks Scored:', average_marks)
