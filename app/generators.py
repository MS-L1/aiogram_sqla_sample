# Asynchronous Example
import asyncio
from mistralai import Mistral
import os
from config import AI_TOKEN

async def generate_mistral(content):
    async with Mistral(
        api_key=AI_TOKEN,
    ) as mistral:

        res = await mistral.chat.complete_async(model="mistral-large-latest", messages=[
            {
                "content": content,
                "role": "user",
            },
        ], stream=False)
        if res is not None:
            return res
