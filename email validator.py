Email=input('Enter a email id:')
Email
Email
def Email_Validator(email):
    if (len(email)>256):
        print(0)
        if '@' in email:
            if email.count('@')>1:
                print(0)
        else:
            status= 1
    else:
      print(0)

    local_domain=email.split('@')
    status_local=Validate_Local('local')
    status_domain=Validate_Domain('domain')
    if status_local==1 and status_domain==1:
      status=1
    else:
      status=0
      print(status)
def Validate_Local(local):
    if first_char==isalpha() or first_char=='_':
          status_local=1
    else:
        status_local=0
    print(status_local)
def Validate_Domain(domain):
    last=domain.split('.')[-1]
    if last=='org' or last=='edu' or last=='com':
              status_domain=1
    else:
        status_domain=0
        print(status_domain)