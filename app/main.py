import sentry_sdk
from fastapi import FastAPI

from app.utils.env import ENV

sentry_sdk.init(
    dsn=ENV.SENTRY_DSN,
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    enable_logs=True,
)

app: FastAPI = FastAPI()
