import csv
import os
def CREATE():
    f=open("det.txt","w")
    wobj=csv.writer(f,delimiter=",")
    while True:
        fnam=input("Enter first name:")
        lnam=input("Enter last name:")
        eid=input("Enter email id as user name:")
        o=''
        pw=PWD(o)
        pno=input("Enter phone number:")
        dob=input("Enter Date of Birth as dd/mm/yyyy:")
        add1=input("Enter address 1:")
        add2=input("Enter alternate address2:")
        city=input("Enter city:")
        pc=input("Enter pincode:")
        a, b='', []
        ty, mt=TYPE(a,b)
        print("Your account is successfully created!")
        wobj.writerow([fnam,lnam,eid,pno,dob,add1,add2,city,pc,ty,mt,pw])
        f.flush()
        print("Welcome", fnam, "to SNS Heritage and Culture!")
        ch=input("More accounts? Y/N:")
        if ch in "Yy":
            print("We are glad to include you as a part of our family!")
        else:
            break
    f.close()
    
def TYPE(ty,mt):
    while True:
        ty=""
        ty=input("Enter desired type of membership(Gold/Silver/Bronze):")
        mt=[]
        if ty.upper() not in ["GOLD", "SILVER", "BRONZE"]:
            print("Invalid membership type. Enter again.")
            continue
        if ty.upper()=="GOLD":
            mt=["Dance","Historical sites","Music"]
            ty="Gold"
        elif ty.upper()=="SILVER":
            print("Choose any 2 of the following:")
            mt=[]
            d=input("Dance(Y/N):")
            h=input("Historical Sites(Y/N):")
            m=input("Music(Y/N):")
            if d in 'Yy':
                mt+=["Dance"]
            if h in 'Yy':
                mt+=["Historical sites"]
            if m in 'Yy':
                mt+=["Music"]
            if len(mt)==1:
                print("Only 1 field entered. Converting to Bronze.")
                ty="Bronze"
            elif len(mt)==3:
                print("All 3 fields chosen. Converting to Gold.")
                ty="Gold"
        elif ty.upper()=="BRONZE":
            print("Choose any 1 of the following:")
            mt=[]
            d=input("Dance(Y/N)")
            h=input("Historical sites(Y/N):")
            m=input("Music(Y/N):")
            if d in 'Yy':
                mt+=["Dance"]
            if h in 'Yy':
                mt+=["Historical sites"]
            if m in 'Yy':
                mt+=["Music"]
            if len(mt)==2:
                print("2 fields chosen. Converting to Silver.")
                ty="Silver"
            elif len(mt)==3:
                print("All 3 fields chosen. Converting to Gold.")
                ty="Gold"
        if mt!=[]:
            break
    else:
        print("Choose at least 1 field.")
        a,b='',[]
        TYPE(a,b)
    print("Congratulations!")
    return ty, mt

def PWD(o=""):
    while True:
        o=input("Enter password:")
        pc=input("Enter password again for confirmation:")
        if o==pc:
            break
        else:
            print("Passwords do not match. Try again.")
    return o
        
def CHGPWD(fu):
    che=fu
    while True:
        f=open("det.txt","r")
        f.seek(0)
        c=0
        pn=input("Enter phone number to check")
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if c%2==0 and pn==a[3] and che==a[2]:
                print("Phone numbers match.")
                o=PWD()
                return o
            c+=1
            continue
        else:
            print("Invalid phone number. Try again.")
            f.close()

def APPEND():
    f=open("det.txt","a")
    si=os.path.getsize("det.txt")
    f.seek(si)
    wobj=csv.writer(f,delimiter=",")
    while True:
        fnam=input("Enter first name:")
        lnam=input("Enter last name:")
        eid=input("Enter email id as user name:")
        o=''
        pw=PWD(o)
        pno=input("Enter phone number:")
        dob=input("Enter Date of Birth as dd/mm/yyyy:")
        add1=input("Enter address 1:")
        add2=input("Enter alternate address2:")
        city=input("Enter city:")
        pc=input("Enter pincode:")
        a, b='', []
        ty, mt=TYPE(a,b)
        print("Your account is successfully created")
        wobj.writerow([fnam,lnam,eid,pno,dob,add1,add2,city,pc,ty,mt,pw])
        f.flush()
        print("Welcome", fnam, "to SNS Heritage and Culture!")
        ch=input("Are your relatives also willing to be members? Y/N:")
        if ch in "Yy":
            print("We are glad to include you as a part of our family!")
        else:
            break
    f.close()

