import pysipp

pysipp.utils.log_to_stderr("DEBUG")

uac = pysipp.client(destaddr=('mysipdomain.net', 5060))
uac.uri_username = '12345'
uac.auth_password = ''
uac.scen_file = './numeric.xml'
uac()