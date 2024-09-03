# determine if the given string should be translated to English or Braille

def determine_language(text):
    # if the text contains any non-ascii characters, it is assumed to be in English
    if any(ord(char) > 127 for char in text):
        return 'english'
    else:
        return 'braille'