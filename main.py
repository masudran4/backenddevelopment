from fastapi import FastAPI
from auths import auth
from todos import todos
from fan_followers import followers
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only!
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router,
                   prefix='/auth', tags=['Authentication'])
app.include_router(todos.router, tags=['Todos'])
app.include_router(followers.router, tags=['Fan/Followers'])
