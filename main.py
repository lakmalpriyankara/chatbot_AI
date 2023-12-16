from fastapi import Request
from fastapi import FastAPI
from starlette.responses import JSONResponse
from db import  get_test

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def handle_request(request: Request):

    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']


    if intent == "get.service":
        return get_ditails(parameters)



def get_ditails(parameters: dict):

    test = parameters.get("test")
    print(test[0])

    testDitals = get_test(test[0])

    if testDitals:
        fulfillment_text = f"{test} first aid is {testDitals['test_details']}."
    else:
        fulfillment_text = f"No fisr-aid for {test}"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

