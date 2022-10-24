## connect to gmail, search mails, download attachments
# Vaishnavi Acharya Date: 24/10/2022

import email
import getpass
import imaplib
import base64
import os
import sys

userName = 'yourmail@gmail.com'
passwd = 'Authentication-key'
host = 'imap.gmail.com'


detach_dir = '.'
if 'DataFiles' not in os.listdir(detach_dir):
    os.mkdir('DataFiles')

print(os.getcwd)


try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    print(imapSession)
    typ, accountDetails = imapSession.login(userName, passwd)
    print(typ, accountDetails)
    if typ != 'OK':
        print('Not able to sign in!')
        raise

    print('signed in')

    imapSession.select('Inbox')
    typ, data = imapSession.search(None, 'Subject', '"Data from production"')
    print('searching')
    if typ != 'OK':
        print('Error searching Inbox.')
        raise
    print('done search')

    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        print(msgId)
        if typ != 'OK':
            print('Error fetching mail.')
            raise

        print('done fetch')

        emailBody = messageParts[0][1]
        mail = email.message_from_bytes(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            print(fileName)

            

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'DataFiles', fileName)
                
                print(filePath)
                if not os.path.isfile(filePath) :
                    print(fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()

    print('Done')


except :
    print('Not able to download all attachments.')

    
    
