from sqlalchemy import create_engine, text
import urllib.parse
from dotenv import load_dotenv
import pyodbc
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
server_name = os.getenv('SERVER_NAME')
database_name = os.getenv('DATABASE_NAME')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

# Check if environment variables are loaded correctly
if not all([server_name, database_name, user_name, password]):
    raise ValueError("One or more environment variables are missing.")

# Specify the ODBC driver and other options
params = urllib.parse.quote_plus(
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server=tcp:{server_name},1433;"
    f"Database={database_name};"
    f"Uid={user_name};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# Create the engine with the connection string
db_connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM JOBS'))
        jobs = [dict(row._mapping) for row in result.all()]  # Use _mapping to convert rows to dictionaries
    return jobs

# Test the connection
try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Error connecting: {e}")