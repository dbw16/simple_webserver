import os

import fastapi

app = fastapi.FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"The env is {os.environ['ENV']}"}
