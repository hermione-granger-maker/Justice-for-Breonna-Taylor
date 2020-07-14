import time
import random
import smtplib, ssl
from email.mime.text import MIMEText

receiver_email = ["greg.fisher@louisvilleky.gov", "attorney.general@ag.ky.gov", "wineicooke@lousvilleprosecuter.com", "Robert.schroeder@louisvilleky.gov"]
port = 465
smtp_server = "smtp.gmail.com"
# I do not reccomend using your actual email account for this
# because this makes it easier for others to gain access to your account.
# So, make a new account then
# turn Allow less secure apps to ON.

sender_email = ""  # Enter your address
password = "" # Enter you password

message = """Hello, My name is [first name] and I am a
 resident of [city, state]. I am emailing today to demand accountability in the
 unjust murder of Breonna Taylor. I demand that Jonathan Mattingly, Brett
 Hankison and Myles Cosgrove each be arrested and charged for 2nd degree
 murder for the wrongful death of Breonna Taylor. June 5th would
 have been Breonna’s 27th birthday but she is unable to celebrate  because
 on March 13th your police recklessly executed a raid using a “no knock”
 warrant on the wrong home. Despite your almost 3 months of
 inaction, Breonna’s life matters and I want justice for her.
 Sincerely, [first name last name]"""

# I formated the fill-ins so that the number of words will be divisable by
# 5. You need to adjust the code a bit if you would like the length of the
# message to be different

messageList = []
span = 5 # number of words that will appear in the subject

messages = message.split()
for i in range(0,len(messages), 5):
     messageList.append(messages[i]+ " " + messages[i+1]+ " " + messages[i+2]+ " " + messages[i+3]+ " " + messages[i+4])
messageList.reverse()

for word in messageList:
     # prevents emails from being marked spam
     sleepTime = random.randint(1,50)
     time.sleep(sleepTime/10)

     # message text (fill in your information again)
     msg = MIMEText("""Hello, My name is [first name] and I am a
 resident of [city, state]. I am emailing today to demand accountability in the
 unjust murder of Breonna Taylor. I demand that Jonathan Mattingly, Brett
 Hankison and Myles Cosgrove each be arrested and charged for 2nd degree
 murder for the wrongful death of Breonna Taylor. June 5th would
 have been Breonna’s 27th birthday but she is unable to celebrate  because
 on March 13th your police recklessly executed a raid using a “no knock”
 warrant on the wrong home. Despite your almost 3 months of
 inaction, Breonna’s life matters and I want justice for her.
 Sincerely, [first name last name]""")

     # message subject (you don't need to adjust anything here)
     msg['Subject'] = word
     print("sending email: " + word)
     with smtplib.SMTP_SSL(smtp_server, port) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, msg.as_string())

print("Your message has sent!")


