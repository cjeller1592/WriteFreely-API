import writefreely
import re

def getAll(alias):
    c = writefreely.client('write.house')

    list = []

# I assume 100 posts is more than generous!
    for i in range(1,100):
# Iterate through the pages...
        cposts = c.retrieveCPosts(alias, i)
        posts = cposts['posts']
# If the posts are not an empty list, take each post and put it in a list!
# That way it catches pages that don't have 10 posts
        if posts != []:
            for post in posts:
# Append to the list of posts
                list.append(post)

        else:
            break

    return list

def searchC(alias, term):

    list = []

    posts = getAll(alias)

#    code.interact(local=locals())

    for post in posts:
        body = post['body']

        result = re.findall(term, body, re.IGNORECASE)

        if result != []:
            list.append(post)

        else:
            continue

    return list

def test():
    c = writeas.client()
    post = c.retrieveCPost('bix', 'stepping-back')
    return(post)
