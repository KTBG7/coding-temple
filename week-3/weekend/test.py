import unittest
from roicalculator import ROICalculator

class TestROICalculator(unittest.TestCase):
    def test_predefined_total_income(self):
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
        calculator.calculate_income()
        expect_income = rental_income + laundry + misc + storage
        self.assertEqual(calculator.total_income, expect_income)
    
    def test_predefined_total_expense(self):
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
        calculator.calculate_expense()
        expected_expense = tax + insurance + vacancy + utilities + hoa + capex + lawn_care + repairs + property_management + mortgage
        self.assertEqual(calculator.total_expense, expected_expense)

    def test_predefined_cash_flow(self):
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
        calculator.calculate_cashflow()
        expected_expense = tax + insurance + vacancy + utilities + hoa + capex + lawn_care + repairs + property_management + mortgage
        expect_income = rental_income + laundry + misc + storage
        expected_cashflow = expected_expense + expect_income
        self.assertEqual(calculator.cash_flow, expected_cashflow)

    def test_predefined_cash_flow(self):
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
        calculator.calculate_cashflow()
        calculator.calculate_roi()
        expected_expense = tax + insurance + vacancy + utilities + hoa + capex + lawn_care + repairs + property_management + mortgage
        expect_income = rental_income + laundry + misc + storage
        expected_cashflow = expect_income - expected_expense
        expected_total_investment = down_payment + closing_costs + rehab_budget + misc_other
        expected_roi = (expected_cashflow * 12) / expected_total_investment
        expected_roi = expected_roi * 100
        self.assertEqual(calculator.roi, expected_roi)


    def test_user_defined_values(self):
        tax = int(input("How much do you pay monthly for tax? "))
        insurance = int(input('How much do you pay for insurance? '))
        utilities = int(input('How much do you pay for ulitities? '))
        hoa = int(input('How much do you pay for HOA? '))
        lawn_care = int(input('How much do you pay for Lawn Care? '))
        vacancy = int(input('How much do you pay for vacancy? '))
        repairs = int(input('How much do you pay for repairs? '))
        capex = int(input('How much do you pay for Capital Expenses? '))
        property_management = int(input('How much do you pay for property management? '))
        mortgage =  int(input("How much do you pay for your mortgage? "))
        rental_income = int(input("What is your rental income? "))
        laundry = int(input('How much do you spend for laundry? '))
        storage = int(input('How much do spend for storage? '))
        misc = int(input('How much do you pay for miscellaneous? '))
        down_payment = int(input('How much was your down payment?'))
        closing_costs = int(input('How much was the closing cost? '))
        rehab_budget = int(input('How much was the rehab budget? '))
        misc_other = int(input("How much did you pay for miscellaneous during your rental purchase? "))
        calculator = ROICalculator(tax, insurance, utilities, hoa, lawn_care, vacancy, repairs, capex, property_management, mortgage, rental_income, laundry, storage, misc, down_payment, closing_costs, rehab_budget, misc_other)
        calculator.calculate_cashflow()
        calculator.calculate_roi()
        expected_expense = tax + insurance + vacancy + utilities + hoa + capex + lawn_care + repairs + property_management + mortgage
        expect_income = rental_income + laundry + misc + storage
        expected_cashflow = expect_income - expected_expense
        expected_total_investment = down_payment + closing_costs + rehab_budget + misc_other
        expected_roi = (expected_cashflow * 12) / expected_total_investment
        expected_roi = expected_roi * 100
        self.assertEqual(calculator.total_income, expect_income)
        self.assertEqual(calculator.total_expense, expected_expense)
        self.assertEqual(calculator.cash_flow, expected_cashflow)
        self.assertEqual(calculator.roi, expected_roi)

unittest.main()