from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.deps import get_current_user
from app.services.supabase import supabase

router = APIRouter()


class AuthRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/signup")
async def signup(body: AuthRequest):
    try:
        response = supabase.auth.sign_up({"email": body.email, "password": body.password})
        if response.user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Signup failed")
        return {"user": response.user, "session": response.session}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login")
async def login(body: AuthRequest):
    try:
        response = supabase.auth.sign_in_with_password({"email": body.email, "password": body.password})
        if response.user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return {"user": response.user, "session": response.session}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.post("/logout")
async def logout(user=Depends(get_current_user)):
    try:
        supabase.auth.sign_out()
        return {"message": "Logged out successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
