from sqlmodel import Session, select
from Domain.Entities.User import User

class UserRepository:
    def create_user(self, session: Session, user: User) -> User:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_user_by_id(self, session: Session, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        return session.exec(statement).first()

    def list_all_users(self, session: Session) -> list[User]:
        statement = select(User)
        return list(session.exec(statement).all())

    def update_user(self, session: Session, user_id: int, data: User) -> User | None:
        existing_user = self.get_user_by_id(session, user_id)
        if not existing_user:
            return None
        existing_user.email = data.email
        existing_user.full_name = data.full_name
        existing_user.hashed_password = data.hashed_password
        session.add(existing_user)
        session.commit()
        session.refresh(existing_user)
        return existing_user

    def delete_user(self, session: Session, user_id: int) -> bool:
        user = self.get_user_by_id(session, user_id)
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True