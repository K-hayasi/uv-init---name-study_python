def fizz_buzz(n):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz") 
    else:
        print(str(n)) 

fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(4)
fizz_buzz(5)
fizz_buzz(11)
fizz_buzz(12)
fizz_buzz(15)
fizz_buzz(16)

def fizz_buzz(n, x, y):
    if n % x == 0 and n % y == 0:
        print("FizzBuzz")
    elif n % x == 0:
        print("Fizz")
    elif n % y == 0:
        print("Buzz") 
    else:
        print(str(n)) 

fizz_buzz(3, 3, 5)
fizz_buzz(5, 3, 5)
fizz_buzz(16, 3, 5)
