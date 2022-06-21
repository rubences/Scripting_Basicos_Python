:
## -----------------------------------
## Ejecución de un comando por cron
## -----------------------------------

PYTHON=/home/chris/.virtualenvs/lps2/bin/python

## ------------------------
## Pequeña rutina de log
## ------------------------
log()
{
	stamp=$(date "+%j %X")
	echo ">>> $stamp : $1 "
}


DIR_BASE=/home/chris/dvp/scripting_linux_python/scripting_python_linux/src/db-activity-gestion
DIR_BIN=$DIR_BASE
DIR_LOG=$DIR_BASE/log

TS=$(date "+%j_%H%M%S")

FUNCION="${1-null}"
FIC_LOG=$DIR_LOG/${TS}_${FUNCION}.log

exec 1>$FIC_LOG
exec 2>&1

log "Inicio del tratamiento"

if [ -f $DIR_BIN/${FUNCION}.py ]
then
	log "Ejecución del comando: $FUNCION"
	( cd $DIR_BIN ; $PYTHON ${FUNCION}.py )
else
	log "Error Función: $FUNCION inexistente"
fi
log "Fin del tratamiento"
