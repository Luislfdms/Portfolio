from flask import Blueprint, render_template
from . import projects_bp

# Route and view function for the projects page
@projects_bp.route('/')
def projects():
    # Define any variables you want to pass to the template
    projects_list = [['League Stats', 'Discord bot that can be added to a channel and allows users to lookup legue of legends stats \
                      of members of the channel or anybody else in general if they have their username. With initial setup you can link \
                      your league of legends username to your discord which allows users to lookup your stats using your discord name in the \
                      case that they dont know your usename. The names are saved in a mysql database and the bot is ran on an AWS instance.'], 
                     ['This Website!','I have been wanting to create a website incorporating flask for a while and then I realized well I still \
                       not have a portfolio site! Overall This site was really fun to make however I did run into a couple issues such as the home \
                       page which took me a while to get right but in the end I believe it was well worth it. I will be hosting it on render \
                       as it has great support for flask applications and I already have experience with google cloud and AWS already so I want to try something new.'], 
                     ['Travel Pal','Example Description']]
    technology = [['Python','AWS','Riot API', 'discord.py','selenium','mysql'],
                  ['Python', 'HTML/CSS', 'JavaScript', 'Flask', 'Render', 'Web Development']]

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
