import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("198.18.133.110", username="root", password="C1sco12345")

stdin, stdout, stderr = client.exec_command("cd scripts/ && ./sendemail-phish-opendns.sh")



text = stdout.read()

print text

