import smtplib
try:
    server =smtplib.SMTP(host='smtp.gmail.com',port =587)
    server.starttls()
    recever_email=input("enter your email")
    sender_email = 'manishmahawar489@gmail.com'
    password = 'oyiu jvsq ipnc ucro'
    server.login(sender_email,password=password)
    subject =input("what is your problem")
    body = input("Tell deatails")
    message = f"subject{subject}\n\n{body}"
    server.sendmail(sender_email,recever_email,message)
    print("send &%")
    server.quit()
except Exception as e:
    print(e)
else:
    print("yes we did it")    

