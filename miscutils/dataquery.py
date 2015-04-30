import pyodbc

def getIdentityToken(environment,ServiceKey):    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.173.135.13;UID=QAUser;PWD=P@ssw0rd!',database="TestData_New",autocommit=True)
    curs = conn.cursor()    
    curs.execute('Select IdentityToken From Credentials_v where Environment = ? and ServiceKey = ?',environment, ServiceKey)
    row = curs.fetchone()
    return row.IdentityToken

def getServiceId(Environment,Addin,ServiceType,Provider,Workflow="None"):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.173.135.13;UID=QAUser;PWD=P@ssw0rd!',database="TestData_New",autocommit=True)
    curs = conn.cursor()    
    curs.execute('Select ServiceId From Service_v where Environment = ? and Addin = ? and ServiceType = ? and Provider = ? and Workflow = ?',Environment, Addin, ServiceType, Provider, Workflow)
    row = curs.fetchone()
    return row.ServiceId    
