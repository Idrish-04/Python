person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# print the middle skill
if "skills"in person:
    skills=person["skills"]
    middle_skills=skills[len(skills)//2]
    print("Middle skills: ",middle_skills)
#check if python in skills
if "skills" in person:
    print("Python" in person["skills"])
#determine dev title
skills=person['skills']
if skills==["Javascript","React"]:
    print("He is a front end DEV")
elif all(skill in skills for skill in ["Node","Python","MondoDB"]):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")

else:
    print("unknown title")
