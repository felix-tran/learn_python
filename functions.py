def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , from my function!, I wish you a %s" % (username,greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("Felix Tran", "a great year!")

x = sum_two_numbers(1,2)
print(x)