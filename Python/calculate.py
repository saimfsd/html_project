basic = float(input("Enter Basic Salary: "))

da_percent = float(input("Enter DA %: "))
hra_percent = float(input("Enter HRA %: "))

TA_percent = 5     # fixed
insurance = 500    # fixed
pf_percent = 12    # fixed

# Calculate amounts
DA = basic * da_percent / 100
HRA = basic * hra_percent / 100
TA = basic * TA_percent / 100
PF = basic * pf_percent / 100

# Gross salary (before deduction)
gross = basic + DA + HRA + TA

# Net salary (after deduction)
net = gross - insurance - PF

# Output
print("---------- Salary Sheet ----------")
print("Basic Salary     :", basic)
print("DA Amount        :", DA)
print("HRA Amount       :", HRA)
print("TA Amount        :", TA)
print("PF Deduction     :", PF)
print("Insurance        :", insurance)
print("-----------------------------------")
print("Gross Salary     :", gross)
print("Net Salary       :", net)































































.0


   

                                   