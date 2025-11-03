# Chapter 4: Network Automation with Paramiko
# Full Stack Network Automation by Shahzad Qadir
# script4.py

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
    inventory = ["10.10.99.11", "10.10.99.12", "10.10.99.13", 
                 "10.10.99.14", "10.10.99.1", "10.10.99.2", "10.10.99.3"]
    show_command = input("Enter show command: ")
    for device in inventory:
        device_connection = login(device, "script", "cisco123")
        execute_show_commands(device_connection, show_command)
