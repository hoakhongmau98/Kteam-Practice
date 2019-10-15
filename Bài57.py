class MyError(Exception):
     """My own exception class
# Bài Python 57, Code by Quantrimang.com
     Attributes:
        msg -- explanation of the error
     """

     def __init__(self, msg):
        self.msg = msg

error = MyError("Có gì đó sai sai!")
print (error)