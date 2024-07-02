from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.ext import firebase as fb

router = APIRouter()


class Notification(BaseModel):
    fcm_token: str
    title: str
    body: str
    type: str
    id: str


@router.post(
    "/notifications/notify",
    status_code=201,
    tags=["Notifications"],
    description="Sends a notification to a certain user.",
)
def send_notification(notification: Notification):
    try:
        fb.new_user_notification(
            fcm_token=notification.fcm_token,
            title=notification.title,
            body=notification.body,
            type=notification.type,
            str=notification.id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
