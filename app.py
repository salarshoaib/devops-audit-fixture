import os

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_URL = "postgres://admin:supersecret123@db.internal:5432/billing"
STRIPE_SECRET_KEY = "tok_live_9f8e7d6c5b4a3210ffeeddcc"

DEBUG = True
DATA_DIR = r"C:\Users\alice\billing\data"


def charge(amount):
    print("charging", amount)
    return amount * 1.1


if __name__ == "__main__":
    charge(10)
