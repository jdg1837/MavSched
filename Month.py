months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

def isMonth(month):
    return month.title() in months

def countFile(month):
    return month.lower() + '_count.csv'

def scheduleFile(month):
    return month.lower() + '.csv'

def readFile(filename):
    with open(filename, mode='r') as csv_file:
        month_data = []
        for line in csv_file:
            month_data.append(line.replace('\n','').split(','))
    csv_file.close()
    return month_data

def add(month1_file,month2_file,outfile):
    month1 = readFile(month1_file)
    staff_count1 = {}
    for staff in month1:
        staff_count1[staff[0]] = [[int(staff[1]),int(staff[2])],[int(staff[3]),int(staff[4])]]

    month2 = readFile(month2_file)
    staff_count2_unsorted = {}
    for staff in month2:
        staff_count2_unsorted[staff[0]] = [[int(staff[1]),int(staff[2])],[int(staff[3]),int(staff[4])]]

    staff_count2 = {}
    for key in sorted(staff_count2_unsorted.keys()):
        staff_count2[key] = staff_count2_unsorted[key]

    file_out = open(outfile, mode='w')
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