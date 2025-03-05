from flask import Blueprint, render_template
from . import projects_bp

# Route and view function for the projects page
@projects_bp.route('/')
def projects():
    # Define any variables you want to pass to the template
    projects_list = [['League Stats', 'Discord bot that can be added to a channel and allows users to lookup users League of Legends stats \
                      of members of the channel or anybody else in general if they have their username. With initial setup you can link \
                      your league of legends username to your discord which allows users to lookup your stats using your discord name in the \
                      case that they dont know your usename. The names are saved in a mysql database and the bot is ran on an AWS instance.'], 
                     ['This Website!','I have been wanting to create a website incorporating flask for a while and then I realized well I still \
                       not have a portfolio site! Overall This site was really fun to make however I did run into a couple issues such as the home \
                       page which took me a while to get right but in the end I believe it was well worth it. I will be hosting it on render \
                       as it has great support for flask applications and I already have experience with google cloud and AWS already so I want to try something new.'], 
                     ['Barker','Barker is a X (Twitter) clone created by me and my group for Proccess of Software Engineering class for our Mern Project \
                       where I was the project lead. We had a limited time frame for the assignment therefore we werent able to roll out all of our \
                       expected features however I plan on continuing to work on this project further. Currently users are able to create an account \
                       with 2 factor authentication using email (which we built ourselves), create posts, delete posts, and like/dislike posts. \
                       Features which I plan to work on include, profile pictures, post images, following, and recommended feed.']]
    technology = [['Python','AWS','Riot API', 'discord.py','selenium','mysql'],
                  ['Python', 'HTML/CSS', 'JavaScript', 'Flask', 'Render', 'Web Development'],
                  ['React', 'Express.js', 'Node.js', 'MongoDB', 'HTML/CSS', 'Node Mailer']]

    # Render the "projects.html" template with the provided data
    return render_template('projects.html', projects_list=projects_list, technology=technology)

@projects_bp.route('/projects')
def technology_list(elements):
    elements = [['Python','AWS','Riot API', 'discord.py','selenium','mysql']]
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return render_template('projects.html', content=string)
