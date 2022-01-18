# !/bin/bash

mysql --user=root "-pstudent" -P 3306 < create_user.sql
mysql --user=be_180109_db_user "-pbe_180109_db_password" -P 3306 < ./../vol-db-dump/alldb.sql

