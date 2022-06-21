import struct 
 
wtmp_struct = { 
       'type'         : 'i',        # 4 bytes 
       'process_id'   : 'i',        # 4 bytes 
       'DeviceName'   : '32s',             # C-string de 32 
       'Inittab_id'   : '4s',       # C-string de 4 
       'Username'     : '32s',             # C-string de 32 
       'padding'      : '308x',     # relleno 
   } 
 
## construcción de la estructura para unpack 
st = ''.join(wtmp_struct.values()) 
 
## cálculo de la longitud del registro 
len_record = struct.calcsize(st) 
 
print("St=%s: %s " % (st, len_record)) 
 
archivo = '/var/log/wtmp' 
 
with open(archivo, 'rb') as fic: 
   EOF=False 
   while not EOF: 
       record = fic.read(len_record) 
       if len(record) != len_record: 
           EOF=True 
       else: 
           lig = struct.unpack(st, record) 
           l_typ       = lig[0] 
           l_pid       = lig[1] 
           l_device    = lig[2].decode('ascii') 
           l_init      = lig[3] 
           l_user      = lig[4].decode('ascii') 
           print(" %s %s " % (l_device, l_user))
