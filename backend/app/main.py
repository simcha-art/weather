from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware
from routers import citiesRouter, weaterRouter, favoritesRouter
from services.helper import at_bash_dict
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s | %(levelname)s | %(message)s "
)

logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://myapp.vercel.app"
    ],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)

@app.middleware("http")
async def measure_time(req: Request, call_next):
    start = time.perf_counter()
    response = await call_next(req)
    end = time.perf_counter()
    duration = end - start
    logger.info(f"{req.method}/{req.url.path} - {duration:.4f} seconds")
    logger.info(f"query: {req.query_params}")
    return response



@app.get("/health")
def check_health():
    return "server is on"

app.include_router(citiesRouter.router)
app.include_router(weaterRouter.router)
app.include_router(favoritesRouter.router)


@app.get("/at-bash")
def replace_at_bash(long_string: str):
    result = []
    for char in long_string:
        result.append(at_bash_dict.get(char, char))
    return "".join(result)