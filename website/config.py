"""SongDate website development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = "/"

# Secret key for encrypting cookies
SECRET_KEY = b"\xcc\tKo\xbf\xd6\x06E/\x80~]\xf7<i\x899x\xa0\x8d\xa2e\x15\xca"
SESSION_COOKIE_NAME = "login"

# File Upload to var/uploads/
WEBSITE_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = WEBSITE_ROOT / "var" / "uploads"
JS_FOLDER = WEBSITE_ROOT / "website" / "js"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Uncomment and fill in if we decide to use a database 
# Database file is var/insta485.sqlite3
# DATABASE_FILENAME = INSTA485_ROOT / "var" / "insta485.sqlite3"
