from fastapi import FastAPI
from routers import citiesRouter, weaterRouter, favoritesRouter



app = FastAPI()

@app.get("/health")
def check_health():
    return "server is on"

app.include_router(citiesRouter.router)
app.include_router(weaterRouter.router)
app.include_router(favoritesRouter.router)


@app.get("/at-bash")
def replace_at_bash(long_string: str):
    return "not implemented"