import sys
import csv
from operator import add 
import Month

#python total_calculator [first_month_name] [last_month_name]

initial_month = sys.argv[1].title()
last_month = sys.argv[2].title()

if not Month.isMonth(initial_month) and Month.isMonth(last_month):
    print('Error! please run as #python total_calculator [first_month_name] [last_month_name]')

months = Month.months
month1 = initial_month
month2 = initial_month

while month2 != last_month:
    month2 = months[(months.index(month2) + 1) % 12]
    Month.add(Month.countFile(month1),Month.countFile(month2), 'total_count.csv')
    month1 = 'total'