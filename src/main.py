import pydantic
from bson.objectid import ObjectId
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from src.db_wrapper import DbWrapper
from src.models.GetInfo import GetInfo
from src.models.GetServicePoint import GetServicePoint
from src.models.SetInfo import SetInfo
from src.models.SetServicePoint import SetServicePoint

load_dotenv(find_dotenv())

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()
db = DbWrapper()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://depremproje.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    :return: a welcoming screen
    """
    try:
        logger.info("Root method was called.")

        return "Deprem Projesi API"

    except Exception as e:
        logger.error(e)
        return e


@app.post("/set_map_data")
async def set_map_data(info: SetInfo):
    """
    :param info: the data to be inserted
    :return: the inserted data
    """
    try:
        logger.info("Set map data method was called.")

        payload = info.dict()
        query = db.set_map_data(payload)

        return query

    except Exception as e:
        logger.error(e)
        return e


@app.post("/get_map_data")
async def get_map_data(info: GetInfo):
    """
    :return: the data in the database
    """
    try:
        logger.info("Get map data method was called.")

        payload = info.dict()
        query = db.get_map_data(payload)

        return query

    except Exception as e:
        logger.error(e)
        return e


@app.post("/set_service_point")
async def set_service_point(info: SetServicePoint):
    """
    :param info: the data to be inserted
    :return: the inserted data
    """
    try:
        logger.info("Set service point method was called.")

        payload = info.dict()
        query = db.set_service_point(payload)

        return query

    except Exception as e:
        logger.error(e)
        return e


@app.post("/get_service_point")
async def get_service_point(info: GetServicePoint):
    """
    :return: the data in the database
    """
    try:
        logger.info("Get service point method was called.")

        payload = info.dict()
        query = db.get_service_point(payload)

        return query

    except Exception as e:
        logger.error(e)
        return e
