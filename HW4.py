import requests

def getGithubInfo(username):
    repos = requests.get('https://api.github.com/users/'+username+'/repos').json()
    if not isinstance(repos, list):
        if repos['message'] == "Not found":
            return "User not found"
        return "Invalid response"

    info = []
    for repo in repos:
        commits = requests.get(
            'https://api.github.com/repos/'+username+'/'+repo['name']+'/commits').json()
        info.append([repo['name'], len(commits)])
    return info

#print(getGithubInfo("BlackRoseRipp"))