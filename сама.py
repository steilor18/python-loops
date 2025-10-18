def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            print("Эм, ну вообще-то это не число")
def get_operation():
    message = '''
Что будем делать?:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
Ваш выбор:
'''
    correct_operations = '+-/*'
    operation = input(message)
    while operation not in correct_operations:
        print("Эм, ну я такое делать не умею")
        operation = input(message)
    return operation
def calculate(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Ну, если ты не знал, то деление ноль запрещено"
    elif operation == '*':
        result = num1 * num2
    return result
def main():
    num1 = get_number("Введите первое число: ") 
    num2 = get_number("Введите второе число: ") 
    operation = get_operation() 
    result = calculate(num1, num2, operation) 
    print(result)
main()
while True:
    decision = (input('Продолжить? (да/нет) ')).lower()
    if decision == 'да':
        main()
    elif decision == 'нет':
        break