from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(255))  # Link to the project or repository
    technologies = db.Column(db.String(100))  # Technologies used
    image_url = db.Column(db.String(255))  # URL for an image of the project
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

  
class Skill(db.Model, SerializerMixin):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    proficiency = db.Column(db.String(50))  # Level of proficiency (e.g., Beginner, Intermediate, Expert)
    description = db.Column(db.Text)  # Brief description of the skill
    image_url = db.Column(db.String(255))  # URL for an image representing the skill
    features = db.Column(db.Text)  # Key features or details about the skill
    category = db.Column(db.String(50))  # Skill category (e.g., Programming, Design, Soft Skills)



class BlogPost(db.Model, SerializerMixin):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)  # Author of the blog post
    image_url = db.Column(db.String(255))  # URL for the blog post image
    tags = db.Column(db.String(100))  # Tags to categorize the post (e.g., "Python, Flask, Web Development")
    summary = db.Column(db.String(255))  # Short summary of the blog post
    reading_time = db.Column(db.String(20))  # Estimated reading time (e.g., "5 min read")
    external_link = db.Column(db.String(255))  # Optional link to the full post if hosted externally (e.g., Hashnode)


class ContactMessage(db.Model, SerializerMixin):
    __tablename__ = 'contact_messages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


