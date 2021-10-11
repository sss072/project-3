#Income 
#Expenses
#cash flow = Income - Expenses
#Cash on Cash roi  Annual Cash flow / Total investment(Downpayment + closing costs + renovation etc) . 
# Anything above 5 percent is decent.

class Roi():
        
    
    def income(self, income_entered):
        self.income_entered = income_entered
    
    def expenses(self, expenses_enetered):
        self.expenses_entered = expenses_enetered

    def cash_flow(self):
        self.monthly_profit = self.income_entered - self.expenses_entered   

    def total_investment(self, amount_entered):
        self.ivestment = amount_entered

    def percentage_roi(self):
        self.cash_flow()
        self.return_investment = (self.monthly_profit * 12) / self.ivestment

        if self.return_investment < 0.05:
            print(self.return_investment)
            print("this is not a good investment")
        else:
            print(self.return_investment)
            print("this is a good investment")    

flag = True

while flag:
    print("Would you like to find out the return on investment on a property? Enter Y or N")
    x = input()
    if x == "Y":
        new_roi = Roi()
        income_input = int(input("what is ur income on it"))
        new_roi.income(income_input)
        expenses_input = int(input("what are ur total expenses"))
        new_roi.expenses(expenses_input)

        investment_input = int(input("what is ur investment total"))
        new_roi.total_investment((investment_input))
        new_roi.percentage_roi()

    else: 
        flag = False





        

