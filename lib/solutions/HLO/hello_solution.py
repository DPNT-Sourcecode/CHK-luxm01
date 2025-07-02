
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        validate_unicode_string(friend_name)
        return f"Hello, {friend_name}!"
    
# Helpers
def validate_unicode_string(string):
    if not isinstance(string, unicode):
        raise Exception(f"Invalid input {string}. Valid inputs must be unicode strings.")


