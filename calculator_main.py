import calculator_module

MESSAGES = ("\nFirst value: ","Operator: ","Second value: ")

def user_input():

    values = []

    for n in range(3):
        u_input = input(MESSAGES[n])
        if u_input == "q":
            return False
        values.append(u_input)
    
    try:
        values[0] = float(values[0].strip())
        assert values[1] in calculator_module.operations
        values[2] = float(values[2].strip())
    except:
        raise ValueError("""Invalid input given.
            Values should be numbers.
            Valid operators: + - * / // ^ %""")
    return tuple(values)

def calculate(value_1,operator,value_2):

    #runs a function from calculator on the two values
    result = calculator_module.operations[operator](value_1,value_2)

    #doesn't return float on whole numbers
    if result.is_integer():
        result = int(result)

    return result

if __name__ == "__main__":

    print("\n###### Welcome to CALCULATOR #######")
    print("######## Enter 'q' to quit. ########")

    while True:

        user_values = user_input()
        
        if not user_values:
            print("#### Thank you for using CALCULATOR ###")
            break

        print(f"Result: {calculate(*user_values)}")
