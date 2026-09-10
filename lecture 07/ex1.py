survey_results = [
    ["Python","JavaScript", "C++"],
    ["Python","JavaScript", "C#"],
    ["Python","Java"],
    ["Python", "C++","JavaScript"],
    ["Python","JavaScript", "C++","Java"],
]

survey_set = [
    {"Python","JavaScript", "C++"},
    {"Python","JavaScript", "C++"},
    {"Python","JavaScript", "C++"}
]

choices_set = [set(day) for day in survey_results]
print(choices_set)

common_languages = set.intersection(*choices_set)
print("Languges chosen by all participants:",common_languages )

all_students = set.union(*choices_set)
absent_at_least_one_day = all_students - common_languages
print("Number of unique languages:",absent_at_least_one_day)

first_day_present = choices_set[0]
last_day_present = choices_set[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Languages chosen by exactly two participant:",first_day_but_not_last)

unique_students_count = len(all_students)
print("Participants with the same set of languages:",unique_students_count)