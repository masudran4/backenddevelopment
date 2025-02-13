from fastapi import FastAPI
from auths import auth
from todos import todos
from fan_followers import followers
app = FastAPI()
app.include_router(auth.router,
                   prefix='/auth', tags=['Authentication'])
app.include_router(todos.router, tags=['Todos'])
app.include_router(followers.router, tags=['Fan/Followers'])
