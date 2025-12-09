# server.py
from fastapi import FastAPI
from schemas import ProductIn, DescriptionOut
from ai_server_core import generate_product_description

app = FastAPI()

@app.post("/ai/description", response_model=DescriptionOut)
async def ai_description(body: ProductIn):
    blocks = generate_product_description(body.model_dump())
    return DescriptionOut(blocks=blocks)
