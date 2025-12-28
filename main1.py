people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

max_old_people = people[0]

for person in people:
    if person[1] > max_old_people[1]:
        max_old_people = person


print(max_old_people)