def DISPLAY():
    while True:
        f=open("det.txt","r")
        f.seek(0)
        c=0
        mc=input("Enter username(e-mail id) of member to display the account details:")
        p=input("Enter password:")
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if c%2==0 and a[2].strip()==mc and p==a[11]:
                print("First name:", a[0], "\tLast Name:",a[1])
                print("User ID:",a[2])
                print("Phone number:",a[3])
                print("DOB:",a[4])
                print("Address 1:",a[5])
                print("Address 2:",a[6])
                print("City:",a[7],"\tPincode:",a[8])
                print("Membership type:",a[9])
                print("Password:",a[11])
                print("Chosen fields:",end="")
                for i in a[10]:
                    if i.isspace():
                        print(" ", end='')
                    elif i.isalnum():
                        print(i,end="")
                    elif i==",":
                        print(end=", ")
                    else:
                        continue
                print()
                break
            c+=1
        else:
            print("Invalid username or password.")
            cp=input("Change password?")
            if cp in 'Yy':
                pw=CHGPWD(mc)
                f.close()
                f=open("det.txt","r")
                robj=csv.reader(f,delimiter=",")
                c=0
                s=[]
                for al in robj:
                    if c%2==0:
                        s.append(al)
                    c+=1
                f.close()
                f=open("det.txt","w")
                wobj=csv.writer(f,delimiter=",")
                for b in s:
                    if b[2]==mc:
                        b[11]=pw
                        print("Password updated.")
                        wobj.writerow(b)
                    else:
                        wobj.writerow(b)
                    continue
            f.close()
            ch=input("Try Again? Y/N")
            if ch in 'Yy':
                continue
        break
            
def DELETE():
    while True:
        f=open("det.txt","r")
        mc=input("Enter username(e-mail id) to delete:")
        p=input("Enter password:")
        f.seek(0)
        c=0
        s=[]
        robj=csv.reader(f,delimiter=",")
        for a in robj:
            if c%2==0 and a[2].lower()!=mc.lower():
                s.append(a)
            elif c%2==0 and a[2].lower()==mc.lower() and p==a[11].strip():
                print("Details of deleted account:")
                print("First name:", a[0], "\tLast Name:",a[1])
                print("User ID:",a[2])
                print("Phone number:",a[3])
                print("DOB:",a[4])
                print("Address 1:",a[5])
                print("Address 2:",a[6])
                print("City:",a[7],"\tPincode:",a[8])
                print("Membership type:",a[9])
                print("Chosen fields:",end='')
                for i in a[10]:
                    if i.isspace():
                        print(" ", end='')
                    elif i.isalnum():
                        print(i,end="")
                    elif i==",":
                        print(end=", ")
                    else:
                        continue
                print()
                print("Your account has been successfully deleted!")
                break
            c+=1
        else:
            print("Invalid username or password.")
            cp=input("Change password?")
            if cp in 'Yy':
                pw=CHGPWD(mc)
                f.close()
                f=open("det.txt","r")
                robj=csv.reader(f,delimiter=",")
                c=0
                s=[]
                for al in robj:
                    if c%2==0:
                        s.append(al)
                    c+=1
                f.close()
                f=open("det.txt","w")
                wobj=csv.writer(f,delimiter=",")
                c=0
                for b in s:
                    if b[2].strip()==mc.strip():
                        b[11]=pw
                        print("Password updated.")
                        wobj.writerow(b)
                    else:
                        wobj.writerow(b)
                    continue
            f.close()
            ch=input("Try Again? Y/N")
            if ch in 'Yy':
                continue
        break
        
