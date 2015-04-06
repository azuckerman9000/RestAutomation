import pyodbc

def getIdentityToken(environment,ServiceKey):    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.173.135.13;UID=QAUser;PWD=P@ssw0rd!',database="TestData_New",autocommit=True)
    curs = conn.cursor()    
    curs.execute('Select IdentityToken From Credentials_v where Environment = ? and ServiceKey = ?',environment, ServiceKey)
    row = curs.fetchone()
    return row.IdentityToken

        
