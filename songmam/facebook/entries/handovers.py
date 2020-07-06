from pydantic import BaseModel

from songmam.facebook.entries.base import MessagingWithTimestamp


class PassThreadControl(BaseModel):
    new_owner_app_id: str
    metadata: str


class HandoversEntry(MessagingWithTimestamp):
    pass_thread_control: PassThreadControl


# {
#   "sender":{
#     "id":"<PSID>"
#   },
#   "recipient":{
#     "id":"<PAGE_ID>"
#   },
#   "timestamp":1458692752478,
#   "pass_thread_control":{
#     "new_owner_app_id":"123456789",
#     "metadata":"Additional content that the caller wants to set"
#   }
# }