I. File list
------------
irc.py		Class for irc commands
ircbot.py	An irc driven bot
httpflood.py	Launch HTTP attack
udpflood.py	Launch UDP flood
hulk.py		Unbearable HTTP attack from Packetstorm


II. Usage
------------
1. Configure ircbot to the IRC server and channel that is going to be used. Can be changed in 
   the header of ircbot.py
2. Set password that is going to be used to verify commands are coming from controller. Can be
   changed in the header of ircbot.py
3. Start ircbot.py using python 2.7.1+ 
	example: python ircbot.py
4. ircbot will connect to the IRC server and channel specified in the ircbot code. Connect to
   the same channel to start sending commands, using any IRC client.
	example: http://webchat.freenode.net/
5. After connecting to the server the ircbot will listen for commands that
   contains the correct password and are in the correct format. 


III. Supported Commands
------------
<password>hi - bot will reply with 'Hello'
	example: @!!@hi
<password>RollCall - all bot connected to the channel will reply with 'Here!' useful for knowing 
how many bots are connected.
	example: @!!@RollCall
<password>HTTP <ip> <port> <number-of-request> - send HTTP flood to target
	example: @!!@HTTP 10.108.229.24 5000 5
<password>UDP <ip> <port> <length-of-attack> - send UDP flood to target
	example: @!!@UDP 10.108.229.24 5000 30
<password>Hulk <target> - Unleash to hulk of the target
	example: @!!@Hulk http://10.108.229.24:5000/
<password>Stop - stop the attack in progress
	example: @!!@Stop
<password>Status - check the status of the attack
	example: @!!@Status

