name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

if net > 50000:
    grade = "Senior Grade"

elif net > 30000:
    grade = "Mid Grade"

else:
    grade = "Junior Grade"

print("\nEmployee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("PF Deduction:", pf)
print("Gross Salary:", gross)
print("Net Salary:", net)
print("Employee Grade:", grade)