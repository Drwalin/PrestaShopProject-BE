function wait_for_db()
{
	DB_HOST="localhost"
	echo ">>>>>>>>>Waiting for database..."
	while ! mysqladmin ping -h"$DB_HOST" --silent; do
    	sleep 1
    	echo "..."
	done
	echo ">>>>>>>>>Database ready"
}
SQL_PID=0

_term()
{
	be-db-export.sh
	kill "$SQL_PID"
	exit
}

trap _term SIGTERM

mariadbd &
SQL_PID=$!
wait_for_db
echo ">>>>>>>Database started."
echo ">>>>>>>Importing..."
be-db-import.sh
echo "--------------SERVER READY-----------------"
wait "$SQL_PID"
