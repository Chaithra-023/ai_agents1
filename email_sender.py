import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password


sender_email="4mh23cs023@gmail.com"
receiver_email="4mh23cs023@gmail.com"
app_password="zico huiu ajlb qctc"

# Create the email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Hello from Python"
msg.set_content("This email was sent using Python 🐍")

# Send it
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()                  # Secure the connection
    server.login(sender_email, app_password)
    server.send_message(msg)
print("Email sent successfully")