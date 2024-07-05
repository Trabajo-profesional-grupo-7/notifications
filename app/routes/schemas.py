from pydantic import BaseModel


class NotificationRequest(BaseModel):
    user_id: int
    title: str
    body: str


class UpdateFCMTokenRequest(BaseModel):
    user_id: int
    fcm_token: str
