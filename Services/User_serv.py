from sqlmodel import Session
from Domain.Entities.User import User
from Persistence.User_repo import UserRepository
from Domain.Models.User_view import UserView

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def to_view(self, user_db: User) -> UserView:
        if user_db.id is None:
            raise ValueError("User id cannot be None")
        return UserView(
            user_id=user_db.id,
            full_name=user_db.full_name,
            email=user_db.email
        )

    def get_user_view(self, session: Session, user_id: int) -> UserView | None:
        user_db = self.repo.get_user_by_id(session, user_id)
        if not user_db:
            return None
        return self.to_view(user_db)

    def create_user(self, session: Session, user: User) -> User:
        return self.repo.create_user(session, user)

    def list_users(self, session: Session) -> list[User]:
        return self.repo.list_all_users(session)

    def update_user(self, session: Session, user_id: int, data: User) -> User | None:
        # Could add additional validation/logic here
        return self.repo.update_user(session, user_id, data)

    def delete_user(self, session: Session, user_id: int) -> bool:
        return self.repo.delete_user(session, user_id)