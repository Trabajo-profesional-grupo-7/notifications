import json
import os

import firebase_admin
from firebase_admin import credentials, messaging, storage


def setup() -> None:
    cert = json.loads(os.getenv("FIREBASE_CREDENTIALS_JSON"), strict=False)
    cred = credentials.Certificate(cert)
    firebase_admin.initialize_app(
        cred,
        {"storageBucket": "trabajo-profesional-51243.appspot.com"},
    )
    bucket = storage.bucket()
    bucket.make_public()


def new_user_notification(fcm_token: str, title: str, body: str):
    # data = {"type": type, "id": id}
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        # android=messaging.AndroidConfig(
        #     data=data,
        # ),
        token=fcm_token,
    )

    return messaging.send(message)
