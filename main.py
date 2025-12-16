import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="OMEGA AUTO‑EXPAND CORE",
    description="Lucifer Omega Autonomous Engine"
)

# ----------------------------------------
# **1) หน้า UI — เปิดได้ทันที**
# ----------------------------------------
@app.get("/")
def ui():
    try:
        return HTMLResponse(open("index.html", "r", encoding="utf-8").read())
    except:
        return HTMLResponse("<h1 style='color:red'>index.html NOT FOUND</h1>")


# ----------------------------------------
# **2) SYSTEM KEY**
# ----------------------------------------
MASTER_API_KEY = os.environ.get("OMEGA_MASTER_KEY")  # <<< ต้องตั้งใน Render


# ----------------------------------------
# **3) DATA MODEL**
# ----------------------------------------
class LogicCommand(BaseModel):
    api_key: str
    command: str
    params: dict = {}


# ----------------------------------------
# **4) KEY VALIDATION**
# ----------------------------------------
def validate_key(key):
    if key != MASTER_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid Omega-Key")
    return True


# ----------------------------------------
# **5) EXECUTION ENGINE (AUTO‑EXPAND)**
# ----------------------------------------
@app.post("/execute")
async def execute_logic(data: LogicCommand):

    validate_key(data.api_key)

    # คำสั่งของ Omega
    if data.command == "auto_expand":
        return {
            "engine": "Ω‑AUTO‑EXPAND",
            "status": "ACTIVE",
            "detail": "Omega Engine Expanded Successfully"
        }

    if data.command == "ping":
        return {"status": "pong", "engine": "omega"}

    return {"status": "unknown_command", "command": data.command}


# ----------------------------------------
# **6) HEALTH CHECK**
# ----------------------------------------
@app.get("/health")
def health():
    return {"status": "Omega Core Running"}

