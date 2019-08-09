#!/usr/bin/python

#-*-coding:utf-8-*- 

#-*-coding:utf-8-*-

#filename :sendmail.py

import sys 

import smtplib

from email.mime.text import MIMEText

from email.header import Header

from email.mime.multipart import MIMEMultipart

from email import Utils

import getopt

import base64





smtp_server = '192.168.201.9'

mail_postfix='@deer-group.com'

username = base64.decodestring('c2VuZ3lp\n')

password = base64.decodestring('c2VuZzEyMzQ=\n')

flag_att=0

def usage():

	print ''' 

	-f or --from   Mail Sender

	-r or --recipients   Mail Recipients

	-s or --subject  Mail Subject

	-c or --content  Mail Content file path

	[-i] or --ip_w_upload Mail Attached file path, support asterisk wildcard

	[-u] or --user Auth user

    [-p] or --password Auth pass

	Examples:

	send mail:

	sendmail.py -f chenweibo -r chenweo,caog -s mysubject -c "test content"  -i './*.gif'

	send p_w_upload mail:

	sendmail.py -f chenweibo -r chenweo,caog -s mysubject -c "aaa content"  -i './*.gif'

	send mail with tar.gz attach:

	sendmail.py -f chenweibo -r chenweo,zhouda -s mysubject -c "hello world" './apache.tar.gz'

	'''

	exit(0)







def send_mail(sender,to_list,sub,content,user,passw):

	

	msg = MIMEText(content,_subtype='plain',_charset='gb2312')  

	msg ['Subject'] = Header(sub,'utf-8')

	msg['From'] = sender   

	msg['To'] = to_list  

	msg['Date'] = Utils.formatdate(localtime = 1)

	print msg['Date']

	smtp = smtplib.SMTP()

	smtp.connect(smtp_server)

	smtp.login(user,passw)

	for recipient in to_list.split(','):

		smtp.sendmail(sender,recipient, msg.as_string())

	smtp.quit





def send_att_mail(sender,to_list,sub,content,att,user,passw):



	msg = MIMEMultipart()

	msg['Subject'] = Header(sub,'utf-8')

	msg['From'] = sender  

	msg['To'] = to_list  

	msg['Date'] = Utils.formatdate(localtime = 1)

	print msg['Date']

	p_w_upload_file = att 

	att1 = MIMEText(open(p_w_upload_file, 'rb').read(), 'base64', 'gb2312')

	att1["Content-Type"] = 'application/octet-stream'

	att1["Content-Disposition"] = 'p_w_upload; filename='+p_w_upload_file.split("/")[-1]

	msg.attach(att1)

	#mail_context=MIMEText(content,'text','utf-8')

	mail_context = MIMEText(content,_subtype='plain',_charset='gb2312')  

	msg.attach(mail_context)

	smtp = smtplib.SMTP()

	smtp.connect(smtp_server)

	smtp.login(user,passw)

	for recipient in to_list.split(','):

		smtp.sendmail(sender,recipient, msg.as_string())

	smtp.quit

	

print sys.argv[1:]

if ( len( sys.argv ) == 1 ):

	print '-h or --help for detail'

	sys.exit(1)

shortargs = 'hf:r:s:c:i:u:p:'

longargs = ['help', 'from=', 'recipients=', 'subject=', 'content=', 'p_w_upload=','user=','password=']

opts, args = getopt.getopt( sys.argv[1:], shortargs, longargs )



print args

if args:

	print '-h or --help for detail'

	sys.exit(1)

	

for opt,val in opts:

	if opt in ( '-h', '--help' ):

		usage()

		continue

	if opt in ( '-f', '--from' ):

		sender=val+mail_postfix		

		continue

	if opt in ( '-r', '--recipients' ):

		receiver = val

		continue

	if opt in ( '-s', '--subject' ):

		subject=val

		continue

	if opt in ('-c','--context'):

		content=val

		continue

	if opt in ('-i','--ip_w_upload'):

		p_w_upload=val

		flag_att=1

		continue

	if opt in ('-u','--user'):

		username=val+mail_postfix

		continue

	if opt in ('-p','--password'):

		password=val

		continue



print flag_att

if flag_att==1:

	send_att_mail(sender,receiver,subject,content,p_w_upload,username,password)	

else:

	send_mail(sender,receiver,subject,content,username,password)
