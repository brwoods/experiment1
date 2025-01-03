import pyperclip
def clean_up_email():
    '''
        This function removes the leading '>' characters from each line of the copied text. 
        It is useful for cleaning up email text that has been copied from an email client. 
        It removes the '>' characters that are used to indicate quoted text in email replies. 
        The cleaned text is then copied back to the clipboard.
    '''
    text = pyperclip.paste()
    lines = text.splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].lstrip(' >')
    text = '\n'.join(lines)
    pyperclip.copy(text)
if __name__ == '__main__':   
    clean_up_email()