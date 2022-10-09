from asyncore import write
import csv
from email import header
from fileinput import filename
import random
x=0
y=0
for j in range(5):
    z=input("请输入你要点名的课\n")
    if z=='软件工程': 
        with open('D://软件工程.csv','r') as f:
            data=[row for row in csv.DictReader(f)]
            header=data[0].keys()
            for p in range(1,21):
                for i in range(90):
                    if random.choice(range(100))<int(float(data[i]['概率']))-2*int(float(data[i]['绩点']))+10:
                        y+=1
                        if data[i]['出勤'+str(p)]=='1':
                            x+=1
                            data[i]['概率']=int(data[i]['概率'])-2
                        else:   
                            data[i]['概率']=int(data[i]['概率'])+2
                    with open('D://软件工程.csv','w',newline='')as k:
                        writer=csv.DictWriter(k,fieldnames=header)
                        writer.writeheader()
                        writer.writerows(data)
    elif z=='接口技术':
        with open('D://接口技术.csv','r') as f:
            data=[row for row in csv.DictReader(f)]
            header=data[0].keys()
            for p in range(1,21):
                for i in range(90):
                    if random.choice(range(100))<int(float(data[i]['概率']))-2*int(float(data[i]['绩点']))+10:
                        y+=1
                        if data[i]['出勤'+str(p)]=='1':
                            x+=1
                            data[i]['概率']=int(data[i]['概率'])-2
                        else:   
                            data[i]['概率']=int(data[i]['概率'])+2
                    with open('D://接口技术.csv','w',newline='')as k:
                        writer=csv.DictWriter(k,fieldnames=header)
                        writer.writeheader()
                        writer.writerows(data)
    elif z=='概率论':
        with open('D://概率论.csv','r') as f:
            data=[row for row in csv.DictReader(f)]
            header=data[0].keys()
            for p in range(1,21):
                for i in range(90):
                    if random.choice(range(100))<int(float(data[i]['概率']))-2*int(float(data[i]['绩点']))+10:
                        y+=1
                        if data[i]['出勤'+str(p)]=='1':
                            x+=1
                            data[i]['概率']=int(data[i]['概率'])-2
                        else:   
                            data[i]['概率']=int(data[i]['概率'])+2
                    with open('D://概率论.csv','w',newline='')as k:
                        writer=csv.DictWriter(k,fieldnames=header)
                        writer.writeheader()
                        writer.writerows(data)
    elif z=='数据库':
        with open('D://数据库.csv','r') as f:
            data=[row for row in csv.DictReader(f)]
            header=data[0].keys()
            for p in range(1,21):
                for i in range(90):
                    if random.choice(range(100))<int(float(data[i]['概率']))-2*int(float(data[i]['绩点']))+10:
                        y+=1
                        if data[i]['出勤'+str(p)]=='1':
                            x+=1
                            data[i]['概率']=int(data[i]['概率'])-2
                        else:   
                            data[i]['概率']=int(data[i]['概率'])+2
                    with open('D://数据库.csv','w',newline='')as k:
                        writer=csv.DictWriter(k,fieldnames=header)
                        writer.writeheader()
                        writer.writerows(data)
    elif z=='图形学':
        with open('D://图形学.csv','r') as f:
            data=[row for row in csv.DictReader(f)]
            header=data[0].keys()
            for p in range(1,21):
                for i in range(90):
                    if random.choice(range(100))<int(float(data[i]['概率']))-2*int(float(data[i]['绩点']))+10:
                        y+=1
                        if data[i]['出勤'+str(p)]=='1':
                            x+=1
                            data[i]['概率']=int(data[i]['概率'])-2
                        else:   
                            data[i]['概率']=int(data[i]['概率'])+2
                    with open('D://图形学.csv','w',newline='')as k:
                        writer=csv.DictWriter(k,fieldnames=header)
                        writer.writeheader()
                        writer.writerows(data)
print(x/y)
    

