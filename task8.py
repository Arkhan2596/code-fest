class possible_palindrome (object):
    def __init__(self, word):
        self.word = word
    def checking_palindrome(self):
        if self.word[::-1] == self.word:
            print('This string is a palindrome.')
        else:
            print('This sting is not a palindrome.')

word = input('Enter string : ')
string_check = possible_palindrome(word)
string_check.checking_palindrome()