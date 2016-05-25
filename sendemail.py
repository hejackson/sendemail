#!/usr/local/bin/python3
"""Create and send an email

This program will generate a fake email to send from, but will allow the user
to change that to a different value.   The program will also attempt to find
a valid SMTP host to use for sending the message and will prompt the user to
enter one if a valid host is not found.   The program will then allow the user
to enter a recepient and also create a message.
"""

import tempfile
import subprocess
import os
import requests
import random
import smtplib


def sender_name():
    """generate random email sender
    from:
    https://stackoverflow.com/questions/18834636/random-word-generator-python
    """

    word_site = ("https://svnweb.freebsd.org/csrg/share/dict/words?"
                 "view=co&content-type=text/plain")

    response = requests.get(word_site, 'html.parser')
    words = [word for word in response.text.splitlines() if len(word) > 4]
    name = random.choice(words).lower()
    domain = random.choice(words).lower()
    sender = name + '@' + domain + '.com'

    return sender


def prompt(text):
    return input(text).strip()


def get_host():
    """return a valid SMTP host, if found"""
    import telnetlib

    hosts = ['outbound.cisco.com']
    host = ''
    while hosts:
        try:
            host = hosts.pop()
            tn = telnetlib.Telnet(host, 25, 3)
            tn.close()
            break
        except:
            host = ''
            pass

    return host


def main():
    fake_from = sender_name()
    from_address = prompt('From [{}]: '.format(fake_from))
    if from_address == '':
        from_address = fake_from

    recepient = prompt('To: ')
    subject = prompt('Subject: ')

    message = ("From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n"
               .format(from_address, recepient, subject))

    smtphost = get_host()
    if not smtphost:
        smtphost = prompt('SMTP host: ')

    EDITOR = os.environ.get('EDITOR', 'vim')
    initial_message = "Please edit this file..."

    with tempfile.NamedTemporaryFile(suffix='.tmp', mode='w') as tf:
        tf.write(initial_message)
        tf.flush()
        subprocess.call([EDITOR, tf.name])

        with open(tf.name, 'r') as newfile:
            message += newfile.read()

    server = smtplib.SMTP(smtphost)
    server.set_debuglevel(1)
    server.sendmail(from_address, recepient, message)
    server.quit()


if __name__ == '__main__':
    main()
