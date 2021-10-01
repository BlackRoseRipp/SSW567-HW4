from github import Github

def getGithubInfo(username):
    info = []
    g = Github()

    user = g.get_user(username)

    for repo in user.get_repos():
        info.append(repo.name + ': ' + str(repo.get_commits().totalCount) + " commits")

    return info

print(getGithubInfo("BlackRoseRipp"))