import psutil 
import humanfriendly as hf 
 
AC = 'ACCESS_DENIED' 
USERNAME = 'chris' 
 
total_rd = 0 
total_wr = 0 
 
for proc in psutil.process_iter(): 
   with proc.oneshot(): 
       pinfo = proc.as_dict(attrs=['pid', 'name', 'username',  
'io_counters'], ad_value=AC) 
       if pinfo['io_counters'] != AC: 
           if pinfo['username'] == USERNAME: 
               total_rd += pinfo['io_counters'].read_chars 
               total_wr += pinfo['io_counters'].write_chars 
 
print( "Para el usuario: %s " % USERNAME ) 
print( "Total de caracteres leídos: %10s" % hf.format_size(total_rd)) 
print( "Total de caracteres escritos: %10s" % hf.format_size(total_wr))
