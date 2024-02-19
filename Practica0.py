from base64 import b64encode, b64decode  # Importa también b64decode para la corrección.
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from hashlib import sha256

plainkey = 'RGV2ZWxvcGVyQ29kZTIhQA=='
iv = b'8\xc0-\x93\x0f\nR^\x973\x1a\xeb]\xeb\xae\x89'

def cipher(data):
    """
    Cifra los datos proporcionados utilizando el algoritmo AES en modo CBC.

    Args:
        data (str): Texto plano que se desea cifrar.

    Returns:
        bytes: Datos cifrados en formato de bytes.

    Nota:
        La clave se decodifica de base64 a bytes antes de su uso,
        y se aplica relleno a los datos para cumplir con el tamaño de bloque de AES.
    """
    # Codifica la entrada en UTF-8 y decodifica la clave de base64 a bytes correctamente.
    data_hex = data.encode('utf-8')
    key = b64decode(plainkey)  # Corregido para decodificar correctamente la clave.
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(pad(data_hex, AES.block_size))  # Usa AES.block_size para claridad.

def decipher(data):
    """
    Descifra los datos proporcionados utilizando el algoritmo AES en modo CBC.

    Args:
        data (bytes): Datos cifrados en formato de bytes.

    Returns:
        bytes: Datos descifrados, todavía en formato de bytes.

    Nota:
        La clave se decodifica de base64 a bytes antes de su uso,
        y se elimina el relleno de los datos descifrados.
    """
    # Decodifica la clave de base64 a bytes correctamente.
    key = b64decode(plainkey)  # Corregido para decodificar correctamente la clave.
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(data), AES.block_size)  # Usa AES.block_size para claridad.

def validate(passwd, hash):
    """
    Valida si el hash SHA-256 del texto cifrado de una contraseña coincide con un hash dado.

    Args:
        passwd (str): Contraseña en texto plano a validar.
        hash (str): Hash SHA-256 esperado, en formato hexadecimal.

    Returns:
        bool: True si los hashes coinciden, False en caso contrario.

    Nota:
        Se cifra primero la contraseña, luego se calcula su hash SHA-256 y se compara.
    """
    ct = cipher(passwd)
    m = sha256()
    m.update(ct)
    digest = m.hexdigest()
    return digest == hash


if __name__ == '__main__':
    name = 'Joel Miguel Maya Castrejón' #Inserte su nombre aquí.
    print(cipher(name))
