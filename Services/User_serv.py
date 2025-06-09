from sqlmodel import Session
from Domain.Entities.User import User
from Persistence.User_repo import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, session: Session, user: User) -> User:
        # Example: automatically set a default hashed password if missing
        if not user.hashed_password:
            user.hashed_password = "default_hash"
        return self.repo.create_user(session, user)

    def get_user(self, session: Session, user_id: int) -> User | None:
        return self.repo.get_user_by_id(session, user_id)

    def list_users(self, session: Session) -> list[User]:
        return self.repo.list_all_users(session)

    def update_user(self, session: Session, user_id: int, data: User) -> User | None:
        # Could add additional validation/logic here
        return self.repo.update_user(session, user_id, data)

    def delete_user(self, session: Session, user_id: int) -> bool:
        return self.repo.delete_user(session, user_id)