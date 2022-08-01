num1 = 42 #variable declaration
num2 = 2.3 # variable declaration
boolean = True # Boolean
string = 'Hello World'# Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary,
fruit = ('blueberry', 'strawberry', 'banana') #Tuple
print(type(fruit)) #type check #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value
print(person['name'])#access value
person['name'] = 'George'#change value
person['eye_color'] = 'blue'#add value
print(fruit[2]) #acess value, log statement

if num1 > 45: #if. conditional
    print("It's greater") #log statement
else: #else, condtional
    print("It's lower") #log statement

if len(string) < 5:#length check, conditional
    print("It's a short word!")#log statement
elif len(string) > 15: #else if, condtional
    print("It's a long word!") #log statement
else: # else, condtional
    print("Just right!") #log statement

for x in range(5):#sequence
    print(x) #log statement
for x in range(2,5):#sequence
    print(x) #log statement
for x in range(2,10,3): #sequence
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while loop
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() # delete value
pizza_toppings.pop(1) # delete value sausage

print(person) #log statement
person.pop('eye_color') #delete value,
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #start
        continue #continue
    print('After 1st if statement') #sequence
    if topping == 'Olives': #conditional, if
        break  #for loop, break

def print_hello_ten_times(): #function, argument
    for num in range(10): # parameter
        print('Hello') #return

print_hello_ten_times() #Log statement

def print_hello_x_times(x): #function, argument
    for num in range(x): # parameter
        print('Hello') #return

print_hello_x_times(4)  #log statement

def print_hello_x_or_ten_times(x = 10): #function, argument
    for num in range(x): #parameters
        print('Hello') #return

print_hello_x_or_ten_times() #return
print_hello_x_or_ten_times(4) # return


"""  #good to relearn and refresh on these concepts
Bonus section 
"""

# print(num3)
# num3 = 72 
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)