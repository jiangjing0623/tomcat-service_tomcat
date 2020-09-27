# encoding: utf-8
import sys
import os
import pwd
import grp
import signal
import time
import glob
from resource_management import *
from subprocess import call


class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        #tomcat_package = 'https://downloads.apache.org/tomcat/tomcat-9/v9.0.38/bin/apache-tomcat-9.0.38.tar.gz'
        tomcat_package = 'https: // downloads.apache.org/tomcat/tomcat-7/v7.0.106/bin/apache-tomcat-7.0.106.tar.gz'
        service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
        Execute('mkdir -p ' + params.tomcat_log_dir)
        Execute('touch ' + params.tomcat_log)
        Execute('mkdir -p ' + params.tomcat_dirname)
        Execute('mkdir -p ' + params.tomcat_install_dir)
        Execute('mkdir -p ' + params.tomcat_dir)
        Execute('mkdir -p ' + params.tomcat_bin_dir)
        Execute('echo Installing tomcat pachages')
        if not os.path.exists(params.temp_file):
            Execute('wget ' + tomcat_package + ' -O ' +
                    params.temp_file + ' -a ' + params.tomcat_log)
        Execute('tar xvf ' + params.temp_file+' -C ' +
                params.tomcat_install_dir + " >> " + params.tomcat_log)

        # Execute('echo "export TOMCAT_HOME = {0}" '.format(
        #    params.tomcat_dir) + ' >> etc/profile')
        #Execute('echo "export JRE_HOME=${JAVA_HOME}/jre " >> etc/profile' )
        #Execute('source /etc/profile')
        self.configure(env, True)

    def port_change(self, env):
        import params
        import change_port
        env.set_params(params)
        #如果需要修改端口，则修改为params.tomcat_port        
        Execute(
            "sed -i 's/8080/{0}/g ' {1}/server.xml".format(
                params.tomcat_port, params.tomcat_conf_dir))
        Execute(
            "sed -i 's/8005/{0}/g ' {1}/server.xml".format(
                params.tomcat_stop_port, params.tomcat_conf_dir))

    def configure(self, env, isInstall=False):
        import params
        env.set_params(params)

    def stop(self, env):
        import params
        env.set_params(params)
        Execute(params.tomcat_bin_dir+'/shutdown.sh >>' + params.tomcat_log)
        Execute('rm ' + params.tomcat_pid_file + ' >> ' + params.tomcat_log)

    def start(self, env):
        import params
        self.configure(env)
        self.port_change(env)
        Execute(params.tomcat_bin_dir+'/startup.sh >> ' + params.tomcat_log)
        Execute('mkdir -p '+params.tomcat_pid_dir + ' >> ' + params.tomcat_log)
        Execute('touch ' + params.tomcat_pid_file + ' >> ' + params.tomcat_log)
        Execute("ps -ef | grep -i tomcat | awk {' print $2'} | head -n 1 > " +
                params.tomcat_pid_file)

    def status(self, env):
        import params
        env.set_params(params)
        check_process_status(params.tomcat_pid_file)


if __name__ == "__main__":
    Master().execute()
