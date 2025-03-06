from pydantic import BaseModel

class SketchInput(BaseModel):
    vector_json: dict
    user_prompt: str

class ManimCodeOutput(BaseModel):
    manim_code: str