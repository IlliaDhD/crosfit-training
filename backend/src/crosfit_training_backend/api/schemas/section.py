from typing import Annotated

from pydantic import BaseModel, Field

from crosfit_training_backend.api.schemas.exercise import Exercise


class Section(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    exercises: list[Exercise]
