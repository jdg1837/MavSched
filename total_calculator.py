import sys
import csv
from operator import add 

#python total_calculator first_month_file second_month_file

with open(sys.argv[1], mode='r') as csv_file:
    month1 = []
    for staff in csv_file:
        month1.append(staff.replace('\n','').split(','))
csv_file.close()

staff_count1 = {}
for staff in month1:
    staff_count1[staff[0]] = [[int(staff[1]),int(staff[2])],[int(staff[3]),int(staff[4])]]

with open(sys.argv[2], mode='r') as csv_file:
    month2 = []
    for staff in csv_file:
        month2.append(staff.replace('\n','').split(','))
csv_file.close()

staff_count2 = {}
for staff in month2:
    staff_count2[staff[0]] = [[int(staff[1]),int(staff[2])],[int(staff[3]),int(staff[4])]]

file_out = open(sys.argv[3], mode='w')
for key in staff_count2.keys():
    s2 = staff_count2[key]
    output = ""
    if staff_count1[key]:
        s1 = staff_count1[key]
        output = "{},{},{},{},{}\n".format(key, s2[0][0] + s1[0][0], s2[0][1] + s1[0][1], s2[1][0] + s1[1][0], s2[1][1] + s1[1][1])
    else:
        output = "{},{},{},{},{}\n".format(key, s2[0][0], s2[0][1], s2[1][0], s2[1][1])
    file_out.write(output)
file_out.close()  