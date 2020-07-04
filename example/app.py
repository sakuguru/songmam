import os
from typing import Any, Dict

from decouple import config
from fastapi import FastAPI, Body, Request

from songmam import Page, VerificationMiddleware, Webhook, MessageEvent

# os.environ['PAGE_ACCESS_TOKEN'] = "MY Access token"
# os.environ['PAGE_VERIFY_TOKEN'] = "MY Verify token"

page = Page()
app = FastAPI()

page.add_verification_middleware(app)

@app.get("/healthz")
async def show_server_is_alive(request: Request):
    body = await request.body()
    return "server is online."

# @app.post("/webhook")
# async def handle_entry(webhook: Webhook, request: Request):
#     # body = await request.body()
#     # # webhook = Webhook.parse_raw(body)
#     # print(body)
#     # print(webhook)
#     await page.handle_webhook(webhook)
#     return "ok"

@app.post("/webhook")
async def handle_entry(webhook: Dict[str, Any], request: Request):
    body = await request.body()
    webhook = Webhook.parse_raw(body)
    # print(body)
    print(webhook)
    await page.handle_webhook(webhook)
    return "ok"

@page.handle_message
async def echo(message: MessageEvent):
    page.get_user_profile(message.sender.id)
    page.send(message.sender.id, "thank you! your message is '%s'" % message.text)

if __name__ == "__main__":
    page.id

    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level='debug')