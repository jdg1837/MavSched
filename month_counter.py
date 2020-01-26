import sys
import csv
import Month

#python month_counter.py [month-name]

month_name = sys.argv[1]

if not Month.isMonth(month_name):
    print('Error! please run as: python month_counter.py [month-name]')

month = Month.readFile(Month.scheduleFile(month_name))

staff_count_unsorted = {}

day_type_dict = dict.fromkeys([0,1,2,3,4], 0)
day_type_dict.update(dict.fromkeys([5,6], 1))
on_call_type_dict = {'P': 0, 'S': 1}

for week in month:
    for day in range(0,7):
        on_call_info = week[day]
        if on_call_info == '':
            continue
        on_call_info = on_call_info.replace("\xa0", "")
        on_call_info = on_call_info.strip()

        on_call_info = on_call_info.split(":")
        RA = on_call_info[1]

        day_type = 0
        on_call_type = 0
        if on_call_info[0] == 'HP':
            day_type = 1
            on_call_type = 0
        elif on_call_info[0] == 'HS':
            day_type = 1
            on_call_type = 1
        elif on_call_info[0] == 'RP':
            day_type = 0
            on_call_type = 0
        elif on_call_info[0] == 'RS':
            day_type = 0
            on_call_type = 1
        else:
            day_type = day_type_dict[day]
            on_call_type = on_call_type_dict[on_call_info[0]]
        

        if RA not in staff_count_unsorted.keys():
            staff_count_unsorted[RA] = [[0,0],[0,0]]

        staff_count_unsorted[RA][day_type][on_call_type] += 1

staff_count = {}
for key in sorted(staff_count_unsorted.keys()):
    staff_count[key] = staff_count_unsorted[key]

file_out = open(sys.argv[1] + '_count.csv', mode='w')
for key in staff_count.keys():
    count = staff_count[key]
    output = "{},{},{},{},{}\n".format(key, count[0][0], count[0][1], count[1][0], count[1][1])
    file_out.write(output)
file_out.close()