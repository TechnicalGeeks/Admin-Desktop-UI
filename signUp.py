
import firebase_admin
from typing import Optional
import sys
from firebase_admin import auth
from firebase_admin.auth import UserRecord

# from initialise_firebase_admin import app

config={
  "type": "service_account",
  "project_id": "proxy-detection-1df22",
  "private_key_id": "a531450741a68a3e4a393c26d163d754ef7fe894",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCztaGOaDfxNl4o\n9g5RQ/zdXq28QAYL2wsGr7JTCzP/xTQNoieRGwq/FF7CyXsBnQxzfb2m0coipSS9\nU2jPZBs0murWiLhtjtSNXDKfPSsqvz4Qc3HAZ6zZj1ybzxaDL/nC7WttOhoax1HO\n0CMazoO/DZC7flYwXVvJ82KKRi7Q3LVAsoJnyF8t1jVjO39xc3y5JUhyX4LUPeHq\nCRGTQcXsnvr7FALDRnuKajKlPRvH34OEGq2HC5Iw0QmZk9sEs/tuJxSzIMqKfD96\n05Qh4kXORp9alDjkZ3deZF8lodqyj2xS6nooP2zbcKtsuIexTfbFYE0aOjlT5nNC\nEI7wB7GvAgMBAAECggEABADj3HxN4r3HUzpID19oXrYhQLRcbh8vG7MGUftJ6UTH\naBZYs07a6m7VvZkneF27TUdb1j+ONT9glicpipU8Veutl6HsGeS4r32CUzHVqFoi\nU9N+kT6+Bwq+kWoHolyLP+ByKDjHJBmUpPrWDV7UaIkw1Dx4RxONW+5kH5h4qoZ2\nm3uXQx8niS63WR07OUWHaxv5jG2a/wo/yYcqddPTPuU4bZl712zCOnDmWCymtphc\nl5EdIJfQ6SF5UR6mWVRXtWfQoTBpT9SsL79wX5KZ9cBrzrijg5fwwYx6fkAZaokZ\nf0+85gnHNFRUITUMmElmTX/4xb0Hqh4HphnhUKir4QKBgQDp9jk/YS7DdJa1OKpR\nrSkN0jVTue3KTz9dhXCp5vjSQsTLvb8Vc0yHRYo1sl4URFn80WSCYvqH+JP1w67H\n5uePc4BKT0sOZJBaNsJswn4ThkMNxDz/BIfqxfdf5e2KQSD/+JExm1ST/cTsg/Dn\nvxuhy7JwqkE5exCJfLECqDSrewKBgQDEoymGlUF4mJcUL2AGDRnq7sJAZdS3AOsV\nnZcBGUxFPymO1TGbF8L1HFkv9dpQlp7rAarTK53AaOqWiXOLwXJ25P4a3xftM5nV\nD4eqAC9TLwxpwnLjkLbO9uTsiOTEaJLjg4NUKY4MZdGKCYmWmBJQ9cYCtn63Dde1\nJTFcJGhSXQKBgQCfWboCJhHwxE8FnVO8D6G/rSXvIdsJCVLSQtnKjut4YkuhrVoh\npQdBtyZ8jkEvsqJL5N59RCb5R2CXarF3rBiZhwShGEK5ydrb5yIja5DtgWvYS4lz\n9EUSrcVgRr20hcmRLl7OF8rShWyD3xXM8khCufeObxe/q8dGrWvusFw3UwKBgHtw\nhd/zkH8ZIzZLqzcBQHTn30+33TnovKr8G9BXxjZuOTNuCE75MqzWV/KwnpUaiLa0\nfD1GUyh3dFR+AugHz0ht5kqOJCIG05oZvqtspEjO7zbxF1hd/zSbbwhBw4K8twFW\nDLpnv8FupYTHCfVcj5r9PolzcMaPTQttRrg2LrsNAoGAeERywA7sm2yhgQpZbCVZ\nJ11bvz+3jdnFAMqu8Y27McVNWj+RskaSJXBQi8YbWRGroYVZJIhWSJ1rAbryFVAW\nhRNqSr0rw1Q7F0KZdBpAxHEjMjklW2FhqQc7v1HHaCvzoSa6uLn62hKFZiJcDJKE\nA4NI3HciE9ebyBb7RAO/VrM=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-y1uq2@proxy-detection-1df22.iam.gserviceaccount.com",
  "client_id": "118416496771639552318",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y1uq2%40proxy-detection-1df22.iam.gserviceaccount.com"
}
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

    