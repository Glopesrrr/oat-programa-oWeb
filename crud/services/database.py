import pyodbc

server = 'PEDRXXT' 
database = 'crud_cliente' 
username = 'sa'  
password = 'pedrofilho123'  
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()