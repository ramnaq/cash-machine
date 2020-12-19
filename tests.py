from cashmachine import *
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_cash_out_less_than_min_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 1

        result = cash_machine.cash_out(4)

        self.assertEqual(result.total, 0)

    def test_cash_out_amount_not_multiple_of_min_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 2

        result = cash_machine.cash_out(7)

        self.assertEqual(result.total, 0)

    def test_total(self):
        cash_machine = CashMachine()

        cash_machine.five = 2
        cash_machine.ten = 1
        cash_machine.twenty = 2
        cash_machine.fifty = 3

        self.assertEqual(cash_machine.total, 5*2 + 10*1 + 20*2 + 3*50)

    def test_cash_out_more_than_total_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 2
        cash_machine.five = 2

        result = cash_machine.cash_out(7)

        self.assertEqual(result.total, 0)

    def test_cash_out_five_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 1

        result = cash_machine.cash_out(5)

        self.assertEqual(result.total, 5)
        self.assertEqual(result.five, 1)

    def test_cash_out_ten_having_two_five_bills_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 2

        result = cash_machine.cash_out(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.five, 2)

    def test_cash_out_ten_having_one_ten_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.ten = 1

        result = cash_machine.cash_out(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.ten, 1)

    def test_cash_out_fifteen_having_three_five_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 3

        result = cash_machine.cash_out(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 3)

    def test_cash_out_fifteen_having_two_five_bill_and_one_ten_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 2
        cash_machine.ten = 1

        result = cash_machine.cash_out(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 1)
        self.assertEqual(result.ten, 1)

    def test_cash_out_thirty_having_two_twenty_bill_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.twenty = 2

        result = cash_machine.cash_out(30)

        self.assertEqual(result.total, 0)

    def test_cash_out_sixty_five_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 1
        cash_machine.ten = 2
        cash_machine.twenty = 2

        result = cash_machine.cash_out(65)

        self.assertEqual(result.total, 65)
        self.assertEqual(result.five, 1)
        self.assertEqual(result.ten, 2)
        self.assertEqual(result.twenty, 2)

    def test_cash_out_sixty_five_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 1
        cash_machine.ten = 1
        cash_machine.twenty = 2

        result = cash_machine.cash_out(65)

        self.assertEqual(result.total, 0)
        self.assertEqual(result.five, 0)
        self.assertEqual(result.ten, 0)
        self.assertEqual(result.twenty, 0)

    def test_cash_out_seventy_having_sixty_five_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.five = 1
        cash_machine.ten = 2
        cash_machine.twenty = 2

        result = cash_machine.cash_out(70)

        self.assertEqual(result.total, 0)
        self.assertEqual(result.five, 0)
        self.assertEqual(result.ten, 0)
        self.assertEqual(result.twenty, 0)

