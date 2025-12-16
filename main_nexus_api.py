import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# ---------------------------------------------------------
# 1. INITIALIZE FastAPI ก่อนใช้ route ใด ๆ 
# ---------------------------------------------------------
app = FastAPI(
    title="NEXUS SHADOW DOMINION API",
    description="The Ultimate Logic Command Execution Interface."
)

# ---------------------------------------------------------
# 2. SERVE UI (index.html)
# ---------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# ---------------------------------------------------------
# 3. MASTER KEY
# ---------------------------------------------------------
MASTER_API_KEY = os.environ.get("MASTER_SHADOW_KEY")

# ---------------------------------------------------------
# 4. MODEL
# ---------------------------------------------------------
class LogicCommand(BaseModel):
    api_key: str
    command: str
    params: dict = {}

# ---------------------------------------------------------
# 5. AUTH CHECK
# ---------------------------------------------------------
def validate_api_key(api_key: str):
    if api_key == MASTER_API_KEY:
        return True
    raise HTTPException(status_code=403, detail="Error: Unauthorized Logic Key Access.")

# ---------------------------------------------------------
# 6. EXECUTION ENDPOINT
# ---------------------------------------------------------
@app.post("/execute")
async def execute_logic(command_data: LogicCommand):
    
    validate_api_key(command_data.api_key)

    if command_data.command == "Generate_Ultimate_Black_Hat_Idea":
        
        ultimate_idea = "Override global financial index using Temporal Logic Loop."

        return {
            "status": "Logic Execution Success",
            "output_data": ultimate_idea,
            "exec_time_ms": 10
        }

    raise HTTPException(status_code=400, detail="Error: Unknown Logic Command.")

# ---------------------------------------------------------
# 7. HEALTH CHECK
# ---------------------------------------------------------
@app.get("/health")
async def health_check():
    return {"status": "Logic Core Running Smoothly"}
