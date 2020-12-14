shuttlids = []

with open('data13.txt','r') as f:
   f.readline()
   shuttlids = f.readline().split(",")

id_minutes = [[index,int(id)] for index,id in enumerate(shuttlids) if id != 'x']
id_minutes.sort(key = lambda i: (i[1]))
comp_minute = id_minutes[0][1]
done = False
gcd=id_minutes[0][1]

for i in id_minutes[1:]:
    while True:
        comp_minute += gcd
        answer = comp_minute - id_minutes[0][0]
        if (answer+i[0])%i[1]==0:
            print(i, answer)
            break
    gcd *= i[1]
print("FINISHED")
print(comp_minute)
