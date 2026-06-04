#concatination
s="Thirty"
s2="Days"
s3="Of"
s4="Python"
r=s+" "+s2+" "+s3+" "+s4
print(r)
company="coding for all"
print(company)
length=len(company)
print(length)
upper=company.upper()
print(upper)
capitalized=company.capitalize()
print(capitalized)
swapped=company.swapcase()
print(swapped)
title=company.title()
print(title)
slice=company.split()[2]
print(slice)
replace=company.replace("coding", "Python")
print(replace)
a="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" #split string by comma and space
companies=a.split(", ")
print(companies)
#last index of coding for all
c=len(company)-1
print(c)
print(company.rfind('l'))
print(company[10])