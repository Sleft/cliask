# -*- coding: utf-8 -*-

## @package cliask
#
#  A module for getting validated user input via the console.

import re


## Ask for input until a valid response is given and return the
#  response.
#  @param question         A string containing a question asking for
#                          input.
#  @param default          A default answer if the user gives no
#                          answer (default: None).
#  @param validator        A regex, function, tuple or list to
#                          validate the question (default: None). If
#                          it is a regex the input must match it to be
#                          validated. If it is a function the function
#                          must take the input as a parameter and
#                          return true if the input is valid. If it is
#                          a tuple or a list the input must be an
#                          element in it to valid.
#  @param invalid_response A string containing the response to print
#                          when invalid input is entered (default:
#                          None).
#  @return The validated input.
def ask(question, default='', validator='',
        invalid_response=''):

    if default:
        question = '{} |{}| '.format(question.strip(), default)

    while True:
        answer = input(question)

        # If there is no input and a default is given, return the
        # default.
        if not answer and default:
            answer = default
            break

        # If there is input but no validator, return the input.
        if not validator:
            break

        # If there is a validator, return the input if it is valid.
        if _validate(validator, answer):
            break

        print(invalid_response)

    return answer


## Ask for yes or no until a valid response is given and return True
#  if the answer is yes.
#
#  @param question         A string containing a question asking for
#                          input.
#  @param default          A default answer if the user gives no
#                          answer (default: None).
#  @param validator        A regex, function, tuple or list to
#                          validate the question (default: a regex for
#                          yes and no). If it is a regex the input
#                          must match it to be validated. If it is a
#                          function the function must take the input
#                          as a parameter and return true if the input
#                          is valid. If it is a tuple or a list the
#                          input must be an element in it to valid.
#  @param invalid_response A string containing the response to print
#                          when invalid input is entered (default:
#                          Please enter "yes" or "no").
#  @return The validated input.
def agree(question, default='', validator=r'(?i)\Ay(?:es)?|no?\Z',
          invalid_response='Please enter "yes" or "no"'):
    if ask(question,
           default=default,
           validator=validator,
           invalid_response=invalid_response)[0].lower() == 'y':
        return True
    else:
        return False


## Returns true if the given validator validates the given input.
#  @param validator See ask().
#  @param s         Input string to validate.
#  @return True if the given validator validates the given input.
def _validate(validator, s):
    valid = False
    # If the validator is a function.
    if (hasattr(validator, '__call__')):
        if validator(s):
            return True
    elif type(validator) is list or type(validator) is tuple:
        if s in validator:
            return True
    elif re.search(validator, s):
        return True
    return False


## Unit test by an example of usage.
def _test():
    ## Checks if input is within a range.
    #  @param input Input string to check.
    #  @return True if input is within range.
    def in_range(s):
        number = ''

        try:
            number = int(s)
        except ValueError:
            pass

        return number in range(1, 11)

    print('Please answer the following questions:')

    # If you use cliask from another module you have to prefix it with
    # its module name, i.e. call cliask.ask and cliask.agree.
    ynq = ask('Yes or no or quit? ',
              validator=r'(?i)[ynq]',
              invalid_response='Answer y or n for yes or no',
              default='y')

    number = ask('A number between 1 and 10: ',
                 validator=in_range,
                 invalid_response='You must specify a number between 1 and 10')

    animal = ask('Cow or cat? ',
                 validator=('cow', 'cat'),
                 invalid_response='You must say cow or cat')
    yn = agree('Yes or no? ')

    q = ask('Why? ')

    print('You answered:')
    print(ynq)
    print(number)
    print(animal)
    print(q)
    print(yn)

if __name__ == '__main__':
    _test()
