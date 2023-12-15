

from fastapi import FastAPI

# initialize
app = FastAPI()


# define a route
@app.get('/')
def index():
    return 'welcome to my first api'