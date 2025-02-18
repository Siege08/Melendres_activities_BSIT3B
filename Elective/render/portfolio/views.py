from django.shortcuts import render

def dashboard(request):
    # Dashboard statistics
    stats_data = [
        {"title": "Users", "count": 150, "icon": "fa-users"},
        {"title": "Orders", "count": 320, "icon": "fa-shopping-cart"},
        {"title": "Revenue", "count": "$12,450", "icon": "fa-dollar-sign"},
        {"title": "Projects", "count": 25, "icon": "fa-project-diagram"},
    ]
    
    # Profile information
    profile_data = {
        "name": "John Carlo Melendres",
        "bio": "I love creating innovative solutions and learning new technologies.",
        "profile_pic": "images/profile_1.jpg",
        "role": "Full Stack Developer",
        "skills": ["Python", "Django", "JavaScript", "HTML/CSS", "React"],
    }
    
    # Social links
    social_links = [
        {
            "platform": "Instagram",
            "url": "https://instagram.com/jcrlo.m",
            "icon": "fab fa-instagram"
        },
        {
            "platform": "GitHub",
            "url": "https://github.com/Siege08",
            "icon": "fab fa-github"
        },
        {
            "platform": "Facebook",
            "url": "https://facebook.com/jcrlo.m",
            "icon": "fab fa-facebook"
        },
    ]

    # Navigation menu items
    nav_items = [
        {"title": "Home", "url": "/", "icon": "fas fa-home"},
        {"title": "Reports", "url": "#", "icon": "fas fa-chart-bar"},
        {"title": "Settings", "url": "#", "icon": "fas fa-cog"},
        {"title": "Profile", "url": "#", "icon": "fas fa-user"},
        {"title": "Contact", "url": "#", "icon": "fas fa-envelope"},
    ]

    context = {
        'stats_data': stats_data,
        'profile': profile_data,
        'social_links': social_links,
        'nav_items': nav_items,
    }
    return render(request, 'portfolio/dashboard.html', context)