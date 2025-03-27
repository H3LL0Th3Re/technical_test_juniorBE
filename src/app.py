from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.database import db  
import os
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)    

   
    database_url = os.getenv("DATABASE_URL")
    # database_url = f"postgresql://{user}:{password}@{hostname}:{port}/{db_name}" //if failed to get env
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    
    from models.book import Book
    from models.member import Member
    from models.borrowing import Borrowing

    from routes.book_routes import book_bp
    from routes.member_routes import member_bp
    from routes.borrowing_routes import borrowing_bp

    app.register_blueprint(book_bp, url_prefix="/api/books")
    app.register_blueprint(member_bp, url_prefix="/api/members")
    app.register_blueprint(borrowing_bp, url_prefix="/api/borrowings")

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the Library API"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
