FROM prestashop/prestashop

COPY --chown=www-data:www-data ./vol-presta/ /var/www/html/
RUN rm -rf /var/www/html/install
RUN rm -rf /var/www/html/admin
COPY ssl/*.crt /etc/ssl/certs/
COPY ssl/* /etc/ssl/private/

COPY ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf

RUN sed -i 's/.*error_reporting \= E_ALL \& \~E_DEPRECATED \& \~E_STRICT.*/error_reporting \= E_ALL \& \~E_NOTICE \& \~E_DEPRECATED \& \~E_STRICT/' /usr/local/etc/php/php.ini

RUN apt update -y
RUN apt install vim nmap iputils-ping -y

RUN a2enmod ssl

