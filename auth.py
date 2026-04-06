from fastapi import Header, HTTPException

def get_role(x_role: str = Header(...)):
    return x_role

def check_role(role, allowed):
    if role not in allowed:
        raise HTTPException(status_code=403, detail="Access denied")