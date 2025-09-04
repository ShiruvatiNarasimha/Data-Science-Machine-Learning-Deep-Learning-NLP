## Arithmetic Operators


a = 10
b = 15

add_result = a + b
subtract_result = a -b
multiply_result = a * b
divide_result = a / b
modulus_result = a % b
exponent_result = a ** b


print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)
print(modulus_result)
print(exponent_result)





## Comparison Operators
x = 10
y = 10

x = y



## Not Equal Operator

str3 = "shiruvati"
str4 = "shiruvati"

str3!=str4



## greater than

num1 = 45
num2 = 55

num1>num2




## Logic operators



## And, Not, Or


P = True
U = True

result = P and U
print(result)

P = False
U = False

result2 = P or   U
print(result2)




## if statement


age = 20

if age>=18:
    print("You are allowed to vote in the election")





    ##  else 

age = 16

if age>=18:
    print("You are eligible for voting")
else:
    print("You are a minor")    






## elif

age = 18

if age<13:
    print("You are child")
elif age<=18:
    print("you are a teenager")    
else:
    print("You are an adult")





## Nested Loop

num=int(input("Enter the number"))

if num>0:
    print("The number is Positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")    
else:
    print("The number is Zero or negative")        