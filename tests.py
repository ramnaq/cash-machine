from cashmachine import *
import unittest

class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_withdraw_less_than_min_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 1)

        result = cash_machine.withdraw(4)

        self.assertEqual(result.total, 0)

    def test_withdraw_amount_not_multiple_of_min_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 2)

        result = cash_machine.withdraw(7)

        self.assertEqual(result.total, 0)

    def test_total(self):
        cash_machine = CashMachine()

        cash_machine.deposit(5, 2)
        cash_machine.deposit(10, 1)
        cash_machine.deposit(20, 2)
        cash_machine.deposit(50, 3)

        self.assertEqual(cash_machine.total, 5*2 + 10*1 + 20*2 + 3*50)

    def test_withdraw_less_than_total_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 2)
        cash_machine.deposit(5, 2)

        result = cash_machine.withdraw(7)

        self.assertEqual(result.total, 0)

    def test_withdraw_five_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 1)

        result = cash_machine.withdraw(5)

        self.assertEqual(result.total, 5)
        self.assertEqual(result.five, 1)

    def test_withdraw_ten_having_two_five_bills_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 2)

        result = cash_machine.withdraw(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.five, 2)

    def test_withdraw_ten_having_one_ten_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(10, 1)

        result = cash_machine.withdraw(10)

        self.assertEqual(result.total, 10)
        self.assertEqual(result.ten, 1)

    def test_withdraw_fifteen_having_three_five_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 3)

        result = cash_machine.withdraw(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 3)

    def test_withdraw_fifteen_having_two_five_bill_and_one_ten_bill_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 2)
        cash_machine.deposit(10, 1)

        result = cash_machine.withdraw(15)

        self.assertEqual(result.total, 15)
        self.assertEqual(result.five, 1)
        self.assertEqual(result.ten, 1)

    def test_withdraw_thirty_having_two_twenty_bill_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(20, 2)

        result = cash_machine.withdraw(30)

        self.assertEqual(result.total, 0)

    def test_withdraw_sixty_five_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 1)
        cash_machine.deposit(10, 2)
        cash_machine.deposit(20, 2)

        result = cash_machine.withdraw(65)

        self.assertEqual(result.total, 65)
        self.assertEqual(result.five, 1)
        self.assertEqual(result.ten, 2)
        self.assertEqual(result.twenty, 2)

    def test_withdraw_sixty_five_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 1)
        cash_machine.deposit(10, 1)
        cash_machine.deposit(20, 2)

        result = cash_machine.withdraw(65)

        self.assertEqual(result.total, 0)
        self.assertEqual(result.five, 0)
        self.assertEqual(result.ten, 0)
        self.assertEqual(result.twenty, 0)

    def test_withdraw_seventy_having_sixty_five_NOT_OK(self):
        cash_machine = CashMachine()
        cash_machine.deposit(5, 1)
        cash_machine.deposit(10, 2)
        cash_machine.deposit(20, 2)

        result = cash_machine.withdraw(70)

        self.assertEqual(result.total, 0)
        self.assertEqual(result.five, 0)
        self.assertEqual(result.ten, 0)
        self.assertEqual(result.twenty, 0)

