from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session
from app.db.database import get_session
from app.controllers.users_controllers import fetch_users, fetch_user_by_id, fetch_delete_user, fetch_update_user, fetch_create_user
from app.schemas.users import ModifyUserDataSchema, UserBasicSchema
from app.models.users import UserModifyModel, User
from typing import Optional
from app.auth.authorization import authenticate


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", description="Get all users", status_code=status.HTTP_200_OK)
async def read_users(is_active: Optional[bool]= Query(None), session : Session = Depends(get_session)) -> dict:
    all_users = fetch_users(db=session, is_active=is_active)
    return {
        "success": True,
        "data": all_users
        }
    
    
@router.get("/{user_id}", description="Ask for an user by its ID", status_code=status.HTTP_200_OK)
async def read_user_by_id(user_id: str, session: Session = Depends(get_session)):    
    user = fetch_user_by_id(db=session, user_id= user_id)
    return {
        "success": True,
        "data": user
    }


@router.post("", description="Create a new user", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: UserBasicSchema, session: Session = Depends(get_session), username: str = Depends(authenticate)):
    new_user = new_user.model_dump(exclude_unset=True) 
    new_user = User(**new_user)   
    created_user = fetch_create_user(db=session, new_user=new_user)
    return {
        "success": True,
        "username": username,
        "data":created_user
    }
    
    
@router.delete("/{user_id}", description="Delete an user by its ID", status_code=status.HTTP_200_OK)
async def delete_user(user_id: str, session:  Session = Depends(get_session), username: str = Depends(authenticate)):
    deleted_user = fetch_delete_user(db=session, user_id=user_id)
    return {
        "success": True,
        "username": username,
        "data": deleted_user
    }
    
    
@router.put("/{user_id}", description="Update user data by its ID", status_code=status.HTTP_200_OK)
async def modify_user(user_id: int, modify_user_data: ModifyUserDataSchema, session: Session = Depends(get_session), username: str = Depends(authenticate)): 
    modify_user_data = modify_user_data.model_dump(exclude_unset=True)
    modify_user_data = UserModifyModel(**modify_user_data)    
    modified_user = fetch_update_user(db=session, user_id=user_id, modify_user_data=modify_user_data )    
    return {
        "success": True,
        "username": username,
        "data": modified_user
    }
    
    