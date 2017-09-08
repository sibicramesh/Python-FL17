inputList = [{'Name': 'Sibi', 'StartingSalary': 50000, 'SalaryNow': 100000},
             {'Name': 'Arun', 'StartingSalary': 60000, 'SalaryNow': 120000},
             {'Name': 'Kalind', 'StartingSalary': 70000, 'SalaryNow': 130000}]

# Fucntion to average salaries
def avgSalaries():
    for sal in inputList:
        avgSalary = (sal.get('StartingSalary') + sal.get('SalaryNow')) / 2
        sal.pop('StartingSalary')
        sal.pop('SalaryNow')
        sal['AverageSalary'] = int(avgSalary)
    return inputList


print("******** Before Calling Average Function ********")
print(inputList, "\n")
print("******** After calling Average Function *********")
print(avgSalaries())
