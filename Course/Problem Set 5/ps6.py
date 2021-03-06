import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(word_list, 'bat') returns
    True
    # >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        import string
        lower_case_list = []  # empty string list
        for letter in string.ascii_lowercase:  # create a lowercase list
            lower_case_list.append(letter)
        upper_case_list = []  # empty string list
        for letter in string.ascii_uppercase:
            upper_case_list.append(letter)
        dict = {}  # empty dict
        index = 0
        while index < 26:
            if index + shift < 26:
                dict[string.ascii_lowercase[index]] = lower_case_list[index + shift]
                index += 1
            else:
                dict[string.ascii_lowercase[index]] = lower_case_list[index + shift - 26]
                index += 1
        index = 0
        while index < 26:
            if index + shift < 26:
                dict[string.ascii_uppercase[index]] = upper_case_list[index + shift]
                index += 1
            else:
                dict[string.ascii_uppercase[index]] = upper_case_list[index + shift - 26]
                index += 1
        return dict
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dict = self.build_shift_dict(shift)
        text_list = []
        lower_and_upper = string.ascii_lowercase + string.ascii_uppercase
        for letter in self.get_message_text():
            text_list.append(letter)
        index = 0
        while index != len(text_list):
            if text_list[index] in lower_and_upper:
                text_list[index] = dict[text_list[index]]
                index += 1
            else:
                index += 1
        return ''.join(text_list)


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        text_list = self.message_text.split(' ')
        text_length = len(text_list)
        shift = 0
        best_shift = 0
        valid_word = 0
        while shift in range(0, 25):  # Testing each shift
            # print(shift)
            previous_valid_word = valid_word
            valid_word = 0
            for word in text_list:  # In each shift test, test all words in the string
                text = Message(word)
                decrypt = text.apply_shift(shift)
                # print(decrypt)
                if is_word(self.valid_words, decrypt):  # Check if that word is valid
                    valid_word += 1
            if valid_word == 0:
                shift += 1
            elif text_length - valid_word < text_length - previous_valid_word:
                best_shift = shift
                shift += 1
            elif text_length - valid_word >= text_length - previous_valid_word:
                shift += 1
        ans_list = []
        # print('The best shift is ' + str(best_shift))
        for word in text_list:
            text = Message(word)
            decrypt = text.apply_shift(best_shift)
            ans_list.append(decrypt)
        ans_string = ' '.join(ans_list)
        ans_tup = (best_shift, ans_string)
        return ans_tup



# Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq')
# print('Expected Output:', (24, 'hello'))
# print('Actual Output:', ciphertext.decrypt_message())


# Function for testing
def all_shift_test(text):
    fail_list = []
    for shift in range(0, 26):
        print('Current shift: ', shift)
        plaintext = PlaintextMessage(text, shift)
        encryption = plaintext.get_message_text_encrypted()
        ciphertext = CiphertextMessage(encryption)
        if ciphertext.decrypt_message()[1] != text:
            fail_list.append(str(shift))
    if len(fail_list) == 0:
        print('Every shift is ok!')
    else:
        print('Shift: ', ', '.join(fail_list), 'is not working!')


# all_shift_test('nerf, this!')
# all_shift_test('happy')

def decrypt_story():
    text = get_story_string()
    Story = CiphertextMessage(text)
    return Story.decrypt_message()
