from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from crosfit_training_backend.api.schemas.workout import WorkoutIn, WorkoutOut
from crosfit_training_backend.models.workout import Workout

router = APIRouter(prefix="/workouts", tags=["workouts"])


@router.post("", response_model=WorkoutOut, status_code=status.HTTP_201_CREATED)
async def create_workout(payload: WorkoutIn) -> Workout:
    workout = Workout(**payload.model_dump())
    await workout.insert()
    return workout


@router.get("/{workout_id}", response_model=WorkoutOut)
async def get_workout(workout_id: UUID) -> Workout:
    workout = await Workout.get(workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout
