
from db.database import SessionLocal, engine
from users.models import Base
from users.seeders import seed_users

def main():
    # Create all tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

    # Seed the database
    db = SessionLocal()
    try:
        num_users = seed_users(db)
        print(f"Successfully seeded {num_users} test users into the database")
    except Exception as e:
        print(f"Error seeding database: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    main()