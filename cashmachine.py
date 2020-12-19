
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
        self._five = ['five', 5, 0]
        self._ten = ['ten', 10, 0]
        self._twenty = ['twenty', 20, 0]
        self._fifty = ['fifty', 50, 0]
        self._MIN = self._five
        self._total = 0

    @property
    def total(self):
        return self._total

    @property
    def five(self):
        return self._five

    @five.setter
    def five(self, bills):
        self._five[-1] += bills
        self._total += self._five[1] * bills

    @property
    def ten(self):
        return self._ten

    @ten.setter
    def ten(self, bills):
        self._ten[-1] += bills
        self._total += self._ten[1] * bills

    @property
    def twenty(self):
        return self._twenty

    @twenty.setter
    def twenty(self, bills):
        self._twenty[-1] += bills
        self._total += self._twenty[1] * bills

    @property
    def fifty(self):
        return self._fifty

    @fifty.setter
    def fifty(self, bills):
        self._fifty[-1] += bills
        self._total += self._fifty[1] * bills

    def cash_out(self, amount):
        result = CashOut()

        if amount > self._total:
            # Amount is greater than the total that the machine has.
            return result

        if (amount % self._MIN[1]) != 0:
            # Impossible to cash out an amount that is not multiple of the lowest value bill.
            return result

        bills = [self._five, self._ten, self._twenty, self._fifty]
        bills = list(filter(lambda b: b[-1] != 0, bills))
        bills.reverse()

        cashing_out = amount
        print('\n\nAMOUNT: ', amount)
        for bill in bills:
            needed = self._bills_needed(cashing_out, bill[1])
            available = bill[2]

            print('BILL: ', bill[1])
            print('NEEDED:', needed)
            print('AVAILABLE:', available)
            if needed <= 0:
                continue

            if needed <= available:  #if needed <= available:
                used = needed
            else:
                used = available

            result.add(bill[1], used)
            bill[2] -= used
            cashing_out -= used * bill[1]
            print('cashing_out uptaded: ', cashing_out)
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
