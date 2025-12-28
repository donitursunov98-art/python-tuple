students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]

subject = input('subject: ')
count = 0
for name, subjects in students:
    if subject in student[1]:
        count += 1

print(count)
       