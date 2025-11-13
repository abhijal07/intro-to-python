# Constants
num_departments = 4
num_employees = 5
work_days = 6

# Initialize total payroll
company_total = 0

for dept in range(1, num_departments + 1):
    print(f"\n--- Department {dept} ---")
    dept_total = 0
    
    for emp in range(1, num_employees + 1):
        daily_wage = float(input(f"Enter daily wage for Employee {emp} in Dept {dept}: ₹"))
        
        weekly_salary = daily_wage * work_days
        print(f"  Weekly salary for Employee {emp}: ₹{weekly_salary}")
        
        dept_total += weekly_salary
    
    print(f"Total salary for Department {dept}: ₹{dept_total}")
    company_total += dept_total

print("\n==============================")
print(f"Company's total weekly payroll: ₹{company_total}")
print("==============================")
