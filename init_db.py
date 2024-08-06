from app import app, db

# Ensure the Flask app is created and use the application context
with app.app_context():
    db.create_all()

