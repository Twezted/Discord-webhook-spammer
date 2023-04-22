import requests
from colorama import init, Fore, Style

init()

print(Fore.GREEN + Style.BRIGHT + """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗           
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗  
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                               
""")

print(Fore.YELLOW + Style.BRIGHT + "\nHola mi amigo! Bienvenido\n")

webhook_url = input(Fore.CYAN + Style.BRIGHT + "Please enter the Discord webhook URL: ")
message = input(Fore.CYAN + Style.BRIGHT + "Please enter the message to spam: ")
count = int(input(Fore.CYAN + Style.BRIGHT + "Please enter the number of times to spam the message: "))

print(Fore.YELLOW + Style.BRIGHT + "\nSpamming the message...\n")

for i in range(count):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print(Fore.GREEN + Style.BRIGHT + f"Message {i+1} sent successfully!")
    else:
        print(Fore.RED + Style.BRIGHT + f"Failed to send message {i+1}!")

print(Fore.YELLOW + Style.BRIGHT + "\nAll messages have been sent!")
