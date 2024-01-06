import pypyodbc as odbc

DRIVER_NAME = 'SQL Server' 
SERVER_NAME = 'DESKTOP-UU6IQ1P\\SQLEXPRESS' 
DATABASE_NAME = 'prompt_data_base'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;  
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()


