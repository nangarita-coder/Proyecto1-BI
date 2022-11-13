from pydantic import BaseModel

class DataModel(BaseModel):
    text: str

    def columns(self):
        return ["text"]
