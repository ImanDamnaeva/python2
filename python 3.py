#An action committed in anger is an action doomed to failure. - Dschingis Khan
famous_quotes ='"An action committed in anger is an action doomed to failure."'
print("Dschingis Khan once said", str(famous_quotes))

def number_eight():
    print(5+3)
    print(10-2)
    print(4*2)
    print(16/2)

number_eight()

def name_age():
    name = input('Enter your name:')
    age = int(input('Enter your age:'))
    print('Hello, ' + name + ' . You are ' + str(age) + ' years old.')
    print('Hello, {}. You are {} years old.'.format(name, int(age)))
    print(f'Hello, {name}. You are {age} years old.')

name_age()

def swap_integers():
    x = 25
    y = 50
    temp = x
    x = y
    y = temp
    print('x after swapping:', x)
    print('y after swapping:', y)
swap_integers()

def check_numbers(number1, number2):
    divisible_by_6 = (number1 % 6 == 0) or (number2 % 6 == 0)
    divisible_by_10 = (number1 % 10 == 0) and (number2 % 10 == 0)

    if divisible_by_6:
        print('One number is divisible by 6')
    else:
        print('Neither number is divisible by 6')

    if divisible_by_10:
        print('Both numbers are divisble by 10')
    else:
        print('At least one number is not divisible by 10')

    return divisible_by_6 and divisible_by_10

number1 = 6
number2 = 10
print("Number 1:", number1)
print("Number 2:", number2)
result = check_numbers(number1, number2)
print("Function returned:", result)

def sum_up(number1, number2):
    if number2 <= number1:
        print("Error: The second number should ne greater than the first")
        return None

    result = sum(range(number1, number2 +1))
    return result

number1 = 3
number2 = 9
print('The sum of integers between', number1, 'and' , number2, 'is', sum_up(number1, number2))


def sequence (number):
    if not 0 <= number <= 9:
        print("Error: The number should be a integer between 0 and 9")
        return

    for i in range(10):
        if i != number:
            print(i , end= " ")

sequence(5)

def check_string (text):
    text_lower = text.lower()

    if text_lower.startswith("a") or text_lower.endswith ("a"):
        return True
    else:
        return False

result1 = check_string('Apple')
print(result1)
result2 = check_string('banana')
print(result2)
result3 = check_string('orange')
print(result3)

def triangle(rows):
    for i in range(1, rows +1):
        print(""* (rows - i), end="")
        print("* " * i)

triangle(4)