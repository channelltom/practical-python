# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11

extra_payment_start_month = int(input('Extra Payment Start Month:'))
extra_payment_end_month = int(input('Extra Payment End Month:'))
extra_payment = int(input('Payment Amount: $'))

total_paid = 0.0
months = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1

    if months >= extra_payment_start_month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    
    print(f"Month {months}, Total Paid: {round(total_paid, 2)}, Principal {round(principal, 2)}")
    #print (months, round(total_paid, 2), round(principal, 2))

print ('Total Paid:', round(total_paid, 2))
print ('Months Passed:', months)
