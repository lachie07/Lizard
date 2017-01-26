#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Lizard

Lizard is an opensource FTP client made
using Python. More info can be found at
https://github.com/lachie07/Lizard

author: Lachlan Mather
last edit: 26/01/2017
version: 0.0.1
"""

import ftplib

while True:
    userinput = raw_input("> ").split(" ")
    if userinput[0] == "connect":
        try: #test if all arguments are there
            if not userinput[3] == "":
                ftp = ftplib.FTP(userinput[1])
                ftp.login(userinput[2],userinput[3])
                print "Connected"
        except IndexError:
            print "Not all arguments found"
            print "Usage: connect [server] [username] [password]"
        except Exception as e:
            print "Error occured, more info: %s" % e
    elif userinput[0] == "quit":
        try:
            ftp.quit()
        except NameError:
            print "Not connected to server"
        except AttributeError:
            print "Not connected to server"
    elif userinput[0] == "dir":
        try:
            ftp.dir()
        except NameError:
            print "Not connected to server"            
        except AttributeError:
            print "Not connected to server"
    elif userinput[0] == "help":
        print "Help:"
        print "*Note that all arguments surrounded in < and > means optional"
        print "connect [server] [username] [password] : connects to the desired FTP server"
        print "quit : disconnects from the current server"
        print "dir <directory> : lists all files and folders (in a specific directory)"
