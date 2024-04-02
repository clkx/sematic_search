# Music Genre Classification with FastAPI

Access data with mongoDB using FastAPI as backend.
* Store AI generate music with embedded prompt and audio.
* Perform semantic search to find music by semantic meaning of the prompt and audio signal.
* 
## Installation

```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Run
```bash
uvicorn main:app --reload
```