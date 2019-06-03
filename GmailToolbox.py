__author__ = 'KattStof'
#! python3
# GmailToolbox - A toolbox to do automated cleanup + sending
import imapclient, smtplib, getpass, time
print('####################')
print('######GMAIL#########')
print('######TOOLBOX#######')
print('####################')
print('1) Delete Entire Inbox')
print('2) Delete Emails From Specified Address From Inbox')
print('3) De-Spam Inbox')
print('4) Send Mass Email')
print('5) Email Bomber')
choice = input('Enter Option: ')
if choice == '1':
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    email = input('Enter Your Email Address: ')
    password = getpass.getpass()
    imapObj.login(email, password)
    imapObj.select_folder('INBOX', readonly=False)
    UIDS = imapObj.search(['All'])
    print('Deleting')
    imapObj.delete_messages(UIDS)
    imapObj.expunge()
    print('Finished!')
    imapObj.logout()

if choice == '2':
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    email = input('Enter Your Email Address: ')
    password = getpass.getpass()
    imapObj.login(email, password)
    imapObj.select_folder('INBOX', readonly=False)
    OtherEmail = input('Enter Email Address To Delete: ')
    UIDs = imapObj.gmail_search(OtherEmail)
    print('Deleting')
    imapObj.delete_messages(UIDs)
    imapObj.expunge()
    print('Finished!')
    imapObj.logout()

if choice == '3':
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    email = input('Enter Your Email Address: ')
    password = getpass.getpass()
    imapObj.login(email, password)
    imapObj.select_folder('INBOX', readonly=False)
    txt = input('Enter Txt File With List Of Email Addresses: ')
    list = [line.strip() for line in open(txt, 'r')]
    print('Deleting')
    for line in list:
        UIDs = imapObj.gmail_search(line)
        imapObj.delete_messages(UIDs)
        imapObj.expunge()
    print('Finished!')
    imapObj.logout()
if choice == '4':
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = getpass.getpass()
    password = getpass.getpass()
    smtpObj.login(email, password)
    from_email = input('Enter From Email: ')
    txt = input('Enter txt File With List Of Email Addresses: ')
    list = [line.strip() for line in open(txt, 'r')]
    subject = input('Enter Email Subject: ')
    body = input('Enter Email Body: ')
    print('Sending')
    for line in list:
        smtpObj.sendmail(from_email, line,'Subject:' + subject + '\n' + body)
    print('Done!')
    smtpObj.quit()

if choice == '5':
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = input('Enter Your Email Address: ')
    password = getpass.getpass()
    smtpObj.login(email, password)
    from_email = input('Enter From Email: ')
    to_email = input('Enter Email Address To Bomb:')
    subject = input('Enter Email Subject: ')
    body = input('Enter Email Body: ')
    ammount = int(input('How Many Emails to send?:'))
    for i in range(ammount):
        print('sending ' + str(i + 1))
        time.sleep(1)
        smtpObj.sendmail(from_email, to_email,'Subject:' + subject + '\n' + body)
    print('Finished!')

