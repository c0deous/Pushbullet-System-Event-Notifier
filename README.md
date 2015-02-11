<h1>Pushbullet Linux System Notifyer</h1>

<p>

<h3> Purpose of this program </h3>
This program is meant to be run in whatever upon shutdown, startup, or any other custom action.  This program does not run on its own upon these actions but you must configure your system so that it calls this program, with the necessary options, to run upon said events.
I have only tested this with ubuntu linux using the /etc/rc*.d files.  Windows and OSX is not officially supported, though I suspect OSX should work without any problems.
<br />

<b>To get started, edit the file "pushbulletsystemstats.py" and put in all necessary information</b>
<br />

Run this program with option --startup during startup to send a push notification to all pushbullet devices. <br />
Run this program with option --shutdown during shutdown to send a push notification to all pushbullet devices. <br />
Run this program with option --custom="ACTION" replacing ACTION with said action you will be notified of said action <br />
<br />

NOTE: This program requires the Pushbullet Python library.  It can be installed via Pip, easy_install, or you can download the package manually from
https://pypi.python.org/pypi/pushbullet.py just make sure when you run setup.py that you run it with python3.  This technically could work with python 2 as well, I just prefer to use 3.
<br />
Created by Jesse Wallace (c0deous) on 3/10/2015.<br />
Copyright (c) 2015 Finaleffect Studios
</p>
