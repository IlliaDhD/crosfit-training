from typing import Annotated

from pydantic import BaseModel, Field


class Exercise(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    sets: Annotated[int, Field(gt=0)]
    reps: Annotated[int, Field(gt=0)]
