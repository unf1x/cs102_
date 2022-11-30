def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in plaintext:
        if i.isupper():
            spot = alph_upper.find(i)
            new_spot = spot + shift
            if i in alph_upper:
                ciphertext += alph_upper[new_spot]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
        else:
            spot = alph_lower.find(i)
            new_spot = spot + shift
            if i in alph_lower:
                ciphertext += alph_lower[new_spot]
            elif plaintext == '""':
                ciphertext += "''"
            else:
                ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in ciphertext:
        if i.isupper():
            spot = alph_upper.find(i)
            new_spot = spot - shift
            if i in alph_upper:
                plaintext += alph_upper[new_spot]
            elif ciphertext == '""':
                plaintext += "''"
            else:
                plaintext += i
        else:
            spot = alph_lower.find(i)
            new_spot = spot - shift
            if i in alph_lower:
                plaintext += alph_lower[new_spot]
            elif ciphertext == '""':
                plaintext += "''"
            else:
                plaintext += i
    return plaintext
