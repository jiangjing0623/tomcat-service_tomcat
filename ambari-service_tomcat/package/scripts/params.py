# encoding: utf-8
from resource_management import *
from resource_management.libraries.script.script import Script
import sys
import os
import glob
from resource_management.libraries.functions.version import format_hdp_stack_version
from resource_management.libraries.functions.default import default

config = Script.get_config()

# params from tomcat-ambari-env

#tomcat_dirname = 'apache-tomcat-9.0.38'
tomcat_dirname = 'apache-tomcat-7.0.106'

tomcat_install_dir = config['configurations']['tomcat-ambari-env']['tomcat.install_dir']
# tomcat_install_dir=/opt


tomcat_dir = os.path.join(*[tomcat_install_dir, tomcat_dirname])
# tomcat_dir =/opt/apache-tomcat-9.0.38/

tomcat_bin_dir = tomcat_dir+'/bin'
# tomcat_bin_dir=/opt/apache-tomcat-9.0.38/bin

tomcat_port = config['configurations']['tomcat-ambari-env']['tomcat.port']
tomcat_stop_port = config['configurations']['tomcat-ambari-env']['tomcat_stop.port']
# 8008

tomcat_log_dir = config['configurations']['tomcat-ambari-env']['tomcat_log_dir']
# tomcat.log_dir =/var/log/tomcat/

tomcat_log = config['configurations']['tomcat-ambari-env']['tomcat.log']
# tomcat.log = /var/log/tomcat/tomcat.log

tomcat_pid_dir = config['configurations']['tomcat-ambari-env']['tomcat_pid_dir']
tomcat_pid_file = tomcat_pid_dir + '/tomcat.pid'
tomcat_port = config['configurations']['tomcat-ambari-env']['tomcat.port']

tomcat_conf_dir = tomcat_dir + '/conf'


# jdk环境配置，以下需要自己参考主机的java环境

jdk_bin_dir = config['configurations']['tomcat-ambari-env']['jdk_bin_dir']
# jdk_bin_dir = /usr/local/jdk/bin/

jdk_dir = config['configurations']['tomcat-ambari-env']['jdk_dir']
# jdk_dir = /usr/local/jdk/

jre_dir = config['configurations']['tomcat-ambari-env']['jre_dir']
# jre_dir = /usr/local/jdk/jre/


# 临时存tomcat源
temp_file = '/tmp/'+tomcat_dirname+'.zip'
# temp_file=/temp/apache-tomcat-9.0.38.zip
