from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

from langchain.schema import SystemMessage, HumanMessage

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# # ---- Try 1
# # Define data model for incoming sketches
# class SketchData(BaseModel):
#     vector_data: dict
#     text_prompt: str

# @app.post("/receive-sketch/")
# async def receive_sketch(data: SketchData):
#     """
#     Receives vector data from the frontend and saves it.
#     """
#     print("Received sketch data:", json.dumps(data.vector_data, indent=2))
    
#     # TODO: Process data (convert to Manim, etc.)
    
#     return {"message": "Sketch received!", "data": data.vector_data}

from agent import llm

# Define input model
class SketchInput(BaseModel):
    vector_data: dict
    text_prompt: str

@app.post("/generate-manim/")
async def generate_manim(data: SketchInput):
    """
    Takes vector data + text prompt and generates Manim code.
    """
    # Convert vector data to readable text format
    vector_description = json.dumps(data.vector_data, indent=2)

    # Define AI Prompt
    messages = [
        SystemMessage(content="You are an AI that generates Manim animation code."),
        HumanMessage(content=f"Here is a vector sketch:\n{vector_description}\n\nUser request: {data.text_prompt}\n\nGenerate a Manim script.")
    ]

    # Call AI Model
    response = llm(messages)

    return {"manim_code": response.content}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

