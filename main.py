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

    else:
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("Error: Unknown Command : Typo?", fg="red", bold=True, blink=True)

if __name__ == "__main__":
    assistant()
