import os
from dotenv import load_dotenv


load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")
print()

api_key = os.environ.get("API_KEY")
matrix_mode = os.environ.get("MATRIX_MODE")
database_url = os.environ.get("DATABASE_URL")
log_level = os.environ.get("LOG_LEVEL")
zion_endpoion = os.environ.get("ZION_ENDPOION")

if (
        api_key and  matrix_mode and database_url 
        and log_level and zion_endpoin
        ):

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    if matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production server")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoion}")
    print()

    print("Environment security check:")


else:
    raise ValueError("[MISSING] missing configuration check the .env file")
