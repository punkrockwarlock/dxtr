"""
DXTR personal assistant.

Author: Ryan Ritchie
Date: 13/12/2018
"""

from config import *

DXTR_SUCCESS = 0
DXTR_ERROR = 1
DXTR_READ_ONLY = 2

class DXTR:
    def __init__(self):
        self._name = 'DXTR'
        self._version = '0.1'

    def parse_command_string(self, command):
        # we dont want to parse any empty strings, return error
        if (command == ''):
            return DXTR_ERROR

        # try to parse commands and args
        try:
            split_commands = command.split(' ')
        except:
            return DXTR_ERROR

        # make sure the first command is a valid command
        if not split_commands[0] in ['GET', 'PUT']:
            return DXTR_ERROR

        if (split_commands[0] == 'GET'):
            # the GET command retrieves information from the database
            pass
        elif (split_commands[0] == 'PUT'):
            # the PUT command stores information in the database
            if DB_READ_ONLY:
                return DXTR_READ_ONLY

        return DXTR_SUCCESS
