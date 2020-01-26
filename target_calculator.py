import sys
import csv

#python target_calculator.py 

with open('total_count.csv', mode='r') as csv_file:
    data = []
    for l in csv_file:
        data.append(l.replace('\n','').split(','))
csv_file.close()

target = [[0,0],[0,0]]
wdp = int(sys.argv[1])
wds = int(sys.argv[2])
wep = int(sys.argv[3])
wes = int(sys.argv[4])
target = [[wdp,wds],[wep,wes]]

staff_count = {}

for line in data:
    staff_count[line[0]] = [[int(line[1]),int(line[2])],[int(line[3]),int(line[4])]]

target_real = [0,0,0,0]

file_out = open('target.csv', mode='w')
for key in staff_count.keys():
    count = staff_count[key]
    target_buffer = [target[0][0] - count[0][0], target[0][1] - count[0][1], target[1][0] - count[1][0], target[1][1] - count[1][1]]
    for i in range(4):
        if target_buffer[i] > 0:
            target_real[i] += target_buffer[i]
    output = "{},{},{},{},{}\n".format(key, target_buffer[0], target_buffer[1], target_buffer[2], target_buffer[3])
    file_out.write(output)
file_out.close()

print(target_real)