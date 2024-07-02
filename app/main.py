from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.ext import firebase as fb
from app.routes.routes import router as notifications

app = FastAPI(
    title="Notifications",
)
fb.setup()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

app.include_router(notifications)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")
