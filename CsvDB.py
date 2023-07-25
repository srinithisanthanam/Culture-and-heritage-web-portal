import csv
import os
def CREATE(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw):
    f = open("det.txt", "a")
    wobj = csv.writer(f, delimiter=",")
    print("Your account is successfully created!")
    wobj.writerow([fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw])
    f.flush()
    print("Welcome to SNS Heritage and Culture!")
    return(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw)
    f.close()

def UPDATE(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw):
    print(add1)
    f = open("det.txt", "a+")
    f.seek(0)
    c=0
    robj = csv.reader(f, delimiter=",")
    for a in robj:
        print(a[6])
        if c%2==0 and a[2]==eid:
            a[0]=fnam
            a[1]=lnam
            a[3]=gender
            a[4]=pno
            a[5]=dob
            a[6]=add1
            a[7]=city
            a[8]=region
            a[9]=pc
            a[10]=country
            a[11]=mt
            a[12]=ty
            a[13]=pw
        return a
    f.close()

def EDIT(fnam,lnam, eid, gender, pno, dob, add1, city, region, pc, country, mt, ty, pw):
    f = open("det.txt", "r")
    f.seek(0)
    c, s = 0, []
    robj = csv.reader(f, delimiter = ",")
    for a in robj:
        if c % 2 == 0 and a[2] !=eid:
            s.append(a)
        elif c % 2 == 0:
            a = []
            a.append(fnam)
            a.append(lnam)
            a.append(eid)
            a.append(gender)
            a.append(pno)
            a.append(dob)
            a.append(add1)
            a.append(city)
            a.append(region)
            a.append(pc)
            a.append(country)
            a.append(mt)
            a.append(ty)
            a.append(pw)
            s.append(a)
        c += 1
    f.close()
    f = open("det.txt", "w")
    wobj = csv.writer(f, delimiter = ",")
    for a in s:
        wobj.writerow(a)
    f.close()

def DISPLAY(email):
    while True:
        f=open("det.txt","r")
        f.seek(0)
        c=0
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if c%2==0 and a[2].strip()==email:
                return a
            c+=1
    f.close()


def DELETE(email):
    f = open("det.txt", "r")
    f.seek(0)
    c = 0
    s=[]
    robj = csv.reader(f, delimiter=",")
    for a in robj:
        if c%2==0 and a[2]!=email:
            s.append(a)
        c+=1
    f,close()
    f=open("det.txt","w")
    wobj=csv.writer(f, delimiter=",")
    for a in s:
        wobj.writerow(a)
    f.close()


def check_credentials(email,pwd):
    f = open("det.txt","r")
    f.seek(0)
    c = 0
    robj = csv.reader(f, delimiter=",")
    for a in robj:
        if c%2==0 and a[2]==email and a[13]==pwd:
            return True
        c=c+1
    else:
        return False
    f.close()

def check(email):
    f = open("det.txt","r")
    f.seek(0)
    c = 0
    robj = csv.reader(f, delimiter=",")
    for a in robj:
        if c%2==0 and a[2]==email:
            return True
        c=c+1
    else:
        return False
    f.close()







