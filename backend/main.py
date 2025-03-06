from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from langchain.schema import SystemMessage, HumanMessage

from models import SketchInput
from agent import chain

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/generate-manim/")
async def generate_manim(sketch_data: SketchInput):
    """
    Takes vector data + text prompt and generates Manim code.
    """
    # Convert vector data to readable text format
    # vector_description = json.dumps(data.vector_json, indent=2)

    # Define AI Prompt
    #messages = [
    #    SystemMessage(content="You are an AI that generates Manim animation code."),
    #    HumanMessage(content=f"Here is a vector sketch:\n{vector_description}\n\nUser request: {data.text_prompt}\n\nGenerate a Manim script.")
    #]

    # Call AI Model
    manim_code = chain.invoke(sketch_data.model_dump())

    return {"manim_code": manim_code.manim_code}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

