grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_score = {}

students_list = sorted(list(students))

grades_count = [(sum(grades[0])/(len(grades[0]))), (sum(grades[1])/(len(grades[1]))), 
                (sum(grades[2])/(len(grades[2]))), (sum(grades[3])/(len(grades[3]))),
                (sum(grades[4])/(len(grades[4])))]

average_score.update({students_list[0]: grades_count[0],
                      students_list[1]: grades_count[1],
                      students_list[2]: grades_count[2],
                      students_list[3]: grades_count[3],
                      students_list[4]: grades_count[4]})

print(average_score)