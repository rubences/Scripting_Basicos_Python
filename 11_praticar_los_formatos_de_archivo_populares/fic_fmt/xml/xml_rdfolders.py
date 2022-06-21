import xmltodict
import pprint
import json

def print_sol(self):
    print("Soluciónn : %s / %s " % (self.name, self.mainport ))
    fmt = "{:20s} | {:15s} | {:10s} | {:s}"
    for m in self.modules:
        print(fmt.format(m.name, m.family, m.typ, str(m.params)))


archivo = 'FOLDERS.xml'

with open(archivo) as fd:
    doc = xmltodict.parse(fd.read(), process_namespaces=True)

folders = doc['INFOFOLDERS']['ACTUAL']['FOLDER']


fmt_tit = "{:10s}|{:10s}|{:10s}|{:10s}|{:10s}|{:45s}|"
titulo = fmt_tit.format( "DOSSIER", "Version", "Release", "Patch", "Update", "Langages" )
print(titulo)
print("-" * len(titulo))


#fmt = "{@ID:10s}|{VERSION:10s}|{RELEASE:10s}|{PATCH:10s}|{UPDATE:10s}|{LANGS:45s}|"
fmt = "{@ID:10s}|{VERSION:10s}|{RELEASE:10s}|{PATCH:10s}|{UPDATE:10s}|"

for f in folders:
    print( fmt.format( **f ) )
