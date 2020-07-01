import getpass
import telnetlib

HOST = '172.19.0.2'
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

if password:
    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii') + b'\n')

# Ciscoコマンド発行
tn.write(b'show clock' + b'\n')
tn.write(b'exit' + b'\n')

# read_until以降のテキストを出力
print(tn.read_all().decode('ascii'))