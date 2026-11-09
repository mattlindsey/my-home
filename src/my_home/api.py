from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import Session, select

from my_home.db import Person, get_session


app = FastAPI(title="my-home")

# Allow the Vite dev server to call the API directly if not using its proxy.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Greeting(BaseModel):
    message: str


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/api/hi", response_model=Greeting)
def say_hi(session: SessionDep) -> Greeting:
    person = session.exec(select(Person)).first()
    if person is None:
        raise HTTPException(status_code=404, detail="No person found")
    return Greeting(message=f"Hi {person.name}!")
