Help on module sendemail:

NAME
    sendemail - Create and send an email

DESCRIPTION
    This program will generate a fake email to send from, but will allow the user
    to change that to a different value.   The program will also attempt to find
    a valid SMTP host to use for sending the message and will prompt the user to
    enter one if a valid host is not found.   The program will then allow the user
    to enter a recepient and also create a message.

FUNCTIONS
    get_host()
        return a valid SMTP host, if found
    
    main()
    
    prompt(text)
    
    sender_name()
        generate random email sender
        from:
        https://stackoverflow.com/questions/18834636/random-word-generator-python

