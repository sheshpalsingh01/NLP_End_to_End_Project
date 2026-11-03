from fastapi import FastAPI, HTTPException
import uvicorn
import os
from pydantic import BaseModel
from fastapi.responses import RedirectResponse, Response
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()


class PredictRequest(BaseModel):
    text: str


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(request: PredictRequest):
    try:
        if not request.text or not request.text.strip():
            raise HTTPException(status_code=400, detail="Text is required")

        obj = PredictionPipeline()
        result = obj.predict(request.text)
        return {"summary": result}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
