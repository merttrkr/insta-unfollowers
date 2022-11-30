import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

L = instaloader.Instaloader()

# Login or load session
username = ""
password = ""
try:
    L.login(username, password)
except TwoFactorAuthRequiredException:
    tfaCode = input("enter 2fa code")
    L.two_factor_login(tfaCode)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followees
follower_list = []
followee_list = []
count = 0
for follower in profile.get_followers():
    follower_list.append(follower.username)
for followee in profile.get_followees():
    followee_list.append(followee.username)

s = set(follower_list)
unfollowers = [x for x in followee_list if x not in s] # loops in followed list x is single followed
# checks if x is in follower list
print(unfollowers)


