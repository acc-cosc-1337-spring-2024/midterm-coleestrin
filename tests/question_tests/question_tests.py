#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import use_local_variable
from src.question_b.question_b import get_bonus_pay
from src.question_c.question_c import get_day_of_week
from src.question_d.question_d import use_global, set_global_value, get_global_value

class Test_Config(unittest.TestCase):

    def test_question_a(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)

    def test_question_b(self):
        self.assertEqual(get_bonus_pay(-1), "Error: Invalid Argument")
        self.assertEqual(get_bonus_pay(200), 10)
        self.assertEqual(get_bonus_pay(600), 36)
        self.assertEqual(get_bonus_pay(1000), 70)
        self.assertEqual(get_bonus_pay(1500), 120)
        self.assertEqual(get_bonus_pay(2000), "Error: Invalid Argument")

    def test_question_c(self):
        self.assertEqual(get_day_of_week(0), "Error: Invalid Number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Error: Invalid Number")
        
    def test_question_d(self):
        set_global_value(300)
        self.assertEqual(get_global_value(), 300)
        use_global()
        self.assertEqual(get_global_value(), 100)
