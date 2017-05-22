from flask import Flask, render_template, redirect
from sshp import sshp



app = Flask(__name__)

@app.route("/")
def main():
	return render_template('indexBoot.html')

@app.route("/connectivity")
def connectivity():
	connect = sshp('wall -n Confirm connection attempt from user: gavtan@cisco.com')
	connect.sendCommand()
	return redirect('/connected')

@app.route("/connected")
def connected():
	return render_template('connected.html')

@app.route("/hacks")
def hacks():
	return render_template('hacks.html')

@app.route("/hack1", methods=['POST'])
def hack1():
	thisHack = sshp('cd scripts/ && ./sendemail-phish-opendns.sh && ./sendemail-phish-known-malware.sh')
	thisHack.sendCommand()
	return redirect('/hackComplete')


@app.route("/hacks2")
def hacks2():
	return render_template('hacks2.html')

@app.route("/hack2", methods=['POST'])
def hack2():
	thisHack = sshp('cd scripts/ && ./sendemail-phish-0day.sh')
	thisHack.sendCommand()
	return redirect('/hacks3')

@app.route("/hacks3")
def hacks3():
	return render_template('hacks3.html')

@app.route("/hack3", methods=['POST'])
def hack3():
	thisHack = sshp('cd scripts/ && expect exploit.tcl')
	thisHack.sendCommand()
	return redirect('/hackError')

@app.route("/hackError")
def hackError():
	return render_template('hackError.html')

@app.route("/hackComplete")
def hackComplete():
	return render_template('hackComplete.html')


"""
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
"""


if __name__ == "__main__":
	app.run()





