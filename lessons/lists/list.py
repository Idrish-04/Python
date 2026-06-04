"""l=list()
print(l)
print(len(l))
l=[]
print(len(l))
#unpacking list
fruits=["banana", "orange", "mango", "lemon"]
first, second  ,*rest,fourth=fruits
print(first)
print(second)

print(rest)
print(fourth)"""
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
i, fr, bg, sw, *rest, es = countries
print(i) 
print(fr)
print(bg)
print(sw)
print(rest)
print(es)
