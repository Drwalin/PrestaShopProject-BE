FROM prestashop/prestashop

RUN rm -rf /var/www/html/*
RUN chmod -R 777 /var/www/html/
RUN chown -R root:root /var/www/html
COPY ./vol-presta/* /var/www/html/
COPY ./vol-presta/.* /var/www/html/
COPY ./vol-presta/app/* /var/www/html/app/
COPY ./vol-presta/app/config/* /var/www/html/app/config/
RUN chmod -R 777 /var/www/html/
RUN chown -R root:root /var/www/html
RUN find /var/www/html/ > /home/tmp.tmp

COPY ssl/*.crt /etc/ssl/certs/
COPY ssl/* /etc/ssl/private/

COPY ./be-presta-apache2-start.sh /bin
COPY ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf

RUN sed -i 's/.*error_reporting \= E_ALL \& \~E_DEPRECATED \& \~E_STRICT.*/error_reporting \= E_ALL \& \~E_NOTICE \& \~E_DEPRECATED \& \~E_STRICT/' /usr/local/etc/php/php.ini
#RUN apt update -y
#RUN apt install -y vim fish

RUN a2enmod ssl

