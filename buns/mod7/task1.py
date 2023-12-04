def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Too many arguments"

        user_input = args[0]

        if ' ' in user_input:
            return "Too many arguments"
        try:
            user_input = int(user_input)
        except ValueError:
            return "Wrong type"
        if user_input < 0:
            return "Negative argument"
        return func(user_input)

    return wrapper


@validate_args
def example_function(x):
    return f"Input accepted: {x}"

user_input = input("Введите целое неотрицательное число: ")

result = example_function(user_input)

print(result)
