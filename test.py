import sdplus
from pprint import pprint
from config import api_token, sdplus_fqdn

request = sdplus.Request(api_token, sdplus_fqdn)
pprint(request.get(53187))
