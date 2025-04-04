import os
import secrets

secret_key = secrets.token_urlsafe(50)
env_content = f"""SECRET_KEY={secret_key}
DATABASE_URL=postgres://user:password@host:port/dbname
"""

with open('.env', 'w') as f:
    f.write(env_content)

print("File .env đã được tạo thành công!")
