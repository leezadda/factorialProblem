def factorial(number):
    value = 1
    for i in range(1, number + 1):
        value = value * i
    return value

# Write the definition and implementation of the combinatorial_number function here:
def combinatorial_number(m,n):
    num = (factorial(m))/(factorial(n)*(factorial(m-n)))
    return num

# Main Program (DO NOT MODIFY THIS SECTION OF THE CODE)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
result = combinatorial_number(m,n)
print ("The combinatorial number value is:",int(result))