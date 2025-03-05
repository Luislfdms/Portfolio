from flask import Blueprint, render_template
from . import experience_bp

# Route and view function for the experience page
@experience_bp.route('/')
def experience():
    accomplished = [["Decreased the latency for a critical system used by 500+ teams by implementing a pub/sub based \
                     messaging/notification system and deploying a cache using a memcached based tool.", 
                    "Developed a framework for developers to detect regression in their code changes earlier in the SDLC \
                     lifecycle by providing an early detection A/B testing mechanism."],
                    ["Migrated a critical report workflow orchestration from a Lua based graph execution api to its python interface", \
                     "Introduced modern CI/CD technologies, including docker and automated deployment software", \
                     "to reduce manual touching in deployment and significantly reduce development time and overall efficiency."
                    ]]

    technology = [["Large Scale Load Testing", "Golang", "MSA(Micro Srver Architecture)", "CI/CD Systems", "Protobuf", "Python", "A/B Testing"], 
                  ["Lua", "Python", "Docker", "CI/CD Systems", "GCP"]]
    
    learned = ["During my time at google I learned so much, not just about technologies and tools used at work but also working with other people and \
               realizing my own style of work and how I best produce results. Some mistakes I caught myself making was dwelving too deep into documents \
               trying to learn an excessive amount of information by myself when a 10 minute chat with a co-worker could provide me with all the information \
               I need and move my project along faster. I had 2 projects during my internship, the first was rather straightforward and were told \
               what to do, the second however was more ambigous and open-ended. The way my hosts set this up was perfect as I got to experience \
               executing a solution created by another to fix a problem, and creating my own solution with the help and coordination of others then \
               executing it. Altough I only spent 3 months there I believe my skills in software engineering and work in general grew exponentially \
               thanks to my effort and the assistance of the amazing engineers I was surrounded by.", "As I continued my journey in software engineering at \
               bloomberg I learned a lot about a different sector of the technology industry. \
                I learned about the importance of testing and how it can save a company millions of dollars in the long run. I learned about the importance \
                of communication and how it can make or break a project. I learned about the importance of documentation and how it can save you hours \
                of time in the future. I learned about the importance of asking questions and how it can save you hours of time in the future. All of these things \
                I learned at Bloomberg helped me grow as a software engineer and I am excited to continue to learn and grow in the future."]

    # Render the "projects.html" template with the provided data
    return render_template('experience.html', accomplished=accomplished, technology=technology, learned=learned)