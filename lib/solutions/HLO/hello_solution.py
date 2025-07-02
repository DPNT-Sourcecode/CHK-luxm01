
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        return f"Hello, {friend_name}!"
    
    def validate_unicode_string(string):
        if not isinstance(string, unicode):
            raise Exception(f"")

