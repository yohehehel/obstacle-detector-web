from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import random
import base64

app = FastAPI()

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy image data
dummy_images = [
    {
        "filename": f"image_{i}.jpg",
        "base64": "data:image/png;base64," + base64.b64encode(b"FakeImageData").decode("utf-8"),
        "prediction": random.choice(["Obstacle", "No Obstacle"])
    }
    for i in range(10)
]

@app.post("/train")
def train_model():
    time.sleep(2)  # Simulate training
    return {"message": "Model training completed (simulated)."}

@app.get("/predict")
def predict_images():
    return {"results": dummy_images}
