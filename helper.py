import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
 
 
fromaddr = 'roswellprogramming@gmail.com'
password = 'hourofcode'


## setup the MIME
def send_emails(data):

    ## start up and log in
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)

    for i, email in enumerate(data):
        print(i)
        subject, body, toaddr = email[0], email[1], email[2]

        index = body.find('</body>')
        if index != -1:
            interjection = '<br><br><i>Hi! I am a bot. This is my ' + str(i + 1) + ' out of ' + str(len(data)) + ' emails. Sorry about the duplicates!</i>'
            body = body[:index] + interjection + body[index:]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        ## send the message
        text = msg.as_string()
        try: 
            server.sendmail(fromaddr, toaddr, text)
        except smtplib.SMTPRecipientsRefused:
            print(toaddr)
        except smtplib.SMTPSenderRefused:
            server.quit()
            time.sleep(10)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddr, text)

    server.quit()