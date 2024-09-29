from datetime import datetime
from app import app, db, ContactMessage, Project, Skill, BlogPost

with app.app_context():
    # Drop all existing tables
    db.drop_all()
    
    # Create all tables
    db.create_all()

    # Seed ContactMessage data
    contact_messages = [
        ContactMessage(name='John Doe', email='john.doe@example.com', subject='Inquiry', message='Hello, I would like more information.'),
        ContactMessage(name='Jane Smith', email='jane.smith@example.com', subject='Feedback', message='Great service!'),
    ]

    for msg in contact_messages:
        db.session.add(msg)
        db.session.commit()  # Commit after each contact message

    # Seed Project data
    projects = [
        Project(
            title='Digishop',
            description='DigiShop is an inventory management system designed to streamline the process of managing items, sales, and user authentication for a digital shop.',
            link='http://example.com/digishop',
            technologies='Python, Flask, React.js, Vite',
            image_url='http://example.com/image1.jpg'
        ),
        Project(
            title='FitHub',
            description='FitHub is an all-in-one fitness tracking application designed to help users maintain a consistent fitness routine and achieve their fitness goals effectively.',
            link='http://example.com/fithub',
            technologies='JavaScript, React, Python, Flask',
            image_url='http://example.com/image2.jpg'
        ),
        Project(
            title='Movie-Review',
            description='This project is a web application for movie reviews, built with Flask and React. The backend provides RESTful APIs for managing movie data, while the frontend allows users to view and submit reviews.',
            link='http://example.com/movie-review',
            technologies='JavaScript, React, Python, Flask',
            image_url='http://example.com/image3.jpg'
        ),
        Project(
            title='Fast Cash',
            description='Fast Cash is a web application designed to streamline the loan application process, providing users with quick and hassle-free access to financial assistance.',
            link='http://example.com/fast-cash',
            technologies='JavaScript, React, Python, Flask',
            image_url='http://example.com/image4.jpg'
        ),
        Project(
            title='Shoe Hub',
            description='Shoe Hub is a fully responsive e-commerce website that focuses on providing the best online shopping experience for users interested in buying shoes.',
            link='http://example.com/shoe-hub',
            technologies='JavaScript, React, Python, Flask',
            image_url='http://example.com/image5.jpg'
        ),
    ]

    for project in projects:
        db.session.add(project)
        db.session.commit()  # Commit after each project

    # Seed Skill data
    skills = [
        Skill(name='Python', proficiency='Expert', description='Python programming language', image_url='http://example.com/skill1.jpg', features='Web Development, Data Analysis', category='Programming'),
        Skill(name='JavaScript', proficiency='Expert', description='JavaScript programming language for web development.', image_url='http://example.com/skill2.jpg', features='Front-end and Back-end development', category='Programming'),
        Skill(name='React', proficiency='Intermediate', description='A JavaScript library for building user interfaces.', image_url='http://example.com/skill3.jpg', features='Component-based architecture, Virtual DOM', category='Programming'),
        Skill(name='SQL', proficiency='Intermediate', description='Structured Query Language for managing databases.', image_url='http://example.com/skill4.jpg', features='Data manipulation and retrieval', category='Database'),
        Skill(name='HTML', proficiency='Expert', description='Markup language for creating web pages.', image_url='http://example.com/skill5.jpg', features='Semantic structure of web content', category='Web Development'),
        Skill(name='CSS', proficiency='Expert', description='Style sheet language for designing web pages.', image_url='http://example.com/skill6.jpg', features='Responsive design, Flexbox, Grid', category='Web Development'),
        Skill(name='Flask', proficiency='Intermediate', description='A micro web framework for Python.', image_url='http://example.com/skill7.jpg', features='Lightweight, modular, and easy to get started', category='Web Frameworks'),
        Skill(name='Git', proficiency='Intermediate', description='Version control system for tracking changes in source code.', image_url='http://example.com/skill8.jpg', features='Collaboration, version tracking', category='Tools'),
        Skill(name='Adobe Illustrator', proficiency='Intermediate', description='Vector graphics editor for graphic design.', image_url='http://example.com/skill9.jpg', features='Creating logos, illustrations, and graphics', category='Design'),
        Skill(name='Photoshop', proficiency='Intermediate', description='Raster graphics editor for photo editing.', image_url='http://example.com/skill10.jpg', features='Photo retouching, digital art', category='Design'),
    ]

    for skill in skills:
        db.session.add(skill)
        db.session.commit()  # Commit after each skill

    # Seed BlogPost data
    blog_posts = [
        BlogPost(title='Flask Basics', content='Content of Flask basics', author='Felix kiprotich', image_url='http://example.com/blog1.jpg', tags='Flask, Python', summary='A summary of Flask basics', reading_time='5 min read', external_link='http://example.com/blog/flask-basics'),
        BlogPost(title='Introduction to SQLAlchemy', content='Content of SQLAlchemy', author='Anita Kahenya', image_url='http://example.com/blog2.jpg', tags='SQLAlchemy, Flask', summary='A summary of SQLAlchemy', reading_time='7 min read', external_link='http://example.com/blog/introduction-to-sqlalchemy'),
        BlogPost(title='How to Integrate the Mpesa Express API in Flask and React JS Real World Project', content='Content about integrating Mpesa Express API...', author='Computeman', image_url='http://example.com/blog3.jpg', tags='Mpesa, Flask, React', summary='Guide on integrating Mpesa with Flask and React.', reading_time='10 min read', external_link='http://example.com/blog/mpesa-integration'),
        BlogPost(title='Navigating the World of Data Structures in Python: A Beginner\'s Guide', content='Content about data structures in Python...', author='Ecee chain', image_url='http://example.com/blog4.jpg', tags='Python, Data Structures', summary='A guide for beginners on data structures.', reading_time='8 min read', external_link='http://example.com/blog/data-structures-python'),
        BlogPost(title='Python Prowess: A Beginner\'s Odyssey into the World of Programming Magic!', content='Content about Python programming...', author='Ecee chain', image_url='http://example.com/blog5.jpg', tags='Python, Programming', summary='A beginner\'s journey into Python programming.', reading_time='6 min read', external_link='http://example.com/blog/python-prowess'),
        BlogPost(title='My First Blog', content='Content of my first blog post...', author='Ecee chain', image_url='http://example.com/blog6.jpg', tags='Personal, Blog', summary='My journey in blogging.', reading_time='4 min read', external_link='http://example.com/blog/my-first-blog'),
    ]

    for post in blog_posts:
        db.session.add(post)
        db.session.commit()  # Commit after each blog post

    print("Seeding complete!")
