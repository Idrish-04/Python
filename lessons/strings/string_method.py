"""a="I am newbie and i have    stared    thirty days of python"
print(a.capitalize())
print(a.count("a",1,30))
challenge = 'thirty days of python'
print(challenge.count('y', 7, 14))
#endwith
print(challenge.endswith('on'))
print(challenge.endswith('tion'))
#expandtabs
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))
#find
print(a.find("a"))
print(a.format(a))"""
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.strip("thiaon"))
split_string = challenge.split()
print(split_string)
print(challenge.split('y'))
print(challenge.rsplit('y', 1))