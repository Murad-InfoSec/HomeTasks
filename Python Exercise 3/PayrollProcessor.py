"""Payroll processing module."""

import math


class PayrollProcessor:
    """Manages employee payroll and salary calculations."""
    
    def __init__(self, name, role, salary):
        """Initialize employee data."""
        self.name = name
        self.role = role
        self.salary = salary
        
    def information(self):
        """Display employee information."""
        print(f"Employee: {self.name} Job Role: {self.role}\tSalary: {self.salary}")
    
    def increase_salary(self, percent):
        """Apply percentage increase to salary."""
        self.salary *= (1 + percent / 100)


if __name__ == "__main__":
    sabir = PayrollProcessor("Sabir Reham", "JR Admin", 1000)
    sabir.information()
    sabir.increase_salary(13.0)
    sabir.information()
