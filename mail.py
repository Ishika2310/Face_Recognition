import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("ishika.sharma2310@gmail.com","IshikaSharma2310")
subject="Sending email using python"
body="Hey ! Hope you are doing well and keeping safe ! Have a great day ahead ! Thanks ..."
message="subject:{}\n\n{}".format(subject,body)
ob.sendmail("ishika.sharma2310@gmail.com","ishash2310@gmail.com",message)
print("Sent successfully..")
ob.quit()