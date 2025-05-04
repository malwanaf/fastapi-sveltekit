from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from model.inference import classify_image

app = FastAPI()

# Optional CORS for dev (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # SvelteKit dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/classify")
async def classify(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")

    result = classify_image(img)
    return result

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running."}
