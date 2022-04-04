def factorial(n):
    result = 1
    for i in range(1, n+1):
       result = result * i
    return result

inp = input("Enter a number: ")
inp = int(inp)

print(f"The result is: {factorial(inp)}")