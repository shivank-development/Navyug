morse_word = {
    'A': '._',   'B': '_...',  'C': '_._.',  'D': '_..',  'E': '.',     'F': '.._.',  'G': '__.',   'H': '....',  'I': '..',    'J': '.___',  'K': '_._',   'L': '._..',  'M': '__',    'N': '_.',    'O': '___',   'P': '.__.',  'Q': '__._',  'R': '._.',   'S': '...',   'T': '_',  'U': '.._',   'V': '..._',  'W': '.__',   'X': '_.._',  'Y': '_.__',  'Z': '__..'
}
encrypt_Msg = input().strip()
results = []
def encrypt(a, current):
    if a == len(encrypt_Msg):
        results.append(current)
        return
    for word, code in morse_word.items():
        if encrypt_Msg.startswith(code, a):
           encrypt(a + len(code), current + word)
encrypt(0, "")
for word in sorted(results):
    print(word)