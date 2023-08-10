# AND - all expressions must be True to return True
# OR - at least one must be True to return True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

balance = 1000
withdrawal = 250
limit = 200
special_account = True

exp = balance >= withdrawal and withdrawal <= limit or special_account and balance >= withdrawal
print(exp)

exp2 = (balance >= withdrawal and withdrawal <= limit) or (special_account and balance >= withdrawal)
print(exp2)

regular_account_with_enough_balance = balance >= withdrawal and withdrawal <= limit
special_account_with_enough_balance = special_account and balance >= withdrawal

exp3 = regular_account_with_enough_balance or special_account_with_enough_balance
print(exp3)