it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[6])
it_companies.append('Twitter')
print(it_companies)
it_companies.insert(3, 'Tesla')
print(it_companies)
#uppercase one of the companies
it_companies[0] = it_companies[0].upper()
print(it_companies)
#join the companies with a string '#;  '
joined_companies = '  #;  '.join(it_companies)
print(joined_companies)
#check if a certain company exists in the list
print('Apple' in it_companies)
#sort the list using sort() method
it_companies.sort()
print(it_companies)
#reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#slice out the first 3 companies
print(it_companies[:3])
#slice out the last 3 companies
print(it_companies[-3:])
#slice out the middle company or companies
middle=len(it_companies)//2
print(len(it_companies))
print(it_companies[middle])
#remove the first company from the list
it_companies.pop(0)
print(it_companies)
#remove the middle company or companies from the list
it_companies.pop(middle)
print(it_companies)
#remove the last company from the list  
it_companies.pop()
print(it_companies)
#clear the list
it_companies.clear()
print(it_companies)
