s  =  "1324"
s1 =  "pythön!"
s2 =  'adsv'
s3 = '''sfdgfbabbababababa'''
s4="XDDXDFCVF"
s5="XDDX\tDFC\tVF"
print(s,s2,s3)
#length Function
print(len(s),len(s2),len(s3))
#index Function
print(s.index("3"))
#Count Function
print(s3.count('b'))
#Slice in Strings
print(s3[1:12:2]) #initial:Ending:Skipping Character
#inverse the string
print(s3[::-1])
#Upper & Lower Character
print(s2.upper())
#title
print(s4.title())
#endswith
print(s3.endswith("2"))
#Capitalize
print(s4.capitalize())
#CASEFOLD
print(s4.casefold())
#Center in String
print(s.center(13,"*"))
#encode in string
print(s1.encode())  # default UF8
#Expand Tabs
print(s5.expandtabs(3))
#Find index of letter in Python
print(s4.find('FC'))
#Alpha-Numeric
print(s3.isalnum())
# Join in Python
print(s.join('243'))
#split in Python
print(s3.split("b"))





