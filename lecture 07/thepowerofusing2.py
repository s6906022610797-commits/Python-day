attendanue_week = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eve"],
    ["Bob", "Charlie", "David"]
]
attendanue_sets = [
    {"Alice", "Bob", "Charlie"},
    {"Alice", "David", "Charlie"},
    {"Bob", "David", "Eve"}
]
attendanue_sets = [set(day) for day in attendanue_week]
print(attendanue_sets)

present_every_day = set.intersection(*attendanue_sets)
print("Present every day:", present_every_day)

all_students = set.union(*attendanue_sets)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:")