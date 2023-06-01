import paramiko

ssh = para.SSHClient()

ssh.set_missing_host_key_policy(para.AutoAddPolicy())
ip = '10.10.10.10'
port = 22
username = 'admin'
password = 'password'

ssh.connect(ip,port=port,username,password=password)

command = "whoami"
stind,stout,stderr = ssh.exec_command()
cmd_output = stout.read()
print(cmd_output.decode())