import sys
import csv

#python month_counter.py [month-name]

with open(sys.argv[1] + '.csv', mode='r') as csv_file:
    month = []
    for week in csv_file:
        month.append(week.replace('\n','').split(','))
csv_file.close()

staff_count = {}

day_type_dict = dict.fromkeys([0,1,2,3,4], 0)
day_type_dict.update(dict.fromkeys([5,6], 1))
on_call_type_dict = {'P': 0, 'S': 1, 'H': 0}

for week in month:
    for day in range(0,7):
        on_call_info = week[day]
        if on_call_info == '':
            continue
        on_call_info = on_call_info.replace("\xa0", "")

        RA = on_call_info[2:]
        day_type = day_type_dict[day]
        on_call_type = on_call_type_dict[on_call_info[0]]
        if on_call_info[0] == 'H':
            day_type = 1

        if RA not in staff_count.keys():
            staff_count[RA] = [[0,0],[0,0]]

        staff_count[RA][day_type][on_call_type] += 1

file_out = open(sys.argv[1] + '_count.csv', mode='w')
for key in staff_count.keys():
    count = staff_count[key]
    output = "{},{},{},{},{}\n".format(key, count[0][0], count[0][1], count[1][0], count[1][1])
    file_out.write(output)
file_out.close()