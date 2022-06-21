#! /bin/bash

RND=$((RANDOM%5+1))

NUM_INTENTO=0

FOUND=false

while [ $FOUND != true ]
do
	echo "escriba una cifra de 1 a 5"
	read intento
	if [ "$intento" == "$RND" ]
	then
		echo "ENCONTRADO"
		FOUND=true
	else
		echo "Inténtelo de nuevo ..."
	fi
	NUM_INTENTO=$(($NUM_INTENTO+1))
done
echo "BRAVO Encontrado en $NUM_INTENTO intento(s)"
