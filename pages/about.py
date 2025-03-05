from flask import Blueprint, render_template
from . import about_bp

# Route and view function for the about page
@about_bp.route('/')
def about():
    # Define variables to pass dynamic data to the template
    about_text = "I am a Senior at the University of Central Florida pursuing my \
                  Bachelor's in Computer Science. My professional interest lies in Software Engineering \
                  where I haven't found my niche however I hope that through more experiences working in \
                  the industry I'll find the area that best suits me as a developer. Originally I wanted to study \
                  Aerospace Engineering, however after taking a computer science course in high school with a friend \
                  I found that software engineering allows me to freely create and explore the possibilities of my mind \
                  I never previously thought about. I always had a passion for computers and building things, and this career \
                  allows me to seamlessly blend the two together."
    contact_email = "luislfdms18@gmail.com"
    contact_phone = "+1 407-572-4961"
    linkedin_link = "https://www.linkedin.com/in/luis-souto/"
    github_link = "https://github.com/Luislfdms"
    
    # Render the "about.html" template with the provided data
    return render_template('about.html', about_text=about_text, contact_email=contact_email, 
                           contact_phone=contact_phone, linkedin_link=linkedin_link, github_link=github_link)