def UPDATE():
    f=open("det.txt","r")
    mc=input("Enter username(e-mail ID) 0f account to update membership:")
    p=input("Enter password:")
    f.seek(0)
    c=0
    s=[]
    robj=csv.reader(f,delimiter=",")
    for a in robj:
        if c%2==0 and a[2].lower()!=mc.lower():
            s.append(a)
        elif c%2==0 and mc.upper()==a[2].upper() and p==a[11].strip():
            print("Details of account:")
            print("First name:", a[0], "\tLast Name:",a[1])
            print("User ID:",a[2])
            print("Phone number:",a[3])
            print("DOB:",a[4])
            print("Address 1:",a[5])
            print("Address 2:",a[6])
            print("City:",a[7],"\tPincode:",a[8])
            print("Membership type:",a[9])
            print("Chosen fields:",end='')
            for i in a[10]:
                if i.isspace():
                    print(" ", end='')
                elif i.isalnum():
                    print(i,end="")
                elif i==",":
                    print(end=", ")
                else:
                    continue
            print()
            if a[9].upper()=="GOLD":
                print("Account has gold membership.")
                si=input("Want to change it to Silver?(Y/N)")
                if si in 'Yy':
                    anot=input("Enter field to be removed:")
                    if anot.lower() in ["dance","historical sites", "music"]:
                        if anot.lower()=="dance":
                            a[10]=["Historical sites","Music"]
                        elif anot.lower()=="historical sites":
                            a[10]==["Dance","Music"]
                        elif anot.lower()=="music":
                            a[10]==["Dance","Historical sites"]
                        a[9]="Silver"
                        print("Change in membership has been updated.")
                    else:
                        print("Field does not exist. Account remains as Gold membership.")
                else:
                    br=input("Want to change it to Bronze?(Y/N)")
                    if br in 'Yy':
                        anot=input("Enter the field name chosen:")
                        if anot.lower() in ["dance", "historical sites", "music"]:
                            a[10]=[anot]
                            a[9]="Bronze"
                            print("Change in membership has been updated.")
                        else:
                            print("Field does not exist. Account remains as Gold membership.")
            elif a[9].upper()=="SILVER":
                print("Account has Silver membership.")
                go=input("Want to change it to Gold?(Y/N)")
                if go in 'Yy':
                    a[9]="Gold"
                    a[10]=["Dance", "Historical sites", "Music"]
                    print("Change in membership has been updated.")
                else:
                    br=input("Want to change it to Bronze?(Y/N)")
                    if br in 'Yy':
                        anot=input("Enter the field to be chosen:")
                        if anot.lower() in ["dance", "historical sites", "music"]:
                            a[10]=[anot]
                            a[9]="Bronze"
                            print("Change in membership has been updated.")
                        else:
                            print("Field does not exist. Account remains as Silver membership.")
            elif a[9].upper()=="BRONZE":
                print("Account has Bronze membership.")
                go=input("Want to change it to Gold?(Y/N)")
                if go in 'Yy':
                    a[9]="Gold"
                    a[10]=["Dance", "Historical sites", "Music"]
                    print("Change in membership has been updated.")
                else:
                    si=input("Want to change it to silver?(Y/N)")
                    if si in 'Yy':
                        anot=input("Enter field to be added:")
                        if anot.lower() in ["dance","historical sites","music"]:
                            if "dance" in a[10].lower():
                                a[10]=["Dance",anot]
                            elif "historical sites" in a[10].lower():
                                j="Historical sites"
                                if j.upper()>anot.upper():
                                    j,anot=anot,j
                                a[10]=[j,anot]
                            elif "music" in a[10].lower():\
                                a[10]=[anot,"Music"]
                            a[9]="Silver"
                            print("Change in membership has been updated.")
                        else:
                            print("Field does not exist. Account remains as Bronze membership.")
            s.append(a)
        c+=1
    else:
        for b in s:
            if mc.upper()==b[2].upper() and p==b[11]:
                break
            continue
        else:
            print("Invalid username or password.")
            cp=input("Change password?")
            if cp in 'Yy':
                pw=CHGPWD(mc)
                f.close()
                f=open("det.txt","r")
                robj=csv.reader(f,delimiter=",")
                c=0
                s=[]
                for al in robj:
                    if c%2==0:
                        s.append(al)
                    c+=1
                f.close()
                f=open("det.txt","w")
                wobj=csv.writer(f,delimiter=",")
                for b in s:
                    if b[2].strip()==mc.strip():
                        b[11]=pw
                        print("Password updated.")
                        wobj.writerow(b)
                    else:
                        wobj.writerow(b)
                    continue
            f.close()
            ch=input("Try Again? Y/N")
            if ch in 'Yy':
                UPDATE()
    f.close()
    f=open("det.txt","w")
    wobj=csv.writer(f,delimiter=",")
    for a in s:
        wobj.writerow(a)
    f.close()

