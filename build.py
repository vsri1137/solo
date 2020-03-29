
# reads in template with top/bottom html
template = open("templates/base.html").read()

pages = [  # list with metadata on pages
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About me",
    },
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Blog",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
]

def content_extractor():  # this function iterates through pages list and extracts content

    for page in pages:  # iterates through each item in list
        # pull page location from dictionary
        content = open(page["filename"]).read() 
        finished_page = template.replace("{{placeholder}}", content)
        open(page["output"], "w+").write(finished_page)

content_extractor()


