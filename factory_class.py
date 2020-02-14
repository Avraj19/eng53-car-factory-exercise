#set up
class Factory:

    def make_car(self, arg1, arg2):
        if arg1 == 'metal' and arg2 == 'labour':
            return 'shiny parts'
        else:
            return 'na bro, your wrong'

