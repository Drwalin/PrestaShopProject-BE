FROM mariadb

RUN echo "innodb_log_file_size = 20M" >> /etc/mysql/my.cnf
RUN echo "innodb_file_per_table = 1" >> /etc/mysql/my.cnf

COPY ./be-db-export.sh /bin
COPY ./be-db-import.sh /bin
COPY ./be-db-session.sh /bin

RUN sed -i 's/.*exec \"\$\@\".*/ exec be-db-session\.sh/' usr/local/bin/docker-entrypoint.sh 

RUN apt-get update && apt-get install -y pv

EXPOSE 3306
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mariadbd"]