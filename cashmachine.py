
class CashOut:

    def __init__(self):
        self.total = 0
        self.five = 0
        self.ten = 0
        self.twenty = 0
        self.fifty = 0

    def add(self, bill_value, number):
        cash_in = bill_value * number
        self.total += cash_in
        if bill_value == 5:
            self.five += number
        if bill_value == 10:
            self.ten += number
        if bill_value == 20:
            self.twenty += number
        if bill_value == 50:
            self.fifty += number


class CashMachine:

    def __init__(self):
        self.five = [5, 0]  # [value, number of bills]
        self.ten = [10, 0]
        self.twenty = [20, 0]
        self.fifty = [50, 0]
        self.MIN = self.five[0]
        self.total = 0

    def deposit(self, value, quantity):
        switch = {
            5: self.five,
            10: self.ten,
            20: self.twenty,
            50: self.fifty
        }
        bill = switch[value]
        bill[1] += quantity
        self.total += value * quantity

    def cash_out(self, amount):
        result = CashOut()

        if amount > self.total:
            return result

        if (amount % self.MIN) != 0:
            # Impossible to cash out an amount that is not multiple of the lowest value bill.
            return result

        bills = [self.five, self.ten, self.twenty, self.fifty]
        bills = list(filter(lambda b: b[1] != 0, bills))
        bills.reverse()

        cashing_out = amount
        print('\n\nAMOUNT: ', amount)
        for bill in bills:
            needed = self._bills_needed(cashing_out, bill[0])
            available = bill[1]

            print('BILL: ', bill[1])
            print('NEEDED:', needed)
            print('AVAILABLE:', available)
            if needed <= 0:
                continue

            if needed <= available:  #if needed <= available:
                used = needed
            else:
                used = available

            result.add(bill[0], used)
            bill[1] -= used
            cashing_out -= used * bill[0]
            continue

        if result.total == amount:
            return result
        else:
            return CashOut()

    def _bills_needed(self, amount, bill):
        if bill > amount:
            return -1;

        remaining = amount % bill
        return (amount - remaining) / bill
