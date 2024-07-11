from sqlalchemy  import create_engine, text
import urllib.parse
from dotenv import load_dotenv
import pyodbc

import os


db_connection_string = os.getenv('AZUREDB')

# Replace these values with your Azure SQL database credentials
server_name = os.getenv('SERVER_NAME')
database_name = os.getenv('DATABASE_NAME')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

# Specify the ODBC driver and other options
params = urllib.parse.quote_plus(
r"Driver={ODBC Driver 18 for SQL Server};"
f"Server=tcp:{server_name},1433;"
f"Database={database_name};"
f"Uid={user_name};"
f"Pwd={password};"
"Encrypt=yes;"
"TrustServerCertificate=no;"
"Connection Timeout=30;"
)

# Create the engine with the connection string
engine = create_engine(db_connection_string )



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM JOBS'))
    
    jobs = []
    for row in result.all():
        row_dict = dict(row._mapping)  # Use _mapping to convert the row to a dictionary
        jobs.append(row_dict)
    return jobs
  
  
  
  
# try:
#     connection = engine.connect()
#     print("Connection successful!")
#     connection.close()
# except Exception as e:
#     print(f"Error connecting: {e}")
    

  
    # print ('type(result):', type(result)) 
    # result_all = result.all()
    # print ('type(result.all()):', type(result_all)) 
    # first_result = result_all[0]
    # print ('type(first_result):', type(first_result)) 
    # first_result_dict = first_result._asdict()
    # print('type(first_result_dict):', type(first_result_dict))
    # print(first_result_dict)

  


# Test the connection