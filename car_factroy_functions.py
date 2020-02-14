# As a users, I want to be able to call a function make_parts
# with 'metal' and 'labour' and get back 'shinny parts'.
print(__name__)
def make_parts(arg1, arg2):
    if arg1 == 'metal' and arg2 == 'labour':
        return 'shinny parts'
    else:
        return 'na bro, your wrong'


