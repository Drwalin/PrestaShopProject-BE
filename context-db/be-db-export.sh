echo "Exporting database to volume..."
mysqldump -u root "-p$MYSQL_ROOT_PASSWORD" --opt --all-databases --flush-privileges > /var/dbdump/alldb.sql
echo "Exporting complete."