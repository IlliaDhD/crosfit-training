WORKOUT = {
    "title": "Тестове тренування",
    "sections": [
        {
            "name": "Розминка",
            "exercises": [{"name": "Присідання", "sets": 3, "reps": 10}],
        },
        {
            "name": "Основне тренування",
            "exercises": [{"name": "Підтягування", "sets": 5, "reps": 5}],
        },
    ],
}


async def test_create_and_get_workout(client):
    created = await client.post("/workouts", json=WORKOUT)
    assert created.status_code == 201
    body = created.json()
    assert body["sections"] == WORKOUT["sections"]

    fetched = await client.get(f"/workouts/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == WORKOUT["title"]


async def test_invalid_workout_rejected(client):
    bad = {
        "title": "x",
        "sections": [{"name": "A", "exercises": [{"name": "B", "sets": 0, "reps": 5}]}],
    }
    response = await client.post("/workouts", json=bad)
    assert response.status_code == 422
