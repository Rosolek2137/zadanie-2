import math

def factorize(num):
    factors = []
    i = 2
    while num > 1:
        if num % i == 0:
            factors.append(i)
            num /= i
        else:
            i += 1
    return factors

def calculate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Nie można obliczyć podanego wyrażenia."

def calculate_task(task):
    if task.startswith("Obwód trójkąta"):
        a = b = c = 0
        for element in task.split(","):
            if "a=" in element:
                a = float(element.split("=")[1])
            elif "b=" in element:
                b = float(element.split("=")[1])
            elif "c=" in element:
                c = float(element.split("=")[1])
        if a + b > c and a + c > b and b + c > a:
            obwod = a + b + c
            return f"Obwód trójkąta wynosi: {obwod} cm"
        else:
            return "Nieprawidłowe wartości boków trójkąta."
    else:
        return "Nieznane polecenie."

def log_operation(operation):
    with open("log.txt", "a") as log_file:
        log_file.write(operation + "\n")

while True:
    user_input = input("Wpisz działanie lub polecenie: ")
    if user_input.lower() == "koniec":
        break
    elif user_input.lower() == "log":
        with open("log.txt", "r") as log_file:
            print(log_file.read())
    else:
        factors = factorize(int(user_input))
        if len(factors) > 1:
            operation = f"{user_input} = {' * '.join(map(str, factors))}"
            print(operation)
            log_operation(operation)
        else:
            expression_result = calculate_expression(user_input)
            if expression_result != "Nie można obliczyć podanego wyrażenia.":
                operation = f"{user_input} = {expression_result}"
                print(operation)
                log_operation(operation)
            else:
                task_result = calculate_task(user_input)
                print(task_result)
                if task_result != "Nieznane polecenie.":
                    log_operation(user_input + " = " + task_result)
