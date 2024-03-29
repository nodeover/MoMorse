morse_to_alpha = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '..--..': '?', '-..-.': '/', '--..--': ',', 
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-',
    '-..-.': '/', '.--.-.': '@', '.-..-.': '"', '..--.-': '_', '---...': ':',
    '.----.': "'", '.-.-.': '+', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---..-': '=', '..-.-': ' ', '..--../': ' '
}
def mo_morse_string_decoder(morse_code):
    decoded_message = ''
    for word in morse_code.split('/'):
        for letter in word.split():
            decoded_message += morse_to_alpha.get(letter, '')
        decoded_message += ' '
    decoded_message.strip()
    return decoded_message
    
morse_to_alpha = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '..--..': '?', '-..-.': '/', '--..--': ',', 
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-',
    '-..-.': '/', '.--.-.': '@', '.-..-.': '"', '..--.-': '_', '---...': ':',
    '.----.': "'", '.-.-.': '+', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---..-': '=', '..-.-': ' ', '..--../': ' '
}
alpha_to_morse = {value: key for key, value in morse_to_alpha.items()}


def mo_morse_string_decoder(morse_code):
    decoded_message = ''
    for word in morse_code.split('/'):
        for letter in word.split():
            decoded_message += morse_to_alpha.get(letter, '')
        decoded_message += ' '
    decoded_message.strip()
    return decoded_message
    

def mo_morse_string_encoder(text):
    text = text.upper().strip()
    encoded_message = ''
    
    for word in text.split(' '):
        for letter in word:
            encoded_message += alpha_to_morse.get(letter, '') + ' '
        encoded_message = encoded_message.rstrip() + '/'
        
    return encoded_message.rstrip('/')


test_string = 'HELLO? NICE TO MEET YOU'
encoded_test_string = mo_morse_string_encoder(test_string)
decoded_test_string = mo_morse_string_decoder(encoded_test_string)
print(encoded_test_string)
print(decoded_test_string)

