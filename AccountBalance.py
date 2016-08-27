class AccountBalance(object):
    def processTransactions(self, startingBalance, transactions):
        for typ, amt in map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(), transactions)):
            if typ == "C":
                startingBalance += amt
            elif typ == "D":
                startingBalance -= amt
        return startingBalance

print AccountBalance().processTransactions(53874, ["D 1234", "C 987", "D 2345", "C 654", "D 6789", "D 34567"])
