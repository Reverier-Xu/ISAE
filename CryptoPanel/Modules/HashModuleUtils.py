from hashlib import md5, \
    sha1, \
    sha224, \
    sha384, \
    sha512, \
    sha3_224, \
    sha3_256, \
    sha3_384, \
    sha3_512, \
    sha256
import random, string


def generate_file_md5(path, blocksize=2 ** 20):
    m = md5()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha1(path, blocksize=2 ** 20):
    m = sha1()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha224(path, blocksize=2 ** 20):
    m = sha224()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha256(path, blocksize=2 ** 20):
    m = sha256()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha384(path, blocksize=2 ** 20):
    m = sha384()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha512(path, blocksize=2 ** 20):
    m = sha512()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha3_224(path, blocksize=2 ** 20):
    m = sha3_224()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha3_256(path, blocksize=2 ** 20):
    m = sha3_256()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha3_384(path, blocksize=2 ** 20):
    m = sha3_384()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def generate_file_sha3_512(path, blocksize=2 ** 20):
    m = sha3_512()
    with open(path, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def addSalt(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length)).encode()


def generate_md5(text, salt=0):
    m = md5()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha1(text, salt=0):
    m = sha1()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha224(text, salt=0):
    m = sha224()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha256(text, salt=0):
    m = sha256()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha384(text, salt=0):
    m = sha384()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha512(text, salt=0):
    m = sha512()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha3_224(text, salt=0):
    m = sha3_224()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha3_256(text, salt=0):
    m = sha3_256()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha3_384(text, salt=0):
    m = sha3_384()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()


def generate_sha3_512(text, salt=0):
    m = sha3_512()
    text += addSalt(salt)
    m.update(text)
    return m.hexdigest()
