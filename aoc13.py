depart_minute = 0
shuttlids = []
with open('data13.txt','r') as f:
   depart_minute = int(f.readline())
   shuttlids = f.readline().split(",")
print(shuttlids)
all_minutes = []
schedule_table = {}

for i in shuttlids:
    if i != 'x':
        bus_minutes = []
        arrive_minute = int(i)
        bus_minutes.append(arrive_minute)
        while arrive_minute < depart_minute:
            arrive_minute += int(i)
            if arrive_minute > depart_minute-1000:
                bus_minutes.append(arrive_minute)
        all_minutes += bus_minutes 
all_minutes.sort()
goal_minute = 0
for i in all_minutes:
    if i > depart_minute:
        goal_minute = i
        break
print(depart_minute)
print(goal_minute)

for i in shuttlids:
    if i != 'x':
        arrive_minute = int(i)
        while arrive_minute < depart_minute:
            arrive_minute += int(i)
            if arrive_minute == goal_minute:
                print("FINISHED")
                print(i)
        all_minutes += bus_minutes 