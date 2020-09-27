#!/bin/bash
#导入外部文件引用
#conf文件夹位置
conf=`python -c 'import params; print params.tomcat_conf_dir'`  
#ambari指定Tomcat连接端口
tomcat_port=`python -c 'import params; print params.tomcat_port'`  
tomcat_stop_port=`python -c 'import params; print params.tomcat_stop_port'`  
#获取当前tomcat使用的端口并输出
origin_port=`grep -r "shutdown" $conf/server.xml|awk 'BEGIN {FS="\" "} {print $1}'|awk -F"\"" '{print $2}'`
echo -e 当前Tomcat的监听端口为："$origin_port"
origin_monitor_port=`grep "HTTP"  $conf/server.xml|awk 'BEGIN {FS="\" "} {print $1}'|awk -F"\"" '{print $2}'`
echo -e 当前Tomcat连接端口为："$origin_monitor_port"



# 改端口逻辑：
# 默认：如果server.xml中设置的tomcat端口已经被当前主机占用，有则切换server.xml中的端口内容为8090以及8015，否则，不做修改。
# 如果tomcat_port\tomcat_stop_port修改了，则检查是否被当前主机占用，没有则切换server.xml中的端口内容为tomcat_port\tomcat_stop_port

# tomcat中设置的端口是否与主机端口冲突
host_port=`lsof -i :$origin_port|grep -v "PID" | awk '{print $2}'`
echo $host_port
if [ "$host_port" != "" ];
then
    #server.xml中设置的tomcat端口已经被当前主机占用
    #修改server.xml 改端口为tomcat_port
    sed -i "s/$origin_port/$tomcat_port/" $conf/server.xml
    port_getted="1"
    echo "1"

else
    #未被占用，不做修改，使用默认端口,输出默认端口
    echo "$origin_port"
    port_getted="0"
    echo "0"
fi
#当前tomcat设置端口是否与tomcat_port冲突
if [ "$origin_port" != "$tomcat_port" ]&&[ "$origin_port" != "$tomcat_stop_port" ]; then
    echo '$origin_port not eq $tomcat_port'
    sed -i "s/$origin_port/$tomcat_port/" $conf/server.xml
    sed -i "s/$origin_monitor_port/$tomcat_stop_port/" $conf/server.xml
else
    echo '$origin_port  eq $tomcat_port'
fi




# echo -e '\n'
# echo "***********************************"
 
# origin_port=`grep -r "shutdown" server.xml|awk 'BEGIN {FS="\" "} {print $1}'|awk -F"\"" '{print $2}'`
# echo -e 当前Tomcat的监听端口为："\033[32m $origin_port \033[0m"
# origin_monitor_port=`grep "HTTP" server.xml|awk 'BEGIN {FS="\" "} {print $1}'|awk -F"\"" '{print $2}'`
# echo -e 当前服务器连接器端口为："\033[32m $origin_monitor_port \033[0m"
# port3=`grep -i "redirectPort" server.xml|awk "NR==1"|awk 'BEGIN {FS="=\""} {print $2}'|cut -f1 -d"\""`
# echo -e 当前重定向的端口为："\033[32m $port3 \033[0m"
# port4=`grep -i "ajp" server.xml |awk 'BEGIN {FS="\" "} {print $1}'|awk -F"\"" '{print $2}'`
# echo -e 当前服务器的集成端口端口为："\033[32m $port4 \033[0m"
# echo "***********************************"
# echo -e '\n\n'
 
# while :
# do
 
# cat <<eof
# ***********************************
#       请输入数字或字符选项
# ***********************************
# 1.修改Tomcat监听端口
# 2.修改当前服务器连接器的端口
# 3.修改当前重定向的端口
# 4.修改当前服务器的集成端口
# x.退出
# ***********************************
 
# eof
# linenumber=`grep -rn "unpackWARs" server.xml | awk -F":" '{print $1}'`
# echo -e unpackWARS...内容在文件第"\033[32m $linenumber \033[0m"行
# echo -e '\n'
# read -p "输入您的选择：" op
#     case $op in
#         1)
#          read -p "修改Tomcat监听端口为 " port_1
#          sed -i "s/$origin_port/$port_1/" /test/server.xml
#          echo -e 当前Tomcat的监听端口为："\033[32m $port_1 \033[0m"
#          echo Tomcat监听端口修改成功
#          ;;
 
#         2)
#          read -p "修改当前服务器连接器的端口为 " port_2
#          sed -i "s/$origin_monitor_port/$port_2/" /test/server.xml
#          echo -e 当前服务器连接器端口为："\033[32m $port_2 \033[0m"
#          echo 当前服务器连接器的端口修改成功
#          ;;
 
#         3)
#          read -p "修改当前重定向的端口为 " port_3
#          sed -i "s/$port3/$port_3/" /test/server.xml
#          echo -e 当前重定向的端口为："\033[32m $port_3 \033[0m"
#          echo 当前重定向的端口修改成功
#          ;;
 
#         4)
#          read -p "修改当前服务器的集成端口为 " port_4
#          sed -i "s/$port4/$port_4/" /test/server.xml
#          echo -e 当前服务器的集成端口端口为："\033[32m $port_4 \033[0m"
#          echo $port4
#          echo 当前服务器的集成端口修改成功
#          ;;
 
#         x)
#          echo 退出修改操作...
#          break
#          ;;
#     *)
#         echo -e "\033[31m 错误输入，请输入指定选项 \033[0m"
#     esac
# done
# echo -e '\n'