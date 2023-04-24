class ROICalculator:
    def __init__(self, tax, insurance, utilities, hoa, lawn_care, vacancy, repairs, capex, property_management, mortgage, rental_income, laundry, storage, misc, down_payment, closing_costs, rehab_budget, misc_other) -> None:
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn_care = lawn_care
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_management = property_management
        self.mortgage =  mortgage
        self.rental_income = rental_income
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other

    def calculate_expense(self) -> None:
        self.total_expense = self.tax + self.insurance + self.utilities + self.hoa + self.vacancy+ self.capex + self.lawn_care + self.repairs + self.property_management + self.mortgage
        print(f'Your total monthly expense will be: {self.total_expense}')
    
    def calculate_income(self):
        self.total_income = self.rental_income + self.laundry + self.storage + self.misc
        print(f'Your monthly rental income will be: {self.total_income}')
    
    def calculate_cashflow(self):
        self.calculate_expense()
        self.calculate_income()
        self.cash_flow = self.total_income - self.total_expense
        print(f'Your monthly cash flow will be: {self.cash_flow}')
    def calculate_roi(self) -> None:
        self.calculate_cashflow()
        total_investment = self.down_payment + self.closing_costs + self.rehab_budget + self.misc_other
        yearly_cash_flow = self.cash_flow * 12
        self.roi = yearly_cash_flow / total_investment
        self.roi = self.roi * 100
        print(f'Your return on investment is {self.roi}%')

tax = 150
insurance = 100
utilities = 0
hoa = 0
lawn_care = 0
vacancy = 100
repairs = 100
capex = 100
property_management = 200
mortgage = 860
rental_income = 2000
laundry = 0
storage = 0
misc = 0
down_payment = 40000
closing_costs = 3000
rehab_budget = 7000
misc_other = 0
calculator = ROICalculator(tax, insurance, utilities, hoa, lawn_care, vacancy, repairs, capex, property_management, mortgage, rental_income, laundry, storage, misc, down_payment, closing_costs, rehab_budget, misc_other)
calculator.calculate_roi()
