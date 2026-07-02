from sqlalchemy import create_engine  
 # Import function to create a database connection
# Step 1: Create database connection
engine = create_engine('sqlite:///students.db')  
# This creates a connection to a SQLite database file named 'students.db'
# If the file does not exist, it will be created automatically
print('Engine created successfully')   # Just confirming engine is created
# Step 2: Connect to the database
with engine.connect() as conn:  
    # This opens a connection to the database
    # 'conn' is the connection object used to interact with the DB
    print('Database connected successfully')  
    # Just confirming that connection is successful