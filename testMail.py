import smtplib, ssl

port = 465  # For SSL


sender_email = "crazyydeveloper@gmail.com"
receiver_email = ['karan2399@gmail.com']
message = """\
Subject: This is subject

Hello Fellow User,\nThis is crazy developer speaking.\n"""

message += "TESTING TESTING"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, "Qwert@321")
    server.sendmail(sender_email,receiver_email,message)
    print(f"Email sent to {receiver_email}")

print(message)
