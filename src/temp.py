import get_methods

repos = get_methods.get_git_repos('/home/konstantinos/personal/repos')
#Print git repos list
for i in range(0, len(repos)):
    print(i)
    print(repos[i][0])
    print(repos[i][1] + "\n")

