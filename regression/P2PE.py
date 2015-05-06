from httprequests import SignOn, TPS
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.23/REST/"
session_token = SignOn.SignOnWithUsernamePassword(base_url,"UserA","P@ssw0rd","BAA20642CE000001")
TPS.RequestKey("https://api.ciptest.goevo.local/2.1.23/",session_token,"3CF9E00001")