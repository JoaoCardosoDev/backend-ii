from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import requests
from typer import Typer
from multiprocessing import cpu_count

from logging import setup_logging

from api import logging
import db

api_url = "http://api:8000/"
fetch_endpoint = f"{api_url}fetch"
raw_endpoint = f"{api_url}get_raw_data"


app = Typer()
setup_logging()
logger = logging.getLogger(__name__)

def collect_data():
    try:
        response = requests.post(fetch_endpoint)
        response.raise_for_status()
        return response.json()
    except Exception as exp:
        raise exp

def process_data(skip:int = 0, limit:int=1000):
    try:
        response = requests.get(raw_endpoint)
        response.raise_for_status()
        data = response.json()["data"]
        new_data = []
        for item in data:
            new_data.append({
            "firstname": item["firstname"],
            "lastname": item["lastname"],
            "email": item["email"],
            "phone": item["phone"]
        })
        db.get_collection("processed_data").insert_many(new_data)
    except:
        raise

@app.command()
def fetch(total_pages:int, num_process:int = cpu_count):
    assert num_process <= (2*cpu_count), "The max of total thread must not exceed number of cores * 2"
    with ThreadPoolExecutor(max_workers=num_process) as executor:
        for _ in range(1, total_pages):
            executor.submit(collect_data)

    logger.info("Processed!")

@app.command()
def process(total_pages:int = 10, limit:int=1000, num_process:int = cpu_count):
    assert num_process <= (2*cpu_count), "The max of total thread must not exceed number of cores * 2"
    with ProcessPoolExecutor(max_workers=num_process) as executor:
            for page in range(total_pages):
                executor.submit(process_data, limit*page, limit)

    logger.info("Processed!")
