
''' types of arguments: Formal arguments and actual arguments'''


def function1(fruit_name):     # here fruit_name is formal argument
    print(f"{fruit_name} is a fruit")

function1("Apple")
function1("Mango")   #here Apple & Mango are actual arguments


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''types of actual arguments

 1 Positional arguments
- We must have to pass number of actual arguments equal to formal arguments as per sequence'''

def function2(first_name, sirname, age):
    print(f"Name:{first_name} {sirname}  Age: {age}" )
function2("ABC", "XYZ", 20)   
function2("DEF", "PQR", 25)   # here "ABC", "XYZ", 20 and "DEF", "PQR", 25 are positional arguments
          
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


'''

2 Default arguments
- Deafault arguments always comes after non-default arguments

'''
def family_member_names(first_name,middle_name, sirname = "XYZ"):    # here 'sirname' is default argument and first_name and middle_name are non-default arguments
    print(f"Name: {first_name} {middle_name} {sirname}")
family_member_names("AB", "CD")
family_member_names("LM", "CD")
family_member_names("PQ", "RS","PQR")     # we can also pass different value to change the value of default argument ahile calling the function
family_member_names("TU","VW", "ABC")   #  so here, we can pass min 2 args (no. of non-default arguments ) and max. 3 args (including default args)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''

3 Keyword arguments
- we can provide specific value as a keyword to an argument
- positional args follows keyword argument
'''

def national_symbols(flag, bird, animal, flower,):
    print(f'''Indian national symbols are:
National flag of India = {flag}
National bird of India = {bird}
Narional flower of India = {flower}
National animal of India = {animal}
''')
    
national_symbols(flag = "Tiranga", bird = "Peacock", flower = "Lotus", animal = "Tiger")  # here flag = "Tiranga", bird = "Peacock", flower = "Lotus", animal = "Tiger" are keyword args
#we can change sequence of keyword args with respect to formal args
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''

4 Variable length arguments
- we can pass any number of args (min 0 & max infinite)
- args can be any data (diff data types)
- it gives value of args in the form of tuple

'''

def function2(*n):
    print(n)
function2(100,200,300,400,500,600)          # variable length args of same datatypes
function2(10,20, "ABCD", [9,8,7], (1,2,3))   # variable length args of diff datatypes
function2()                                  #function with 0 variable length args


def function2(category,taste,*n):
    print(category, taste)
    print(n)
function2("fruits", "sweet", "watermelon", "banana", "mango")     #positional args follows variable length args
function2("desserts", "sweet","pudding", "pestries", "ice-cream")


def function2(*args, category,taste):
    print()                                                                   
    print(category, taste)
    print(args)
function2("grapes", "orange", "kiwi", category = "fruits", taste = "sour")    # Variable length args follows keyword args
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

'''
5. Keyword variable length argument
-we can pass any number of args (min 0 & max infinite)
- it gives value of args in the form of dictionary
'''
def function3(**args):
    print(args)
function3(a1 = 2, a2= 4, a3 = 6, a4 = 8, a5 = 10)   #same datatype
function3(a1= 2, a2 = "namrata", a3 = (9, 8, 7), a4= [])   #diff datatype


def function3(a, b,*n, **args):
    print()
    print(a,b)
    print(n)
    print(args)
function3(10,20,55, 65, 75, 25, a1 = 2, a2= 4, a3 = 6, a4 = 8, a5 = 10) #positional args follows keyword variable length args
# Variable length args follows keyword variable length args

