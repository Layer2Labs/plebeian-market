import json
import os

SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = bool(int(os.environ.get("DEBUG", 0)))
PROPAGATE_EXCEPTIONS = False

LIGHTNING_INVOICE_AMOUNT = 21
MINIMUM_CONTRIBUTION_AMOUNT = 21

BID_LAST_MINUTE_EXTEND = 5

if DEBUG:
    SECRET_KEY = "DEBUG_SECRET_KEY_IS_NOT_REALLY_SECRET"
else:
    with open("/secrets/secret_key") as f:
        SECRET_KEY = f.read()

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
if DB_USERNAME is None or DB_PASSWORD is None:
    # NB: we check for None, not for ""
    # for the tests we set these to "", so no secrets file is needed, but that will result in an invalid SQLALCHEMY_DATABASE_URI
    # which is fine, since the tests should not access the database directly!
    with open("/secrets/db.json") as f:
        db = json.load(f)
        if DB_USERNAME is None:
            DB_USERNAME = db['USERNAME']
        if DB_PASSWORD is None:
            DB_PASSWORD = db['PASSWORD']

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@db:5432/market"

if bool(int(os.environ.get("SQLALCHEMY_DISABLE_POOLING", 0))):
    from sqlalchemy.pool import NullPool
    SQLALCHEMY_ENGINE_OPTIONS = {'poolclass': NullPool}

BASE_URL = os.environ.get('BASE_URL')

MOCK_LND = bool(int(os.environ.get("MOCK_LND", 0)))
LND_GRPC = os.environ.get('LND_GRPC')
LND_MACAROON = "/secrets/admin.macaroon"
LND_TLS_CERT = "/secrets/tls.cert"

MOCK_TWITTER = bool(int(os.environ.get("MOCK_TWITTER", 0)))
TWITTER_SECRETS = "/secrets/twitter.json"
