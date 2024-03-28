# import pymongo
# import requests
# from motor.motor_asyncio import AsyncIOMotorClient
# from dotenv import load_dotenv
# import os


# load_dotenv()
# # client = pymongo.MongoClient(os.getenv("MONGO_URL"))
# # db = client.sample_mflix
# # collection = db.movies
# MONGO_URL = os.getenv("MONGO_URL")
# client = AsyncIOMotorClient(MONGO_URL)
# database = client["mydatabase"]
# collection = database["embedded_music"]

# # print(collection.find().limit(5))

# # items = collection.find().limit(5)

# # for item in items:
# #     print(item)


# huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
# embedding_url = os.getenv("EMBEDDING_URL")

# def generate_embedding(text: str) -> list[float]:

#   response = requests.post(
#     embedding_url,
#     headers={"Authorization": f"Bearer {huggingface_token}"},
#     json={"inputs": text})

#   if response.status_code != 200:
#     raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

#   return response.json()

# print(generate_embedding("90s rock song with electric guitar and heavy drums"))
import httpx
import os

async def generate_embedding(text: str) -> list[float]:
    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
    embedding_url = os.getenv("EMBEDDING_URL")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            embedding_url,
            headers={"Authorization": f"Bearer {huggingface_token}"},
            json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()