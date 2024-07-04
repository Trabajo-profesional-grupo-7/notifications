import json
import os

import requests
from fastapi import HTTPException


def update_fcm_token(user_id: int, fcm_token: str):
    users_url = f"{os.getenv('USERS_URL')}/fcm_token"

    requests.post(users_url, json={"user_id": user_id, "fcm_token": fcm_token})


def get_fcm_token(user_id: int):
    users_url = f"{os.getenv('USERS_URL')}/{user_id}/fcm_token"

    response = requests.get(users_url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "message": f"User service error: {response.status_code}",
            },
        )

    return str(response.json())
