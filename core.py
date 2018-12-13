"""
DXTR personal assistant.

Author: Ryan Ritchie
Date: 13/12/2018
"""

DXTR_ERROR = 1
DXTR_SUCCESS = 0

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
            command.split(' ')
        except:
            return DXTR_ERROR

        return DXTR_SUCCESS
