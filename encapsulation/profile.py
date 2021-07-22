import re

class Profile:

    def __init__(self, username: str, password: str):
        if 5 <= len(username) <= 15:
            self.username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")


        pattern = "[A-Za-z0-9]{8}"
        if re.match(pattern, password):
            self.password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        stars = "*" * len(self.password)
        return f"You have a profile with username: \"{self.username}\" and password: {stars}"

#profile_with_invalid_password = Profile('My_username', 'My-password')
#print(profile_with_invalid_password)

#profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
