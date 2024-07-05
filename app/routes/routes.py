from fastapi import APIRouter, HTTPException, status

from app.ext import firebase as fb
from app.routes.schemas import NotificationRequest, UpdateFCMTokenRequest
from app.services import services

router = APIRouter()


@router.post(
    "/notifications/notify",
    status_code=201,
    tags=["Notifications"],
    description="Sends a notification to a certain user.",
)
def send_notification(notification: NotificationRequest):
    try:
        fcm_token = services.get_fcm_token(notification.user_id)

        fb.new_user_notification(
            fcm_token=fcm_token,
            title=notification.title,
            body=notification.body,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/notifications/update_fcm_token",
    status_code=201,
    tags=["Notifications"],
    description="Updates the fcm_token for a certain user_id.",
)
async def post_fcm_token(fcm_token: UpdateFCMTokenRequest):
    try:
        return services.update_fcm_token(
            user_id=fcm_token.user_id, fcm_token=fcm_token.fcm_token
        )
    except Exception as e:
        raise HTTPException(
            detail="Error updating FCM token",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
