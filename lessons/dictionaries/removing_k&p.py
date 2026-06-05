#removing key and value pairs from dict
#pop(key):removes the item with the specified key name
#popitem():removes the last item
#del:removes anitem with specific key name
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop("first_name")
print(person)
print("---------")
person.popitem()
print(person)
print("---------")
del person["is_marred"]
print(person)
print("---------")
#item()=changes dict to list of tuples
print(person.items())
#clearing=if we dont want items in dict we can clear them
"""print(person.clear())"""
#deleting a dict= to completely dlt a  dict
#del person
#print(person)
#copy=we can avoid mutation of orginal dict
personn=person.copy()
print(personn)
#keys=it gives all the keys of a dict  as a list
print(person.keys())
#getting dict values in a list
print(person.values())

