import requests
class Employee(object):
    """A sample exployee class"""
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first=first #set employee first name
        self.last=last #set employee last name
        self.pay=pay #set employee pay

    #This is a property decorator, this is pythons way of creating getters
    #and setters. So if an employees name is changed, the changes should be reflected
    #in the employees email
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Reponse!'
