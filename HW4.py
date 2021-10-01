import sys
sys.path.insert(0, r"C:\Users\Owner\AppData\Local\Programs\Python\Python38\Lib\site-packages")

from github import Github

username = "BlackRoseRipp"
g = Github()

user = g.get_user(username)

for repo in user.get_repos():
    print(repo.name, ': ', repo.get_commits().totalCount, " commits")
