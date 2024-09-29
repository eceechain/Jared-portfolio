
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import ContactMessage, db, Project, Skill, BlogPost
import re

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Home Route
@app.route('/')
def home():
    return 'Hello, I am Jared Amima, a software engineer passionate about innovative solutions. Explore my work and see how I turn ideas into code.'

# About Route
@app.route('/about')
def about():
    return """
    About Me:
    I'm Jared Amima, a passionate graphic designer and web developer with a keen eye for detail and a love for creative problem-solving. 
    I specialize in crafting visually compelling designs and building user-friendly web applications. 
    With a background in software engineering and a strong proficiency in tools like Adobe Illustrator and Python, I bring ideas to life through design and code.
    
    My mission is to create seamless and impactful digital experiences that resonate with users and drive innovation. 
    When I'm not coding or designing, I'm continually learning new skills and exploring the latest trends in tech and design. 
    Let's connect and create something amazing together!
    """

# Projects Route (All Projects)
@app.route('/projects', methods=['GET'])
def projects():
    projects = Project.query.all()
    projects_data = [
        {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "link": project.link,
            "technologies": project.technologies,
            "image_url": project.image_url,
        } 
        for project in projects
    ]
    return jsonify(projects_data)

# Project Route by ID
@app.route('/projects/<int:id>', methods=['GET'])
def project_by_id(id):
    project = Project.query.get_or_404(id)
    project_data = {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "link": project.link,
        "technologies": project.technologies,
        "image_url": project.image_url,
    }
    return jsonify(project_data)

# Skills Route - Retrieve All Skills
@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    skills_data = [
        {
            "id": skill.id,
            "name": skill.name,
            "proficiency": skill.proficiency,
            "description": skill.description,
            "image_url": skill.image_url,
            "features": skill.features,
            "category": skill.category
        } 
        for skill in skills
    ]
    return jsonify(skills_data)

# Skills Route - Retrieve a Skill by ID
@app.route('/skills/<int:id>', methods=['GET'])
def get_skill_by_id(id):
    skill = Skill.query.get_or_404(id)
    skill_data = {
        "id": skill.id,
        "name": skill.name,
        "proficiency": skill.proficiency,
        "description": skill.description,
        "image_url": skill.image_url,
        "features": skill.features,
        "category": skill.category
    }
    return jsonify(skill_data)

# Resume Route
@app.route('/resume')
def resume():
    return "Download my resume here: [link to resume]."

# Blog Posts Route - Retrieve All Blog Posts
@app.route('/blog_posts', methods=['GET'])
def get_blog_posts():
    blog_posts = BlogPost.query.all()
    blog_posts_data = [
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": post.author,
            "image_url": post.image_url,
            "tags": post.tags,
            "summary": post.summary,
            "reading_time": post.reading_time,
            "external_link": post.external_link
        } 
        for post in blog_posts
    ]
    return jsonify(blog_posts_data)

# Blog Post Route - Retrieve a Blog Post by ID
@app.route('/blog_posts/<int:id>', methods=['GET'])
def get_blog_post_by_id(id):
    post = BlogPost.query.get_or_404(id)
    blog_post_data = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "image_url": post.image_url,
        "tags": post.tags,
        "summary": post.summary,
        "reading_time": post.reading_time,
        "external_link": post.external_link
    }
    return jsonify(blog_post_data)

# Contact Route (GET)
@app.route('/contact', methods=['GET'])
def contact_info():
    return """
    Contact Me:
    I'd love to hear from you! Whether you have a question, a potential collaboration, or just want to say hello, feel free to reach out.
    
    Email: jaredamima@example.com
    LinkedIn: https://www.linkedin.com/in/jaredamima
    GitHub: https://github.com/jaredamima
    Portfolio: https://jaredamima-portfolio.com
    
    I aim to respond to all inquiries within 24-48 hours. Let's connect and create something amazing together!
    """

# Function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Contact Route to Send ContactMessage
@app.route('/contact/send', methods=['POST'])
def send_contact_message():
    data = request.get_json()
    print("Received JSON data:", data)
    
    # Extract data from the request
    name = data.get('name', None)
    email = data.get('email', None)
    subject = data.get('subject', None)
    message = data.get('message', None)

    # Validate the input data
    if name and email and subject and message:
        # Check if email is valid
        if not is_valid_email(email):
            return jsonify(message='Invalid email format.'), 400
        
        new_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(new_message)
        db.session.commit()
        
        return jsonify(message='Your message has been sent successfully! We will get back to you shortly.'), 201
    else:
        return jsonify(message='Message not sent! Some fields are missing or invalid.'), 400


# Route to retrieve all contact messages (for admin use)
@app.route('/contact/messages', methods=['GET'])
def get_contact_messages():
    messages = ContactMessage.query.all()
    messages_data = [
        {
            "id": message.id,
            "name": message.name,
            "email": message.email,
            "subject": message.subject,
            "message": message.message
        } 
        for message in messages
    ]
    return jsonify(messages_data)

if __name__ == '__main__':
    app.run(debug=True)
