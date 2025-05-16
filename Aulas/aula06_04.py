def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False


if email_valido('123'):
    print('E-mail válido!')
else:
    print('E-mail inválido.')

if email_valido('teste'):
        print('E-mail válido!')
else:
    print('E-mail inválido.')

if email_valido('@'):
    print('E-mail válido!')
else:
    print('E-mail inválido.')


if email_valido('a@'):
    print('E-mail válido!')
else:
    print('E-mail inválido.')

if email_valido('a@.com'):
    print('E-mail válido!')
else:
    print('E-mail inválido.')

if email_valido('a@b.com'):
    print('E-mail válido!')
else:
    print('E-mail inválido.')

