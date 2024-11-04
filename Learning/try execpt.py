import sys
start = 6
string = 'hi'
try:
    deposit = int(input('enter your deposit'))
except TypeError:
    print(' data type logic operation error, int cannot add str ')
except SyntaxError:
    print('syntax error')
except RuntimeError:
    print('run time error')
except NameError:
    print('variable name error, variable does not exist')
except IndexError:
    print('index error (for list), index input does not exist yet')
except ValueError:
    # input statement must also inside the try block
    print('data type input wrong, expected number receive char')
except KeyboardInterrupt:
    print('\nstop manually midway in a running code that lies in try block')
#
#
# num = 1
# num2 = 0
# try:
#     num = num + num2
#     print(num)
# except:  # no specific error, it will check all
#     print('something wrong')
# finally:  # optional, this block of code will always run
#     print('end')
#
# '''    for i in range(3):
#         print(sys.exc_info()[i])'''
# # this show the error message, 0 = type of error
# # 1 = what is the part that is wrong
#
