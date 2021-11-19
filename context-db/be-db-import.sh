echo "Importing database from volume..."
pv -f /var/dbdump/alldb.sql | mysql -u root "-p$MYSQL_ROOT_PASSWORD"
echo "FLUSH PRIVILEGES; " | mysql -u root "-p$MYSQL_ROOT_PASSWORD"
echo "Importing complete."