#! /bin/bash

get_lista()
{
	LISTA=$(ls *.odt | grep -v table_de_materias)
	for i in $LISTA
	do
		odt2txt $i | grep -i '#' | grep -i 'archivo' | grep ':'
	done
}


get_lista | cut -d: -f2 | tr -d ' '
