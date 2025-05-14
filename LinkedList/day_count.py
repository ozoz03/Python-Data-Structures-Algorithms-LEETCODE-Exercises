from datetime import date

print('Date format: YYYY-MM-DD')
# a = input('First date: ')
# b = input('Second date: ')
aa = date.today()
bb = date.fromisoformat('2025-06-23')
delta = abs(aa - bb)
print(delta.days)