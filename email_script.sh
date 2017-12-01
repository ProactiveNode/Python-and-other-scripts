#!/bin/bash
#Wanted to send an email every 10 minutes to test email server as well as webmail. 
#Used crontab to schedule the bash script to run every 10 minutes.
#Tested on Ubuntu 16.04 

email_date=$(date +%D_%R)
echo -e "Subject: Test Email at $email_date \n\n Here is some content to use" | /usr/sbin/sendmail inputRecipient@domainname
