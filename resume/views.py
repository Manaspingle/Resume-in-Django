from django.shortcuts import render


def resume(request):
    context = {
        "profile": {"name": "Manas P.", "role": "Computer Science Student & Developer", "location": "India", "email": "hello@manas.dev", "phone": "+91 98765 43210", "initials": "MP"},
        "objective": "To build thoughtful, accessible software while growing as a full-stack developer and contributing to products that solve real problems.",
        "education": [{"period": "2023 - 2027", "degree": "Bachelor of Technology in Computer Science", "school": "Your University", "detail": "Coursework in programming, data structures, databases and web technology."}],
        "skills": ["Python", "Django", "HTML & CSS", "JavaScript", "SQL", "Git", "Problem Solving"],
        "certifications": ["Python Programming Fundamentals", "Web Development with Django", "Introduction to Cloud Computing"],
        "projects": [
            {"name": "Personal Portfolio", "description": "A responsive portfolio that presents projects, skills and contact details in one clear place.", "tags": ["Django", "HTML", "CSS"]},
            {"name": "Campus Activity Tracker", "description": "A simple web platform for discovering events, registering participation and tracking progress.", "tags": ["Python", "SQLite", "JavaScript"]},
        ],
        "achievements": ["Completed hands-on Python and object-oriented programming projects.", "Built and presented a responsive web application as an academic project.", "Regularly practice algorithmic problem solving on coding platforms."],
        "strengths": ["Curious learner", "Clear communicator", "Team player", "Consistent and organized"],
        "weaknesses": ["Can spend too long polishing details", "Working on public speaking confidence"],
        "hobbies": ["Reading technology blogs", "Photography", "Playing chess", "Exploring new tools"],
        "links": [{"label": "GitHub", "url": "https://github.com/", "handle": "github.com/manas"}, {"label": "LinkedIn", "url": "https://www.linkedin.com/", "handle": "linkedin.com/in/manas"}, {"label": "HackerRank", "url": "https://www.hackerrank.com/", "handle": "hackerrank.com/manas"}, {"label": "LeetCode", "url": "https://leetcode.com/", "handle": "leetcode.com/manas"}],
    }
    return render(request, "resume/index.html", context)