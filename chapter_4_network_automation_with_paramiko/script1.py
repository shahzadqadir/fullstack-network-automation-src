# Chapter 4: Network Automation with Paramiko
# Full Stack Network Automation by Shahzad Qadir
# script1.py

import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(hostname="10.10.99.11" ,username="script", password="cisco123", allow_agent=False, look_for_keys=False)
stdin, stdout, stderr = conn.exec_command("show ip int brief")
output = stdout.readlines()
for line in output:
    if line != "":
        print(line.strip())
