FROM prestashop/prestashop

#ENV PS_INSTALL_AUTO=0
#ENV PS_ERASE_DB=9
#ENV DB_HOST=db
#ENV DB_USER=prestashop_be_180109
#ENV DB_PASSWORD=prestashit
#ENV DB_NAME=BE_180109

COPY ssl/*.crt /etc/ssl/certs/
COPY ssl/* /etc/ssl/private/

COPY ./be-presta-apache2-start.sh /bin
COPY ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf

RUN sed -i 's/.*error_reporting \= E_ALL \& \~E_DEPRECATED \& \~E_STRICT.*/error_reporting \= E_ALL \& \~E_NOTICE \& \~E_DEPRECATED \& \~E_STRICT/' /usr/local/etc/php/php.ini

RUN a2enmod ssl

