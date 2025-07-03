class HelloSolution:

    # friend_name = unicode string
    def hello(self, friend_name):
        validate_unicode_string(friend_name)
        return f"Hello, {friend_name}!"


# Helpers
def validate_unicode_string(input):
    if not isinstance(input, str):
        raise Exception(
            f"Invalid input: {input}. Valid inputs must be unicode strings."
        )

