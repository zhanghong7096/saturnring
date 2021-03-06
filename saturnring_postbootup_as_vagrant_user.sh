#!/bin/bash
#Copyright 2014 Blackberry Limited
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
source ./envvars.sh

cd $INSTALLLOCATION
#Get latest saturnringsoftware from master branch
#git clone https://github.com/sachinkagarwal/saturnring/
cd $INSTALLLOCATION
if [ $INSTALLLOCATION != $CODEROOT ]; then
  cp -R $CODEROOT .
fi
if [ ! -d "$INSTALLLOCATION/saturnenv" ]; then
  virtualenv saturnenv
fi
cd $INSTALLLOCATION/ssddj
source $INSTALLLOCATION/saturnenv/bin/activate
pip install -r $INSTALLLOCATION/python-virtualenv-requirements.txt --allow-external django-admin-changelist-stats  --allow-unverified django-admin-changelist-stats

cat <<EOF > $INSTALLLOCATION/ssddj/saturn.ini
[saturnring]
#Cluster name: This is used as the stats Excel XLS filename
clustername=$CLUSTERNAME


#This is where the Saturnring picks up scripts to install on the saturnnode for things like creating/deleting iSCSI targets
bashscripts=globalstatemanager/bashscripts/

#The user needs to copy the corresponding public key to the saturn node's user (specified in the [saturnnode] section using e.g. ssh-copy-id
privatekeyfile=$SATURNWKDIR/saturnringconfig/saturnkey

#This is where saturnring keeps the latest iscsi config file
iscsiconfigdir=$SATURNWKDIR/saturnringconfig/

#Django secret key (CHANGE in production)
django_secret_key=$DJANGOSECRETKEY

#Logging path
logpath=$SATURNWKDIR/saturnringlog

#Number of queues
#If you change this number then please adjust the /etc/supervisor/conf.d/saturnring.conf by adding or deleting queue entries out there
numqueues=$NUMWORKERS

#Proxyfolder
#This is the proxy subfolder if the application is being run behind a proxy
proxyfolder=$PROXYFOLDER

[database]

dbtype=$DATABASE_TYPE
dbname=$DATABASE_NAME
dbhost=$DATABASE_HOST
dbport=$DATABASE_PORT
dbuser=$DATABASE_USER
dbpassword=$DATABASE_PASSWORD
dbdir=$DATABASE_DIR

[saturnnode]
user=$INSTALLUSER
#Location on the saturnnode where the scripts are installed.
install_location=$INSTALLLOCATION/saturn/
bashpath=/bin/bash
pythonpath=/usr/bin/python

[activedirectory]
enabled=$LDAP_ENABLED
ldap_uri=$LDAP_LDAP_URI
user_dn=$LDAP_USER_DN
staff_group=$LDAP_STAFF_GROUP
bind_user_dn=$LDAP_BIND_USER_DN
bind_user_pw=$LDAP_BIND_USER_PW

[tests]
saturnringip=$HOSTNAME
saturnringport=80
#saturniscsiserver=172.19.157.201

EOF

python manage.py syncdb --noinput
python manage.py convert_to_south ssdfrontend
python manage.py schemamigration ssdfrontend --auto
python manage.py migrate


cd $INSTALLLOCATION/ssddj
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '$ADMINEMAIL', '$SATURNRINGPASSWORD')" | python manage.py shell

cat <<EOF > /var/www/saturnring/index.wsgi
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('$INSTALLLOCATION/saturnenv/$INSTALLUSER/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('$INSTALLLOCATION/ssddj')
sys.path.append('$INSTALLLOCATION/ssddj/ssddj')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ssddj.settings'

# Activate your virtual env
activate_env=os.path.expanduser("$INSTALLLOCATION/saturnenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

EOF
python manage.py collectstatic --noinput


#This little bit uses cron to keep updating stats within the application
if [ ! -f mycron ];then
        crontab -l > mycron
        #echo new cron into cron file
 	echo "12 22 * * * cd $INSTALLLOCATION/ssddj/; source ../saturnenv/bin/activate; python manage.py cleanup && echo 'vacuum (analyze, verbose);' | python manage.py dbshell" >> mycron
        echo "* * * * *  curl -X GET http://$SATURNRINGHOST:$SATURNRINGAPACHEPORT/api/stateupdate/" >> mycron
        #install new cron file
        crontab mycron
fi
git config --global user.email "$INSTALLUSER@changeme.com"
git config --global user.name "$INSTALLUSER"

# Create new keys
CONFIGDIR=$SATURNWKDIR/saturnringconfig
sudo mkdir -p $CONFIGDIR
sudo chown $INSTALLUSER:$INSTALLUSER $CONFIGDIR
cd $CONFIGDIR
git init
ssh-keygen -q -f saturnkey -N ''
ssh-keygen -f saturnkey.pub -e -m pem > saturnkey.pem
git add *
git commit -a -m "Created Saturn keys"

mkdir -p $INSTALLLOCATION/redisqconf
cat <<EOF > $INSTALLLOCATION/redisqconf/rqworker.sh
#!/bin/bash
source $INSTALLLOCATION/saturnenv/bin/activate
python $INSTALLLOCATION/ssddj/manage.py rqworker \$1

EOF
chmod +x $INSTALLLOCATION/redisqconf/rqworker.sh
