import netmiko

#デバイス情報の記載
device = {
    'device_type':'cisco_ios',
    'ip':'172.19.0.2',
    'username':'admin',
    'password':'nM6yPmhL',
    'secret':'mainte',
}

#コマンドの実行
with netmiko.ConnectHandler(**device) as con:
    con.enable()
    output = con.send_command("show run")
    print(output)
    con.disconnect()