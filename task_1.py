line = '1h 45m,360s,25m,30m 120s,2h 60s'
new_line = line.replace(',', ' ')
line_1 = new_line.split()
count_minutes = 0

for i in line_1:
    if 'h' in i:
        count_minutes += 60 * int(i[0:len(i)-1])
    elif 's' in i:
        count_minutes += int(i[0:len(i)-1]) / 60
    else:
        count_minutes += int(i[0:len(i)-1])

print(count_minutes)
