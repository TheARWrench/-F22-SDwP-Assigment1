from task4 import error_test

@error_test
def error_zero_div(a=1):
    return a/0

error_zero_div(10)
error_zero_div(0)