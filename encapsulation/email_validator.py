import re


class EmailValidator:
    
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains


    def get_username(self, email):
        username_re = "@"
        return re.split(username_re, email)[0]


    def get_mail(self, email):
        re1 = "@"
        re2 = "\."
        mail = re.split(re1, email)[1]
        email_provider = re.split(re2, mail)[0]
        return email_provider

    def get_domain(self, email):
        re1 = "@"
        re2 = "\."
        mail = re.split(re1, email)[1]
        domain = re.split(re2, mail)[1]
        return domain


    def __is_name_valid(self, name):
        if len(name) < self.min_length:
             return False
        return True
    

    def __is_mail_valid(self, email_provider):
        if email_provider in self.mails:
            return True
        return False



    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        re1 = "@"
        re2 = "\."
        name, mail = re.split(re1, email)
        email_provider, domain = re.split(re2, mail)

        if self.__is_name_valid(name) and\
             self.__is_mail_valid(email_provider) and\
                  self.__is_domain_valid(domain):
                  return True
        return False




mails = ["me"]
domains = ["you", "he"]
email_validator = EmailValidator(5, mails, domains)
print(email_validator._EmailValidator__is_mail_valid("me"))

