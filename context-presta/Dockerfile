FROM prestashop/prestashop

COPY ./vol-presta/ /var/www/html/
RUN chmod -R 777 /var/www/html/
COPY ssl/*.crt /etc/ssl/certs/
COPY ssl/* /etc/ssl/private/

COPY ./be-presta-apache2-start.sh /bin
COPY ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf

RUN sed -i 's/.*error_reporting \= E_ALL \& \~E_DEPRECATED \& \~E_STRICT.*/error_reporting \= E_ALL \& \~E_NOTICE \& \~E_DEPRECATED \& \~E_STRICT/' /usr/local/etc/php/php.ini

RUN a2enmod ssl

