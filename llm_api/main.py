import pipeutils

from fastapi import FastAPI, APIRouter, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from transformers import pipeline


# Model loaded here -in root- because the API fully depends on it.
print("INFO: Loading the model...")
pipe = pipeline(
      "text-generation",
      model="Qwen/Qwen2.5-1.5B-Instruct",
      device_map="auto",
    )
print("INFO: Finished loading the model...")


app = FastAPI()


class ExtractionRequestBody(BaseModel):
    content: str


# Authentication and trust are handled via the internal certificate authority (mTLS).
# No session or JWT-based authorization is needed, since this service is internal-only.

router = APIRouter(prefix="/api/v1")


@router.post("/extract-jobs")
async def extractJobs(extractReqBody: ExtractionRequestBody):
    jobs = pipeutils.extractJobsToJSON(pipe, extractReqBody.content)

    return JSONResponse(
        status_code=200, 
        content={
            "extracted_jobs": jobs,
        },
    ) 



app.include_router(router)