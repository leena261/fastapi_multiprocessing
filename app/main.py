from fastapi import FastAPI
from typing import List
from app.models import AdditionRequest, AdditionResponse
import multiprocessing
from multiprocessing import Pool
from utils.utils import get_cur_time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='application.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = FastAPI()


def add_num_task(payload: List) -> dict:
    try:
        res = sum(payload)
        logger.info(f"Success: add_num_task")
        return res
    except Exception as e:
        logger.error(f"Error in add_num_task: {str(e)}")
        return None
    

@app.post("/add_process")
async def add_process(request: AdditionRequest) -> AdditionResponse :
    logger.info(f"Process Started")
    p = Pool(processes = 2)
    starttime = get_cur_time()
    task = p.map_async(add_num_task, request.payload)
    res = task.get()
    p.close()
    endtime = get_cur_time()
    add_resp = {
        "batchid":request.batchid,
        "response":res,
        "status":"complete",
        "started_at": starttime,
        "completed_at": endtime
        }
    logger.info(f"Process Done: {add_resp}")
    return add_resp
    
