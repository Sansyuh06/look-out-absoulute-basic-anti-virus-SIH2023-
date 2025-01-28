import socket
import os
import subprocess
import re
import ipaddress
import nmap
import winreg
import codecs
import pickle 
import sys
'''
panda=str(input('''enter your path 
O===(ZZZZZZZ>'''))
v=(socket.gethostname())
#ipaddress
a= (socket.gethostbyname(socket.gethostname()))
#hostname 
g= str(os.getcwd())
#file path

print('The Name of this user is '+v)
print('The ip address of this system is '+a)

'''
fp=open(panda,'r')
empty= fp.read()
test=str(empty)
print(test)
fp.close()
'''


#file 
def file_ext():
   cat_2=('type '+panda)
   cat_1=subprocess.run(cat_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
   if cat_1.returncode == 0:
       print("Command executed successfully")
       cmd_output = cat_1.stdout
       print("Command Output:")
       print(cmd_output)
   else:
       print("Command failed with an error")
       cmd_error = cat_1.stderr
       print("Command Error:")
       print(cmd_error)
   cat_3=str(cat_1)
   print(cat_3)
#file type 

file_ext()


def test_previlages():
   file_path=panda

   if os.access(file_path, os.R_OK):
       print(f"The file '{file_path}' is readable.")
   else:
       print(f"The file '{file_path}' is not readable.")
   if os.access(file_path, os.W_OK):
       print(f"The file '{file_path}' is writable.")
   else:
       print(f"The file '{file_path}' is not writable.")
   if os.access(file_path, os.X_OK):
       print(f"The file '{file_path}' is executable.")
   else:
       print(f"The file '{file_path}' is not executable.")

def file_size():
   path=panda 
   
   stats = os.stat(path)
   size = stats.st_size
   print(f"Size of the file is: {size} bytes")


def file_eater():
   sudo=str(input('''enter your path  
O===(ZZZZZZZ> '''))
   print('')
#step 2 is given below
   shred=open(sudo,'wb')
   junk='''
eyJtZXNzYWdlIjoiMTVkNTRjZWI1ZmNlMDU2N2I5NjJhZjg1Yjk0OWEzM2Q4
MWUxYmEyMzA3ZWFjNzJiMzJkMGYzZjdlODRmMjQzYmFiZWM1MzNhYTQzYWZh
NTY3Y2Q2ZmQ5ZDQyNjMwOTNjODM4Y2RiMGNiZWYyNmQxMGJkYTJlZjg4NGU1
MzY0M2JmY2JhNGU3MTk1YmE5ZWY3OTU0NjlhYzRjMDQyZjhkYzEzZmNmZDQ0
ZDRmZDY4NTk0NzI5MjgyN2E0ZjljYTU1NmM2MjQ4ODhlYTJjNjRlYjQ4YmY0
YTVkOGQwY2JlYTZiZTZjNWJjMDI0OTdlZmU4NWNmNzI4MDIyODE2ZmM1ZGNj
NjI3MWY2MjYzMDI3NWNjNWRhNThiZTVlY2FlNmM4ODhmMTYzYTVlODIyY2Fk
MDdkYjkwZTVlZDczYmI3NDdiYzI4YTA5YmYxNDhmNDgyOGFkMTRhMDdkOWZh
ODM3OWE0N2MyNTU5YmNkNmFiZDcwNzhkYjc4MTkyYmUxZmFlNmI5NjExZjJi
NzNkZDM2YTUxODM2ZDRjZDU3ZTBkNWFjNTM1ODFhYmJmNTE2ZWI0NWQxNmQ0
YzE5NDA4MTljNTg4MDU4MGJkNWJjNzFjOGYwMzc3ZTYzNzQxNTExNTNkZmQ2
NmM4MjllNjQwNDYwYTRiZGQ0NGQ1MzA2N2I0Nzc4ODIyNjYyNzU4YmNlZjBm
ZmIwNzE3ODkwYmM0MDQ3NDRjNjcyMTVmNjA2ZjJjZjA2NTNlMzgyM2EzZGYz
YWYwZDY5ZGJkNDc0N2ZiM2FlYzAxM2ZmZjZlZjQyMTVhYmNjZmJjNzczMjc1
OTk5ZGVkZGMxZjk4MTZmNzZiN2NmMTNjMzAxZWYwYWRjZmM3YWNiMDhkNmU4
M2ZiYThmNjZhMjhlYzEyNGFlMGNhZDlmMDE4Mzk3OTBhNDc3YjgyYjFjZTY5
ZjJlM2Y2ZDkwZDUwMThhYmM0NzUwMTE3ODhhZjY1MDE4ZWUwNDc3NGEzM2Jl
MDM4NmY1YWRjZmNlOTJjNjUyM2U0MDQ1N2M5NjkwNWExNTE0NWUxOWJlOTdi
MmM2NmRjZWQwZTU3Yzk4MWM5ZGM5MTEzMWNmZmM2NDI1YWMzM2MyOGY0MzBl
N2I2ZGRlODc2MTQ4ZDMyMzI5MWZhMjdiZjVjNjk1ZDM1ZWYwMDdiZTIzNWI1
MDhmOTAzYjdlNDhkMDRlNWVlODRhNTJhOWMwMGNhYTc3MGYyMWQxNGM1ZDM5
N2E2YzBhNWQ4OWZlZjAzZDA3NGM2ODAwOTEyNWQ4YThlMWE5ZjllYmI0YTJi
YTAwMGM5NGRmMTE3ZDBlMDA0NzcyYjI0YzBhZDQ2ZmE1MGNkMzQwMzM4ZjUx
ZWZlMjUyYWQ0ZjdkNDY0MTAzNWM0OWZkOWNiYWQzODc4ZTE2MGE0MDI5YjYy
NjBhMmYxZjZhZjhkNmNmMTY0NjRjM2U0Y2ViNTFiMWQyZGM3NWE4YzQ4NGQ3
ODRiZDcyZTVjNTQ1YjBmNTMzNTU0YzQ1NTYwNDZhNzU2NjhkNmNmY2YxYzc1
NTVjODRiODljMjU5ZThhYWY5YTcwYjQ5OThhMzVlNzZhNmQzYWNkYzQ0NWJk
ZmI3Y2Y3NGM0NGNlYTk0NDEyOWNkODBmZWQ1NTYxNGIzMjM1NjE0ZjE2MjMx
ZjFhMjBiMmQzYmI5ZGVkYTI4MmI0OWNiMWYwMjI2ZjQ3MDhlOTVkYTk2YTZk
ZWVjYjNmMmI1OGVjOWMyZjM4N2EzNzE3Zjc0NDU1ZTVlMTUyYjIyMmIzNDMy
MGJlNjRhOGNkMmU5MTk2OTllOWIzNzEyMWIxMGExNTg3OTkwZmRkYzU0MzQ2
YTNkYTM5YTNjMTM5MDg5OTJlNTZjMzY3MjE3MTk2OTBjNTE3YWYwMGI4MGFh
YmJjYWEwZjU0YmE4NzBkOWNkNjkyNGZiOGViYjM0OGExMDg5OTBhYzJkMWM3
Nzg0NzA5ZTVlOTVkN2ZjMmQwMDRkNjFiYjJiMmU5NWYwNTQ3NWUyNmE3Zjdk
MjNjMzQ0MjNiOGI5YjQ1YzIyYWNiOWI3ZGE0ZGU1NTQzYWM4MjA3MWE0ZTA1
NzQ4MTlmMWE1YjE4YTdhOTUyNTUxOWM4MmQ5Nzc1NjQ0ODhmN2Q3YTQ3NjIy
ZTdhMjAxN2QxYWE0ZTFkNmQzNWE4NjIzMTM1NWY5ZTlkY2QyZGFhM2JhNjQ5
MzQ2Mzk5NTg5NGY5ZGYzYjk2YTc1YjdiM2ZhMDMxODhkMTRkYTVlMDBhZTZl
NDlmOWE1YTI4YWZkZDIwNGQ5OWE1YzBkYjJmZjQ4MDlkMzNiMWUxOTFlMWIz
MWNjNjMyMWFiZWUyZDk2MTQwMDljMTljMTUzNDNhYjY5MWNjMDAwN2Q3YzQz
MmI4OGRjMDk2YzU2MDM2OTA4Y2ZmMDZhMjlhYjA2NDUwZDJkODljMTRjOTMz
NDRjZjZlMzBiMGRiMTNmMzFkY2I4MDk4NjEzZWM4NDVjMjJlZmEyZDc2YzNl
MTMyOTc1NDRmYTRhNWE5ZjA3NDM4OThjY2ZiODI1YTYzZGNmNGIyNjAxYWI2
MzQ5YzU1NjE0MjEzMTRhOWEzYmUyMDQ0ZTVlNjAzMmI4YzE5OGJlZWY5ZGE0
ZmQ3Zjk1NWE5YWQ5OTEwN2Y1MzkwOTM2YTlkNWYzYmZiOWQzNzBiNjMwYzA5
MjAzOWE0Mjk3YTE3Mjg5NzkzOGRmY2ExODJjNjU2ODQ0NzEyOTEyNTNmMDQ1
ZTc2NTMwNjdlOWNjOWRjMTk4NTViNjU5MWM4OGQwYjllOTEyODFhOGMwZTRh
NmM0NjhmNWFmMzIwYmY1ZmFkYmFjYmI0NmFlZjg1OTBhZTQwOWUwNmExYjFj
MTJmNWQxYTE4Njg5OGU4NzJlMzFmZTJmMjZiZGVlYTk0MTdmMWRiYWZkMzc2
ODllOTU1YjMyYWRjMWZlOWFiZThjYTQ2NGEyMWNkM2Q0ZThkYThmNzFlM2My
MWUxZGY0YWJlNGNiZDNjMDQ5YzA2MGE2ZWQ0OTBlNTg1ZTFiODU4NzBhZjE3
ZTU4MDM2ZjU3ZmFmMGM3OTljZGE0ZGY4MjFlMWRlMTA2M2JmZmZiMjRiYjU4
N2VjMWZiZGNlNzQ1ZGRmMzk0YjE0MjdlZDEyZmE3MzczZmQ2MWI5NWEwNDg4
NGNhNDZhMmMwNzYzNzdmMWNhYjRmNmY2NWI5ZjZmMGZhMmE2MTlkOGNjMjAy
OGFkYmM3YzU5NDcxZTQ1MTYyZWVlMDQ1MWRmNzE1MDA4Y2I3MmJiNDU5YmE1
OWY3MTYzNDhjMjA4NmZiNWJmZDY3YjVhYTQ3MTA2NWZmOTU5MThjMTFlYmEx
MTNkYjI1NDNhMWU5Nzc1YWVhYzhiODgzYWZmNWIxMTc5Zjc3ZDFjMTUxNzJk
MjI3ZjQ1MWRiN2ZjMThjYjhhNjI3ZTJiMjkxYTVhYjE3MWJkMjZjNjM0ZDU5
ZWM0OTkyOWNlN2JjODM5MDgwNzIzY2Y2OGY0ZDUwYTlmOGY5NTQ0NTExZTUz
NDUxMTdhODc1NTFlOWJmZmUxYWMwZWQ4NTU1NTI1MDZmOGVlMjMwODQwMGY1
N2I1MTQ4ZjVjZDg0ZjA0NjNiNDJiMzM5NzdhZTlhNzkiLCJzaWduYXR1cmUi
OiI0ZTlhMWY5YThkZmJjOWYzYjZiZGFhMzNhNDI3MzUyYzA2ZmVmYWQyZmMx
YzMzODk0YmRmMzlkNjFmYzFhYzEyN2NlOGQwNTNjNzE1N2MyOWRmMWRhYWNl
MTNiODVmN2MxNjg0ODUzNjBmNzMzZGUyNmRlNTlhZjU1YmRhOWQ5NWUwNTQ4
OGRjMzE2NDM4MTEzNzRlODY5MGZkMjYwYjNmZjQ3YjMwMDE0MWZhZjE0N2M4
MjBiNjRkNmY4YmU0YWI1NDU4Mzg4YjQ2ZGY4MjQ0MThjODY5MGQ5M2RiM2E3
NjM4ZDI5NGRhZTEwNTFmNWY3YTIyMmU0YmI5ZDVhYTYzMjJkNDRlYjk4ZjI0
MjQ2NDEwMTg5NWQ4MjUyY2I0YTY5ODU5NmQ3NGM4YzgxM2U1NThlMTIwZGYz
ZWVlMmYyNjk5Y2VjMjdhZjdjMmZhMjNjNDMxODU4OTRiYmEyYmE4OGNlNzBj
MjE0ZWMwZjM1ODQ0OWI2ODc1ZWJhYjE5NDU5NjJlZGQ1NTBmMWE4MDZiNmE2
NzE2N2ViYmRlODEzNTFhMmU1ZDJhYzJiZDEyZTc2ODdkZDIwYmI2Y2YzOTBh
N2ZmYWJmNmZiNjJmMzY3MGU3NSJ9Q7b4g8W0z5a9x2mv1yHJID8A289sd2G8
YjVkNWE5ZGVhY2I1OGNkZjE4NmYzMjljYTRkY2VhNDJlMsWFjNGNiZjVmNmIz'''
   with open(sudo, 'r') as fin:
       data = fin.read().splitlines(True)
   with open(sudo, 'w') as fout:
       fout.writelines(data[1:])
   for i in range (18525): 
       pickle.dump(junk,shred)
   shred.close()
   if os.name == 'nt':
      os.system('del '+sudo)
   else:
      os.system('rm '+sudo)
   sr='  EUTHANIZED FILE !!!'
   file=open(sudo, "wb")
   for i in range (18525):
       pickle.dump(sr,file)
   file.close()
   if os.name=='nt':
      os.system('del '+sudo)
   else:
      os.system('rm '+sudo)
   
