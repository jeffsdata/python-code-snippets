import os
import requests
from datetime import datetime

class MailgunEmailer:
    def sendEmail(self, emailto, subjectmain, subjecttext, bodytext):
        mailgun_key = os.getenv("MAILGUN_KEY")
        return requests.post(
            "https://api.mailgun.net/v3/mg.redoxic.com/messages",
            auth=("api", mailgun_key),
            data={"from": "Jeff Anderson <janderson@mg.redoxic.com>",
                "to": [emailto],
                "subject": subjectmain + ": " + subjecttext,
                "text": bodytext})

def main():
    rb = MailgunEmailer()
    rb.sendEmail("xxxxxxxxxxxxxxx@gmail.com", "log - job complete", f"the python job is complete. {datetime.now()}", "this job finished. It really did!")

if __name__ == '__main__':
    main()