import json

import fitest_lang.dsl
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fitest_lang.program import Program

from .types import Request

app = FastAPI(
    title="fitest.api.io",
    version="v0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"fitest.api.io": "v0.1.0"}


@app.post("/parse")
async def parse(content: Request):
    return json.loads(Program.from_ir(fitest_lang.dsl.parse(content.message)).to_json())


@app.post("/timers")
async def parse(content: Request):
    return json.loads(json.dumps(Program.from_ir(fitest_lang.dsl.parse(content.message)).to_timer_objs().to_json()))
