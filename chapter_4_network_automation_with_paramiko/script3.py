# Chapter 4: Network Automation with Paramiko
# Full Stack Network Automation by Shahzad Qadir
# script3.py

import paramiko

def login(hostname, username, password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(hostname=hostname ,username=username, password=password, allow_agent=False, look_for_keys=False)
    return conn

def execute_show_commands(conn, command):
    stdin, stdout, stderr = conn.exec_command(command)
    output = stdout.readlines()
    for line in output:
        if line != "":
            print(line.strip())

if __name__ == "__main__":
    device_connection = login("10.10.99.12", "script", "cisco123")
    execute_show_commands(device_connection, input("Enter show command: "))
