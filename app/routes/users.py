from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import User, users_table
from app.database import SessionLocal, engine

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all users
@router.get("/", response_model=list[User])
def get_users(db: Session = Depends(get_db)):
    query = users_table.select()
    result = db.execute(query).fetchall()
    return [User(id=row.id, name=row.name, email=row.email) for row in result]

# Add a new user
@router.post("/")
def add_user(user: User, db: Session = Depends(get_db)):
    # Check if ID exists
    query = users_table.select().where(users_table.c.id == user.id)
    exists = db.execute(query).first()
    if exists:
        raise HTTPException(status_code=400, detail="User ID already exists")
    
    insert_query = users_table.insert().values(
        id=user.id, name=user.name, email=user.email
    )
    db.execute(insert_query)
    db.commit()
    return {"message": "User added successfully", "user": user}

# Update user
@router.put("/{user_id}")
def update_user(user_id: int, updated_user: User, db: Session = Depends(get_db)):
    query = users_table.select().where(users_table.c.id == user_id)
    existing = db.execute(query).first()
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_query = users_table.update().where(users_table.c.id == user_id).values(
        id=updated_user.id, name=updated_user.name, email=updated_user.email
    )
    db.execute(update_query)
    db.commit()
    return {"message": "User updated successfully", "user": updated_user}

# Delete user
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    query = users_table.select().where(users_table.c.id == user_id)
    existing = db.execute(query).first()
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    
    delete_query = users_table.delete().where(users_table.c.id == user_id)
    db.execute(delete_query)
    db.commit()
    return {"message": "User deleted successfully"}
