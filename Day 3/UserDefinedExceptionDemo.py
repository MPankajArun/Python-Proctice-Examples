class MyError(Exception):
    pass

try:
    raise MyError("Some infomration about what went wrong")
except MyError as error:
    print("Situation: ",error)
