import openai
from fastapi import FastAPI, HTTPException, Request, Form

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from classes.settings import Settings
from classes.request import RecommendationRequest


settings = Settings()
openai.api_key = settings.OPENAI_API_KEY


app = FastAPI()
messages = [{"role": "system", "content":
             "You are a travel recommendation assistant.  \
                You will reply strictly three(3) things to do on specific country, and season that the user will provide.\
                      Your response should be strictly follow this: do not create new line, do not add numbers to order the list, and it should be separated by comma."}]

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/recommendation")
def travel_reco(body: RecommendationRequest):
    season_list = ["spring", "winter", "summer", "fall"]
    if (body.season.lower() not in season_list):
        raise HTTPException(status_code=400, detail="Invalid Season Selected")
    message = f"Country: {body.country} Season: {body.season}"
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    print('reply', reply)
    return {
        'country': body.country,
        'season': body.season,
        'recommendations': [x.strip() for x in reply.split(',')]
    }
