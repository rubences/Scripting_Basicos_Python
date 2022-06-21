## -------------------
## Script de base
## -------------------

BASE_DIR=$(pwd)

## +%j da el número de días en el año
## Permite de tener un archivo para cada día y un histórico de un año
TS=$(date "+%j")
LOG=$BASE_DIR/log/${TS}.log

## Vamos a los fliujos estándares

exec 2>&1
exec 1>$LOG

## -----------------------
## Pequeña rutina de log
## -----------------------
log()
{
	msg="${1}"
	ts=$(date "+%j %X")
	printf ">>> ${ts} : ${msg}\n"
}

## Función principal 
compute()
{
	echo "Trabajo..."
	sleep 5
}


## -----------
## MAIN
## -----------
log "Inicio del tratamiento"
compute
log "Fin del tratamiento"
