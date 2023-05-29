from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

codespace_name = os.getenv("CODESPACE_NAME")
codespace_domain = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
CSRF_TRUSTED_ORIGINS = [f'https://{codespace_name}-8000.{codespace_domain}']