def EDIT():
    f=open("det.txt","r")
    mc=input("Enter username(e-mail ID) to modify account details:")
    p=input("Enter password:")
    f.seek(0)
    c=0
    s=[]
    robj=csv.reader(f,delimiter=",")
    for a in robj:
        if c%2==0 and a[2].upper()!=mc.upper():
            s.append(a)
        elif c%2==0 and mc.upper()==a[2].upper() and p==a[11].strip():
            print("Existing record details:")
            print("First name:", a[0], "\tLast Name:",a[1])
            print("User ID:",a[2])
            print("Phone number:",a[3])
            print("DOB:",a[4])
            print("Address 1:",a[5])
            print("Address 2:",a[6])
            print("City:",a[7],"\tPincode:",a[8])
            print("Membership type:",a[9])
            print("Chosen fields:",end=', ')
            for i in a[10]:
                if i.isspace():
                    print(" ", end='')
                elif i.isalnum():
                    print(i,end="")
                elif i==",":
                    print(end=", ")
                else:
                    continue
            print()
            print("Enter details to modify the account:")
            fnam=input("Enter first name:")
            lnam=input("Enter last name:")
            eid=input("Enter email id as user name:")
            o=''
            pw=PWD(o)
            pno=input("Enter phone number:")
            dob=input("Enter Date of Birth as dd/mm/yyyy:")
            add1=input("Enter address 1:")
            add2=input("Enter alternate address2:")
            city=input("Enter city:")
            pc=input("Enter pincode:")
            x, b='', []
            ty, mt=TYPE(x,b)
            print("Your account has been modified!")
            a=[]
            a=[fnam, lnam, eid, pno, dob, add1, add2, city, pc, ty, mt, pw]
            s.append(a)
        c+=1
    else:
        for b in s:
            if mc.upper()==b[2].upper() and p==b[11]:
                break
            continue
        else:
            print("Invalid username or password.")
            cp=input("Change password?")
            if cp in 'Yy':
                pw=CHGPWD(mc)
                f.close()
                f=open("det.txt","r")
                robj=csv.reader(f,delimiter=",")
                c=0
                s=[]
                for al in robj:
                    if c%2==0:
                        s.append(al)
                    c+=1
                f.close()
                f=open("det.txt","w")
                wobj=csv.writer(f,delimiter=",")
                for b in s:
                    if b[2].strip()==mc.strip():
                        b[11]=pw
                        print("Password updated.")
                        wobj.writerow(b)
                    else:
                        wobj.writerow(b)
                    continue
            f.close()
            ch=input("Try Again? Y/N")
            if ch in 'Yy':
                EDIT()
    f.close()
    f=open("det.txt","w")
    wobj=csv.writer(f,delimiter=",")
    for a in s:
        wobj.writerow(a)
    f.close()
    
CREATE()
print("Welcome to SNS Heritage center!")
print("You are in the account management section")
while True:
    ch=int(input())
    if ch==1:
        APPEND()
    elif ch==2:
        DISPLAY()
    elif ch==3:
        DELETE()
    elif ch==4:
        UPDATE()
    elif ch==5:
        EDIT()
    else:
        break                