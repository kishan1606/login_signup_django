from django.shortcuts import render
import mysql.connector as sql
name=''
uname=''
email=''
pwd=''
# Create your views here.
def signaction(request):
    global name,uname,email,pwd
    if request.method=="POST": #check form is submitted
        m=sql.connect(host="localhost",user="root",passwd="root",database='test') #db connection
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                name=value
            if key=="user_name":
                uname=value
            if key=="email":
                email=value
            if key=="password":
                pwd=value
        
        cursor.execute("SELECT * FROM users WHERE email = %s OR username = %s", (email, uname)) #check if same username or email exist
        existing_user = cursor.fetchone()
        if existing_user:
            return render(request, 'signup_page.html', {'error_message': 'Email or username already exists'})

        c="insert into users Values('{}','{}','{}','{}')".format(name,uname,email,pwd) #no duplicate found execute insert query
        cursor.execute(c)
        m.commit()
        if cursor.rowcount > 0:
            return render(request, 'signup_page.html', {'ok_message': 'New user created'})
        else:
            return render(request, 'signup_page.html', {'error_message': 'Failed to create new user'})


    return render(request,'signup_page.html')