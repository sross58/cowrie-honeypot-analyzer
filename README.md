# COWRIE SSH HONEYPOT SECURITY ANALYZER

This project is a python based security log analyzer designed to identify suspicious SSH authentication 
activity collected by a Cowrie honeypot. The honeypot runs inside an isolated Ubuntu virtual machine and records
simulated SSH login attempts, authentication failures, and commands entered by connected users. A custom Python
script processes Cowrie's JSON logs and generates a security report.

# Tools Used: 
- Python 3
- Ubuntu Linux 
- Cowrie SSH Honeypot
- VirtualBox
- Git

# HOW IT WORKS:
Cowrie records SSH activity in JSON log files. The python script reads through these logs and counts the 
different types of events. For login failures, the script groups the timestamps by IP address and checks whether
5 attempts occured within a 60 second period. If it finds 5 failed attempts within that time, it warns of 
possible brute force activity.

# TESTING: 
To test the analyzer, I connected to the honeypot locally and simulated SSH login attempts using different 
passwords. I configured Cowrie to generate failed authentication events and confirmed that my script could 
detect repeated failures within a short period. I also created 2 tests within a file to test 5 failed attempts within 45
seconds and 8 minutes. Both worked as expected, with the 45 second test generating an alert, and the 8 minute 
one does not.

# WHAT I LEARNED: 
This is my first project, and it helped me get more comfortable with Linux, configuring software and 
troubleshooting problems along the way. One of the things I learned was figuring out how Cowrie dealt with 
authentication. It initially accepted every password I tried, so no login failures were detected. After changing
some settings, I was able to generate the events needed to test the script.

# SECURITY:
Cowrie was configured to listen only on the VM's localhost interface. All SSH activity was simulated locally 
rather than exposing the honeypot to the internet. I've also excluded raw JSON logs from the GitHub repository
to avoid showing usernames and passwords. 

# FUTURE IMPROVEMENTS:
As I learn more about Python and cybersecurity I hope to revisit this project, including adding more 
detection rules for suspicious commands and improving error handling.
