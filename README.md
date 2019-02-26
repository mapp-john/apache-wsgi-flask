# Apache -> WSGI -> Flask Web app
### *Flask Web App hosted on a LAMP server, with [WSGI integration](https://pypi.org/project/mod_wsgi/) into Python3*

More details regarding [WSGI Configuration](https://modwsgi.readthedocs.io/en/develop/configuration.html)
## Install Apache HTTPD 2.4 
```
yum -y install httpd24 httpd24-httpd-devel
```
## Install Python3
```
yum -y install yum-utils
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python35u
yum -y install python35u-pip
yum -y install python35u-devel
```
## In order to integrate Apache and Python, we need to install WSGI.
#### Do not use ```yum -y install mod_wsgi```, because by default it will be built with Python2.
#### Instead, use PIP to install, then copy to the ```/etc/httpd/modules```
```
cp /usr/local/lib/python3.5/site-packages/mod_wsgi/server/mod_wsgi_3.5.so /etc/httpd/modules/mod_wsgi_3.5.so
```

## Python2
**If you have an app that requires Python2, you can run simultaniously with the Python3 app.**
**However, it does require a secondary installation of HTTPD2.4**
**You will then need to repeat the above steps for WSGI installation into the HTTPD_PY2 modules**


## Installing second instance of HTTPD
**Copy and modify HTTPD service, config, and system files**
```
cp /usr/lib/systemd/system/httpd.service /usr/lib/systemd/system/httpd-py2.service; cp -pr /etc/httpd /etc/httpd-py2; cp /etc/sysconfig/httpd /etc/sysconfig/httpd-py2
mv /etc/httpd-py2/run/httpd.pid /etc/httpd-py2/run/httpd-py2.pid

vim /usr/lib/systemd/system/httpd-py2.service 
vim /etc/httpd-py2/conf.d/ssl.conf 
vim /etc/httpd-py2/conf/httpd.conf 
vim /etc/sysconfig/httpd-py2 
vim /etc/httpd-py2/conf.d/flask.conf 
```
**modify SElinux to allow the secondary service to communicate**
```
semanage port -a -t http_port_t -p tcp 8080
semanage port -a -t http_port_t -p tcp 4443
```
**Reload systemctl**
systemctl daemon-reload 
systemctl start httpd-py2.service 

