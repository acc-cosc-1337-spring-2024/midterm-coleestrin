from question_d import use_global, set_global_value, get_global_value

set_global_value(10)
print(f"Starting value of global: {get_global_value()}")
use_global()
print(f"Modified value of global: {get_global_value()}")