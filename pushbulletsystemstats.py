#!/usr/bin/env python3
# encoding: utf-8
"""
Pushbullet Linux System Notifyer

Run this program with option --startup during startup to send a push notification to all pushbullet devices.
Run this program with option --shutdown during shutdown to send a push notification to all pushbullet devices.
Run this program with option --custom="ACTION" replacing ACTION with said action you will be notified of said action

NOTE: This program requires the Pushbullet Python library.  It can be installed via Pip, easy_install, or you can download the package manually from
https://pypi.python.org/pypi/pushbullet.py just make sure when you run setup.py that you run it with python3.  This technically could work with python 2 as well, I just prefer to use 3.

Created by Jesse Wallace (c0deous) on 3/10/2015.
Copyright (c) 2015 Finaleffect Studios
"""

import sys, os, time
from pushbullet import Pushbullet
from optparse import OptionParser

def main():
    # Settings #
    computer_name = "Your Computer" # Alias name of your computer
    computer_os = "Your OS" # OS of machine
    api_key = "API KEY" # Pushbullet API Key.  Acquire at https://www.pushbullet.com/account
    logging = False # Set to true if you wish to enable event logging. Must set a log folder if set to true.
    logfolder = "LOG FOLDER PATH" # Folder to save event logs.  MUST END IN TRAILING SLASH, DONT USE ~ TYPE OUT LITERAL PATH A new event log will be created for each days actions.  If no events occur then no file will be created for that day.
    
    # Pushbullet Init #
    pb = Pushbullet(api_key)
    
    # Options #
    parser = OptionParser()
    parser.add_option('--startup', dest='startup', action='store_true', help='Notifies upon startup')
    parser.add_option('--shutdown', dest='shutdown', action='store_true', help='Notifies upon shutdown')
    parser.add_option('--custom', dest='custom', help="Notifies with custom action")
    parser.add_option('--log-override-on', dest='log_override_on', action='store_true', help='Overrides log setting to "True"')
    parser.add_option('--log-override-off', dest='log_override_off', action='store_true', help='Overrides log setting to "False"')
    (options, args) = parser.parse_args()
    
    # Log overrides #
    if options.log_override_on or options.log_override_off:
        if options.log_override_on == True:
            logging = True
        elif options.log_override_off == True:
            logging = False
       
    
    def push_pb(machine, os, action, time):
        pushtitle = "(" + machine +") System Notification"
        pushmessage = '(' + machine +') running (' + os +') executed action [' + action +'] at [' + time + ']'
        push = pb.push_note(pushtitle, pushmessage)
        writetolog(pushmessage)
        
    def current_time():
        return(time.strftime("%I:%M:%S") + ' ' + time.strftime(("%d/%m/%y")))
    
    def writetolog(logtext):
        if logging == True:
            logfile = logfolder + 'eventlog-' + time.strftime("%d.%m.%y") + '.log'
            loglocation = open(logfile, 'a+')
            logtext = str(logtext)
            loglocation.write(logtext + '\n')
    
    if options.startup == True:
        push_pb(computer_name, computer_os, 'startup', current_time())
    elif options.shutdown == True:
        push_pb(computer_name, computer_os, 'shutdown', current_time())
    elif options.custom:
        push_pb(computer_name, computer_os, options.custom, current_time())
if __name__ == '__main__':
    main()
