from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from crosfit_training_backend.api.schemas.section import Section


class WorkoutIn(BaseModel):
    title: Annotated[str, Field(min_length=1)]
    sections: list[Section]


class WorkoutOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    sections: list[Section]
    created_at: datetime
