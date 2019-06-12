def logger(function):
    def function_time(*args, **kwargs):
        import datetime
        time_now = datetime.datetime.today().strftime("%d.%m.%Y.%H:%M:%S")
        result = function(*args, **kwargs)
        with open('INFO.txt', 'w', encoding="utf-8") as info:
            print('Time=', time_now, 'Name function=', function.__name__, 'Result =', result, 'Arguments =', *args,
                  **kwargs, file=info)
        return result
    return function_time

@logger
def ret(number):
    f = number**3
    return f

ret(10)
