# Importing Modules
import click
import datetime
import os
import sys
import time
import platform
import socket

# Functions
# DNS Flusher
def dns():
    while True:
        time.sleep(5)
        os.system("ipconfig /flushdns")
        time.sleep(1)
        os.system("cls")
        print("Waiting 5 minutes...")
        time.sleep(300)


# IP Fetcher
def get():
    try:
        addr = input("Enter Host Address: ")
        x = socket.gethostbyname_ex(addr)
        print(x)
    except socket.gaierror:
        x=[]
    return x

# System Info
def info():
    system_name = platform.system()
    node_name = platform.node()
    processor_name = platform.processor()
    python_version = platform.python_version()

    print(f"System Name: {system_name}")
    print(f"Node Name: {node_name}")
    print(f"Processor Name: {processor_name}")
    print(f"Python Version: {python_version}")


# Commands
@click.command()
@click.option("--c", "--command", type=str, default="nil")
def assistant(c):
    if c == "dns-flush":
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("- Flushing DNS", fg="red", bold=True)

        dns()

    elif c == "ip-fetch":
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("- Feteching IP", fg="red", bold=True)

        get()

    elif c == "sys-info":
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("- Fetching System Information", fg="red", bold=True)

        info()

    else:
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("Error: Unknown Command : Typo?", fg="red", bold=True, blink=True)

if __name__ == "__main__":
    assistant()
