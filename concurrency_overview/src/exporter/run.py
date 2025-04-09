import asyncio
import pandas as pd
import requests
from typer import Typer

from logging import setup_logging

from api import logging

api_url = "http://api:8000/"
process_endpoint = f"{api_url}get_processed_data"


app = Typer()
setup_logging()
logger = logging.getLogger(__name__)

async def collect_data():
    try:
        response = await requests.post(process_endpoint)
        response.raise_for_status()
        return response.json()
    except Exception as exp:
        raise exp

async def export_to_csv():
    data = await collect_data
    df = pd.DataFrame(data)
    df.to_csv("output.csv")
    logger.info("Processed!")

@app.command()
def export():
    asyncio.run(export_to_csv())

