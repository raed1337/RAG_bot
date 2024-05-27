import os

from dotenv import load_dotenv


class EnvSettings:
    def __init__(self):
        load_dotenv(".env")  # Load environment variables from .env file

        self.alice_password_hash = os.getenv("ALICE_PASSWORD_HASH")
        self.bob_password_hash = os.getenv("BOB_PASSWORD_HASH")
        self.api_key = os.getenv("API_KEY")
        self.file_path = os.getenv("FILE_PATH")


# Create a global instance of the settings
settings = EnvSettings()
print(settings.alice_password_hash)
