from pydantic import BaseModel

class UserView(BaseModel):
    user_id: int
    full_name: str
    email: str
    # Example transformation: hide hashed_password or rename fields