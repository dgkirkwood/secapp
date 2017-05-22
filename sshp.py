from paramiko import SSHClient, AutoAddPolicy
import time

class sshp(object):

	def __init__(self, script):
		self.script = script

	def sendCommand(self):
		ssh = SSHClient()
		ssh.set_missing_host_key_policy(AutoAddPolicy())
		ssh.connect('198.18.133.110', username='root', password='C1sco12345')
		sleeptime = 0.001
		outdata, errdata = '', ''
		ssh_transp = ssh.get_transport()
		chan = ssh_transp.open_session()
		# chan.settimeout(3 * 60 * 60)
		chan.setblocking(0)
		chan.exec_command(self.script)
		while True:  # monitoring process
		    # Reading from output streams
		    while chan.recv_ready():
		        outdata += chan.recv(1000)
		    while chan.recv_stderr_ready():
		        errdata += chan.recv_stderr(1000)
		    if chan.exit_status_ready():  # If completed
		        break
		    time.sleep(sleeptime)
		retcode = chan.recv_exit_status()
		ssh_transp.close()

		print(outdata)
		print(errdata)


if __name__ == "__main__":
	a = sshp('ls -la')
	a.sendCommand()