# Chapter 4: Network Automation with Paramiko
# Full Stack Network Automation by Shahzad Qadir
# script7.py

import sys
import paramiko

def login(hostname, username, password):
    try:
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(hostname=hostname ,username=username, password=password, allow_agent=False, look_for_keys=False)
    except paramiko.ssh_exception.AuthenticationException:
        print("Invalid username/password")
        sys.exit(1)
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Could not connect to device, Invalid certificates")
        sys.exit(1)
    return conn

def execute_show_commands(conn, command):
    stdin, stdout, stderr = conn.exec_command(command)
    output = stdout.readlines()
    output = [line.strip() for line in output]
    return output

def print_to_screen(output: list):
    for item in output:
        print(item)

def print_to_file(output: list, filename: str, device_name: str):
    with open(filename, "a") as file:
        file.write(f"Device: {device_name}")
        file.write("\n")
        for item in output:
            file.write(item)
            file.write("\n")
        file.write("\n")


if __name__ == "__main__":
    cisco_devices = ["10.10.99.11", "10.10.99.12", "10.10.99.13", 
                 "10.10.99.14", "10.10.99.2", "10.10.99.3"]
    firewalls = ["10.10.99.1"]

    print("********************")
    print("Inventory")
    print("********************")
    print("1. Routers & Switches")
    print("2. Firewalls")
    print("Which type of devices you want to run command? ")
    device_type = ""

    while device_type not in ["1", "2"]:
        device_type = input("Enter Device type 1 or 2: ")    

    show_command = input("Enter show command: ")
    save_output = input("Do you want to print to file?: ")
    if save_output.lower() == "yes":
        filename = input("Filename with path: ")        

    if device_type == "1":            
        for device in cisco_devices:
            print(f"Device: {device}")
            device_connection = login(device, "script", "cisco123")
            outputs = execute_show_commands(device_connection, show_command)            
            if save_output == "yes":
                print_to_file(output=outputs, filename=filename, device_name=device)
            else:
                print_to_screen(output=outputs)
    elif device_type == "2":
        for device in firewalls:
            print(f"Device: {device}")
            device_connection = login(device, "script", "cisco123")
            outputs = execute_show_commands(device_connection, show_command)
            if save_output == "yes":
                print_to_file(output=outputs, filename=filename, device_name=device)
            else:
                print_to_screen(output=outputs)

