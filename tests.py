from cashmachine import *
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_max(self):
        cash_machine = CashMachine()
        cash_machine.five = 1

        result = cash_machine.cash_out(6)

        self.assertEqual(result.five, 0)

    def test_min(self):
        cash_machine = CashMachine()
        cash_machine.five = 1

        result = cash_machine.cash_out(4)

        self.assertEqual(result.total, 0)

    def test_cash_out_five_1(self):
        cash_machine = CashMachine()
        cash_machine.five = 1

        result = cash_machine.cash_out(5)

        self.assertEqual(result.total, 5)
        self.assertEqual(result.five, 1)

    def test_cash_out_amount_not_multiple_of_min(self):
        cash_machine = CashMachine()
        cash_machine.five = 2

        result = cash_machine.cash_out(7)

        self.assertEqual(result.total, 0)

    def test_cash_out_ten_having_two_five_bills(self):
        cash_machine = CashMachine()
        cash_machine.five = 2

        result = cash_machine.cash_out(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.five, 2)

    def test_cash_out_ten_having_one_ten_bill(self):
        cash_machine = CashMachine()
        cash_machine.ten = 1

        result = cash_machine.cash_out(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.ten, 1)

    def test_cash_out_fifteen_having_three_five_bill(self):
        cash_machine = CashMachine()
        cash_machine.five = 3

        result = cash_machine.cash_out(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 3)

    def test_cash_out_fifteen_having_two_five_bill_and_one_ten_bill(self):
        cash_machine = CashMachine()
        cash_machine.five = 2
        cash_machine.ten = 1

        result = cash_machine.cash_out(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 1)
        self.assertEqual(result.ten, 1)

