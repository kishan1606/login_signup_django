from django.shortcuts import render
import mysql.connector as sql
uname=''
pwd=''
# Create your views here.
def loginaction(request):
    global uname,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="uname":
                uname=value
            if key=="password":
                pwd=value
        
        c="select * from users where username='{}' and password='{}'".format(uname,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')