def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False
