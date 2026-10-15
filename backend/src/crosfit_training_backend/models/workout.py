from datetime import UTC, datetime
from typing import Annotated
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field

from crosfit_training_backend.api.schemas.section import Section


class Workout(Document):
    id: UUID = Field(default_factory=uuid4)
    title: Annotated[str, Field(min_length=1)]
    sections: list[Section]
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Settings:
        name = "workouts"
