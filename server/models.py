from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()
import re 

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self, key, value):
        if not value.strip():
            raise ValueError("Name is required.")
        # Check if the name is unique
        existing_author = Author.query.filter(Author.name == value).first()
        if existing_author and existing_author.id != self.id:
            raise ValueError("Name must be unique.")
        
        return value

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be exactly ten digits.")
        return value
        

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    


    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return value

    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) > 250:
            raise ValueError("Summary must be a maximum of 250 characters.")
        return value

    @validates('category')
    def validate_category(self, key, value):
        if value not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return value

    @validates('title')
    def validate_title(self, key, value):
        clickbait_terms = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(term in value for term in clickbait_terms):
            raise ValueError("Title must contain at least one of the specified clickbait terms.")
        return value


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
