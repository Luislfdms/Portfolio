from flask import Blueprint, render_template
from . import experience_bp

# Route and view function for the experience page
@experience_bp.route('/')
def experience():
    accomplished = ["Decreased the latency for a critical system used by 500+ teams by implementing a pub/sub based \
                     messaging/notification system and deploying a cache using a memcached based tool.", 
                    "Developed a framework for developers to detect regression in their code changes earlier in the SDLC \
                     lifecycle by providing an early detection A/B testing mechanism."]
    technology = ["Large Scale Load Testing", "Golang", "MSA(Micro Srver Architecture)", "CI/CD Systems", "Protobuf", "Python", "A/B Testing"]
    learned = "During my time at google I learned so much, not just about technologies and tools used at work but also working with other people and \
               realizing my own style of work and how I best produce results. Some mistakes I caught myself making was dwelving too deep into documents \
               trying to learn an excessive amount of information by myself when a 10 minute chat with a co-worker could provide me with all the information \
               I need and move my project along faster. I had 2 projects during my internship, the first was rather straightforward and were told \
               what to do, the second however was more ambigous and open-ended. The way my hosts set this up was perfect as I got to experience \
               executing a solution created by another to fix a problem, and creating my own solution with the help and coordination of others then \
               executing it. Altough I only spent 3 months there I believe my skills in software engineering and work in general grew exponentially \
               thanks to my effort and the assistance of the amazing engineers I was surrounded by."

    # Render the "projects.html" template with the provided data
    return render_template('experience.html', accomplished=accomplished, technology=technology, learned=learned)