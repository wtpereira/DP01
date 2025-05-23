# def email_valido(email):
#     if email.find('@') >= 1 and email.find('.com') >= 3:
#         return True
#     else:
#         return False

email_valido = lambda email: True if (email.find('@') >= 1 and email.find('.com') >= 3) else False