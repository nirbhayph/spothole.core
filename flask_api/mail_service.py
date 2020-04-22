# author: nirbhay pherwani. (https://nirbhay.me, pherwani37@gmail.com, np5318@rit.edu, https://github.com/nirbhayph)
# mail service for sending email notifications using a google account
import smtplib

# sending an email (accepts recipient email, message and optional subject line
def send_email_spothole(mailToEmail, message, subject="New notification from Spothole!"):
    try:
        gmailaddress = "contact.spothole@gmail.com"
        gmailpassword = "Amazon@12345"
        mailto = mailToEmail
        msg = 'From: Spothole App\nSubject: {}\n\n{}'.format(subject, message)
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        mailServer.quit()
        return ("Email Sent")
    except:
        return ("Email Not Sent")
