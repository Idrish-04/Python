text="coding for all"
acronym="".join(word[0] for word in text.split( ))
print(acronym)
split_text=text.split()
print(split_text)
print(text.index("c"))
print(text.index("f"))
text2="coding for all people"
rfind=text2.rfind("l")
print(rfind)
sent="you cannot end a sentence with because because because is a conjunction"
print(sent.index("because"))
print(sent.rindex("because"))
print(sent.find("because"))
slice=sent[31:54]
print(slice)
#position of first occurrence of because
position=sent.find("because")
print(position)
# does coding for all start with coding
print(text.startswith("coding"))
# does coding for all end with coding   
print(text.endswith("coding"))
#removing left nd right trailing spaces
text3="   coding for all   "
print(text3.strip())
#ididentifier
identifier="30DaysOfPython"
print(identifier.isidentifier())
identifier2="thirty_days_of_python"
print(identifier2.isidentifier())
#['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] joining list with hash
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
formated_string=" # ".join(python_libraries)
print(formated_string)
#newline esc seq
para="I am enjoying this challenge.\nI just wonder what is next."
print(para)
#use tab
para2="Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(para2)
