import pexpect 
import datetime 
 
servidor = "X.X.X.X"    # a adaptar 
username = "anonymous" 
password = "root@ejemplo.com" 
 
child = pexpect.spawn ('ftp %s' % servidor) 
child.expect ('Name .*: ') 
child.sendline (username) 
child.expect ('Password:') 
child.sendline (password) 
child.expect ('ftp> ') 
 
for fic in [ 'help', 'info', 'install' ]: 
   child.sendline ('get %s' % fic) 
   child.expect ('ftp> ') 
for fic in [ 'prnlog', 'stat', 'syslog' ]: 
   fic_ts = fic+"_"+datetime.datetime.now().strftime('%Y%m%d_%H%M%S') 
   child.sendline ('get %s %s' % (fic, fic_ts)) 
   child.expect ('ftp> ') 
 
child.sendline ('sale')


#-r--r--r-- root root 200 Jan  1 01:08 help
#-r--r--r-- root root 200 Jan  1 01:08 info
#-r--r--r-- root root 200 Jan  1 01:08 install
#-r--r--r-- root root 200 Jan  1 01:08 prnlog
#-r--r--r-- root root 200 Jan  1 01:08 stat
#-r--r--r-- root root 200 Jan  1 01:08 syslog

