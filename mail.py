import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("sender_mail_address","user_password")
subject="Sending email using python"
body="Hey ! Hope you are doing well and keeping safe ! Have a great day ahead ! Thanks ..."
message="subject:{}\n\n{}".format(subject,body)
ob.sendmail("sender_mail_address","receiver_mail_address",message)
print("Sent successfully..")
ob.quit()
