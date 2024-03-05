'''
I'm not sure that this is how you wanted us to do it, since 3) says to create the global variable in main, and the only
function 1) says to make is use_global().
But I couldn't find another way to do it other then to have the global variable initialized here in question_d.py. 
When I tried initializing the global variable in main, or in the test case the only way I could 
find to access it here in question_d was to import it, which created a circular import error.

Because if I'm creating the global variable in main or in question_tests, then to access it I need to import main/question_tests
here, but I'm also importing this file to main & question_tests as well, which creates the circular error. So I'm not sure if this
is possible? Or if the way I did it is the intended way, or if I'm misunderstanding the question.
'''

global_variable = 0

def get_global_value():
    return global_variable

def set_global_value(val):
    global global_variable
    global_variable = val

def use_global():
    global global_variable
    global_variable = 100