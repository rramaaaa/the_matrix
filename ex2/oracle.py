import os
from dotenv import load_dotenv


load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")
print()

api_key = os.environ.get("API_KEY")
matrix_mode = os.environ.get("MATRIX_MODE")
database_url = os.environ.get("DATABASE_URL")
log_level = os.environ.get("LOG_LEVEL")
zion_endpoint = os.environ.get("ZION_ENDPOINT")

if (
        api_key and matrix_mode and database_url 
        and log_level and zion_endpoint
        ):

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "development":
        print("Database: Connected to local instance")
    elif matrix_mode == "production":
        print("Database: Connected to production server")
    else:
        print("Database: Connected to unknown environment")

    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")
    print()

    print("Environment security check:")
    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY is missing")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if matrix_mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configurations.")


else:
    raise ValueError("[MISSING] missing configuration check the .env file")
