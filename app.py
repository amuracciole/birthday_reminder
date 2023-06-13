from fastapi import FastAPI
from pydantic import BaseModel
import json
import config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Agregar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Event(BaseModel):
    id: int
    name: str
    type: str
    date: str
    recurrency: bool

def cargar_eventos():
    with open(config.EVENTS_PATH, encoding='utf-8') as file:
        data = json.load(file)
        return data["events"]

# ---------- #
#    GETs    #
# ---------- #

@app.get("/")
def index():
    return {"message": "pagina principal"}

@app.get("/events")
def get_events():
    events = cargar_eventos()
    return events

@app.get("/event/{id_event}")
def get_event(id_event: int):
    events = cargar_eventos()
    found_event = next((event for event in events if event["id"] == id_event), None)
    if found_event:
        return found_event
    else:
        return {"mensaje": "event not found"}

# ---------- #
#   POSTs    #
# ---------- #       

@app.post("/event/")
def create_event(event: Event):
    events = cargar_eventos()
    events.append(event.dict())
    with open(config.EVENTS_PATH, 'w', encoding='utf-8') as file:
        json.dump({"events": events}, file, indent=4)
    return {"mensaje": "event created"}

# ---------- #
#  DELETEs   #
# ---------- #

@app.delete("/event/{event_id}")
def delete_event(event_id: int):
    events = cargar_eventos()
    events = [event for event in events if event["id"] != event_id]
    with open(config.EVENTS_PATH, 'w', encoding='utf-8') as file:
        json.dump({"events": events}, file, indent=4)
    return {"mensaje": "event deleted"}

# ---------- #
#    PUTs    #
# ---------- #

@app.put("/event/{event_id}")
def update_event(event_id: int, updated_event: dict):
    events = cargar_eventos()
    for event in events:
        if event["id"] == event_id:
            # Actualizar los datos del evento
            event.update(updated_event)
            break

    with open(config.EVENTS_PATH, 'w', encoding='utf-8') as file:
        json.dump({"events": events}, file, indent=4)

    return {"mensaje": "event updated"}
