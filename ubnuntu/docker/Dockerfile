FROM debian:latest

RUN apt update && apt upgrade -y

RUN apt install -y sudo ca-certificates apt-transport-https wget gnupg2 curl memcached vim nano

RUN apt update

RUN apt install -y php7.3 php7.3-cli php7.3-common php7.3-curl php7.3-mbstring php7.3-mysql php7.3-xml php7.3-bcmath php7.3-bz2 php7.3-cgi php7.3-cli php7.3-common php7.3-curl php7.3-dba php7.3-dev php7.3-enchant php7.3-fpm php7.3-gd php7.3-gmp php7.3-imap php7.3-interbase php7.3-intl php7.3-json php7.3-ldap php7.3-mbstring php7.3-mysql php7.3-odbc php7.3-opcache php7.3-pgsql php7.3-phpdbg php7.3-pspell php7.3-readline php7.3-recode php7.3-snmp php7.3-soap php7.3-sqlite3 php7.3-sybase php7.3-tidy php7.3-xml php7.3-xmlrpc php7.3-xsl php7.3-zip

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list

RUN wget http://nginx.org/keys/nginx_signing.key && apt-key add nginx_signing.key

RUN apt update && apt install nginx

RUN apt-get update && apt-get install -y locales apt-transport-https && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 && apt-get install -y unixodbc-dev

RUN sudo pear config-set php_ini 'php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"' system && pecl install sqlsrv && pecl install pdo_sqlsrv && echo "extension=sqlsrv.so" >> /etc/php/7.3/fpm/php.ini && echo "extension=sqlsrv.so" >> /etc/php/7.3/cli/php.ini && echo "extension=pdo_sqlsrv.so" >> /etc/php/7.3/fpm/php.ini

RUN mkdir -p /var/www/html && chmod -R 777 /var/www/html && rm -rf /var/www/html/* && mkdir -p /etc/nginx/ssl/ && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj "/C=GR/ST=greece/L=athens/O=c2/OU=devops/CN=ss.peppercode.gr"

RUN rm -rf /etc/nginx/conf.d/*

RUN usermod -a -G www-data nginx

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 80
EXPOSE 443
VOLUME ["/var/www/html"]
ADD ./default /etc/nginx/conf.d/default.conf

ENTRYPOINT service nginx start && service memcached start && service php7.3-fpm start && /bin/bash && tail -f /dev/null
