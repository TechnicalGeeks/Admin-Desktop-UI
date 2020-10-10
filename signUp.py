
import firebase_admin
from typing import Optional
import sys
from firebase_admin import auth
from firebase_admin.auth import UserRecord

# from initialise_firebase_admin import app


def create_user(email: str, user_id: Optional[str]) -> UserRecord:
    return auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)

def set_password(user_id: str, password: str) -> UserRecord:
    return auth.update_user(user_id, password=password)

def update_display_name(user_id: str, display_name: str) -> UserRecord:
    return auth.update_user(user_id, display_name=display_name)

if __name__ == "__main__":
    app = firebase_admin.initialize_app()
    print(app)

    
    ## argv[1]-email, argv[2]-user_id, argv[3]-display_name, argv[4]-password
    new_user: UserRecord = create_user(sys.argv[1], sys.argv[2])
    print(f"Firebase successfully created a new user with email - {new_user.email} and user id - {new_user.uid}")
    
    updated_user = update_display_name(sys.argv[2], sys.argv[3])
    print(f"Updated user display name to {updated_user.display_name}")
    
    user = set_password(sys.argv[2], sys.argv[4])
    print(f"Firebase has updated the password for user with user id - {user.uid}")

    