import xml.etree.ElementTree

def goodTime(creationDate):
    time = creationDate.split('T')[1][:8].split(':')
    return 0 <= int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[0]) <= 6 * 60 * 60


def getQuestions(comments, _posts, _users):
    posts = {}
    users = {}
    correct_post = {}
    user_by_name = {}
    max_comments = 0
    tree = xml.etree.ElementTree.parse(comments)
    posts_tree = xml.etree.ElementTree.parse(_posts)
    users_tree = xml.etree.ElementTree.parse(_users)
    root = tree.getroot()
    posts_root = posts_tree.getroot()
    users_root = users_tree.getroot()
    for post in range(len(posts_root)):
        correct_post[posts_root[post].attrib['Id']] = int(posts_root[post].attrib['PostTypeId'])
    for user in range(len(users_root)):
        users[users_root[user].attrib['Id']] = int(users_root[user].attrib['Reputation'])
        user_by_name[users_root[user].attrib['DisplayName']] = int(users_root[user].attrib['Id'])
    for comment in range(len(root)):
        try:
            if correct_post[root[comment].attrib['PostId']] == 1 and goodTime(root[comment].attrib['CreationDate']) and (users[root[comment].attrib['UserId']] > 100 if 'UserId' in root[comment].attrib.keys() else user_by_name[root[comment].attrib['UserDisplayName']] > 100):
                posts[root[comment].attrib['PostId']] = posts.get(root[comment].attrib['PostId'], 0) + 1
                max_comments = max(max_comments, posts[root[comment].attrib['PostId']])
        except:
            #no such user in database
            pass
    good_posts = []
    for question in posts:
        if posts[question] == max_comments:
            good_posts.append(question)
    return good_posts, max_comments