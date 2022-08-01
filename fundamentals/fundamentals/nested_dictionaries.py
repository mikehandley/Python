#1 Update Values in Dictionaries and Lists

#1.1 change the value 10 in x to 15
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
#Once you're done, x should now be [ [5,2,3], [15,8,9] ]

#1.2 change the last name of the first student from jordan to bryant
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
# print(students[0]['last_name'])
# print(students)

#1.3 change messi to andres
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

#1.4 change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30

#2 iterate through a list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

#iterateDictionary(students)
def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        output = ""
        for key,val in some_list[i].items():
            output += f"{key} - {val},"
        print(output)
#iterateDictionary(students)

#3 get value from a list of dictionaries
def iterateDictionary2(first_name, some_list):
    for i in range(0, len(some_list)):

        for key,val in some_list[i].items():
            if key == first_name:

                print(val) 

#iterateDictionary2('last_name', students)
def iterateDictionary2(last_name, some_list):
    for i in range(0, len(some_list)):

        for key,val in some_list[i].items():
            if key == last_name:

                print(val) 

#4 iterate through a dictionary with list values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print("-------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
printInfo(dojo)
#MJ THE GOAT!!!
