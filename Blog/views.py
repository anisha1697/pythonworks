from Blog.models import users,posts

def signin_required(fn):
  def wrapper(*args,**kwargs):
      if "user" in session:
          return fn(*args,**kwargs)
      else:
          print("invalid session u login")
  return wrapper




# print(users)
# username="akhil"
# password="Password@123"
# user=[ user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("success")
# else:
#     print("denied")
session={}
def authentificate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[ user for user in users if user["username"]==username and user["password"]==password]
    return user
# print(authentificate(username="akhil",password="Password@123"))
class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authentificate(username=username,password=password)
        if user:
            session["user"]=user[0]
        # print(session)

class PostListview:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        post=kwargs.get("data")
        post["userId"]=session["user"]["id"]
        posts.append(post)
        print(posts[-1])




class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post
class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])



log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
all_post=PostListview()
my_post={
    "postId":6,"title":"hello good morning","content":"mycontent","likedby":[]
}
all_post.post(data=my_post)
mypost=MyPostListView()
# print(mypost.get())
like=AddLike()
like.post(postid=1)

