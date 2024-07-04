from pydantic import BaseModel


class NotificationRequest(BaseModel):
    user_id: int
    title: str
    body: str


class UpdateFCMTokenRequest(BaseModel):
    fcm_token: str
