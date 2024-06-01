from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import datetime, time

class BatchId(BaseModel):
    batchid: str

class AdditionRequest(BatchId):
    payload: List[List[int]] = []

class Status(str, Enum):
    COMPLETE= "complete"
    PENDING= "pending"
    FAILED= "fail"

class AdditionResponse(BatchId):
    response: List = None
    status: Status
    started_at: time
    completed_at: time
