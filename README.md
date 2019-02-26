# Apache -> WSGI -> Flask Web app
**Flask Web App hosted on a LAMP server, with WSGI integration into Python**














#####################################
##Installing second instance of HTTPD

cp /usr/lib/systemd/system/httpd.service /usr/lib/systemd/system/httpd-py2.service; cp -pr /etc/httpd /etc/httpd-py2; cp /etc/sysconfig/httpd /etc/sysconfig/httpd-py2
mv /etc/httpd-py2/run/httpd.pid /etc/httpd-py2/run/httpd-py2.pid

vim /usr/lib/systemd/system/httpd-py2.service 
vim /etc/httpd-py2/conf.d/ssl.conf 
vim /etc/httpd-py2/conf/httpd.conf 
vim /etc/sysconfig/httpd-py2 
vim /etc/httpd-py2/conf.d/flask.conf 

semanage port -a -t http_port_t -p tcp 8080
semanage port -a -t http_port_t -p tcp 4443

systemctl daemon-reload 
systemctl start httpd-py2.service 

