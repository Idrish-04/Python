empty={}
print(empty)
person={
    "first_name ":"Idrish",
    "last_name  ":"Katwara",
    "age ":18,
    "country":"India",
    'is_marred':"True",
    "skills":["Java","Node.js","python"],
    "address":{
        "street":"space street","zipcode ":389121
    }
}
print(person)
print(len(person))
print(person["first_name "])
print(person["address"]["street"])
print(person.get('first_name'))
person["job_title"]="DevOps"
print(person)