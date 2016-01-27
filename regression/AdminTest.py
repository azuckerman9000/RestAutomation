from httprequests import Admin, SignOn
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.26/REST/"

sixb_sessiontoken = SignOn.SignOnWithToken(base_url,dataquery.getIdentityToken("TEST","6B2866C8FD500001"))

Admin.ListScopes(base_url,sixb_sessiontoken)
Admin.ListRoles(base_url,sixb_sessiontoken,"2")
Admin.ListRoleClaims(base_url,sixb_sessiontoken,"EnterpriseUser")
Admin.GetMerchants(base_url,sixb_sessiontoken,ServiceKey="6B2866C8FD500001")