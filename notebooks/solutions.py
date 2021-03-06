import base64
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import imp
import random


solution_list_comprehensions = """
J+g88N8BH49B8AZAbuAhsngoS73D0IIXs+Hckk2430mdNS7gRaA3vRYcO71g8O0c2b8HVJdmRMQR
r0DVdOiOH3xn3aT241KX+hP3WSgAIFQ="""

solution_pca_1 = """
8rNeczFb0AxSRfSp7/7wDbcVWVamC7izGoQzHazFeOpQUGrQ42Pmt9QQDlaGXc6pEgapZED28diU
u6yNN/imzHPgHVd/x8Laz1eiL5gg+RHqBpceHmWHXtSPIeat05NnIfgbSGwQACDMqgsaDsqeIdt7
hytkLj8lpi1JdyCQROw="""

solution_pca_2 = """
sCUN6R//yookpAse5W5op95YzL+2mel1xfGltaiyTaVfm5BvgiI9VwElPoEttfgl1mXdIfmW0wpA
j+ts6VZAbjH6yP8AcIsFHk94eRlQ8hg="""

solution_pca_3 = """
bhPGfG3FqRAuKyGlgYAEYReNgMt+MRpHwgCSFi44yZ3y0lXxMZSJhKXEBqHDJlOZxWmOA6D+VnvT
CJayNjn6lh8lFNc1Tci1oaWGB1Vaok1cKsRva2nvlFN02iW/f2D2XQVIgicvbB8WAkdaOYjLOzEY
UM+LvKuhc876U4ewJLM="""

solution_pca_4 = """
32zque8D60ZH8w3udsfOJ1bVA3uSvLpAH3RVpTFG7d4DMlsShOP7oeUMJpG3dpb34d8mPLKi9YIy
ngQDyq/PPf8RD1yHsKev+icFDb5Q+IzE4Z08aJx8iHAH0tl1FIEAJaZghB+x3hoBVIOiA+7Fa9JA
H43k/1Qi1l//u3fC63eOQtaSVnxzKiKWEUdD7eXDCmp0eZ2zlRVgex0hgAttR21emC3bC0u3ViwF
m4Jy1aI="""

solution_pca_5 = """
9+sLOGyr8z2+jUP6AmujQ/ibm1B+Dkjo9kuxbBCjuY07Jfbkqa0PWxj/SnkIIRaVEvDrJIDyOaYw
9SA5tXsflZuiIasnIN3aRdQMAiq4/JfHueE6LRNNOWNU1pj/sUQ+"""

solution_pca_6 = """
YAgePaUxKQvm0uxff4OwBu4Fk+8AnrbWA0auLHXuE50uYm/KX1L/5XqikYr4wY3gIJPdbj7k8V6k
LNdpmGk2IV8+06WWMmynVHkYjCpajWJ6WpknkyFziiLa0gkS/W84RNadVCmemKxslo8mbMRwz+ns
MeCaz7l6k0kef+CU/5fQFOGs7kk6h+eal1+/MvjTYgSGRGn/AV7RlgDI+UB71Osve39p0mvDYI0d
TbXHsiivOr/+KqokvIrE2CXo9rS1tghzmNoCd6ckur/tlY/mzBu4sfJqXzdKSK96fNwubEShf65h
AUXKAc3Q/3S4jdYqL6H9MVQaYzKrnlQibyvPZ+KEf4qXT4BsdW6eL6O268oYQZ4oxIxVyWhNilbY
OhVfAFM5kr3YLcDPQte1kcDP0za2d5jlGYgEzB6wa5+Upys="""

solution_profiling = """
j2DubDEekoKegD/g4oSsAwXbHzHopkNGxOMSmOk9Q2tL6BS0kdLRrSoomA5JnnLI+9QYyaLEJ3dA
z6P7EPeipk/CnavEWZV8QvUdEu0SDUs2rG6/1ZhOxZ+yz6kZiOjz8ciREgFbVw95Oek/GGlNjCyi
9Ojo3CxyWkGGtc7o8oDgJqE3J6EDlhuyxIdQEuUuyHMYZBTJS473NXkQ736+H59cj85LbTU5DoZ2
A/0kacLMz/HFcgv/xVL/h4idXuh8ifFsaESLAp0pNKi4kMuOrfk/6oyN3FIwMCxMfdyu9wqcvCmp
3OpntET94GHYvQz6tF6Ulq5p4GP8uq8V2QseXWEnS4ZgxUTlaEslwausxN2KNtIUQtTlF3XnqLNt
85BByqcy0TBv9g1bM74L5wi7FNaV2wt7LqCPjY6t9p1vJLeLI8z2vwb91NCWVp6GoT+ClKtedRro
MhzAN0yinQVWbwzKVC+fo8NLHfIb0Nd8K8NS8OLCkNEEVljgeehUTHHc8edct+c5r/CS+zstt0HJ
taYoTM2/PADOneQhmQ+BtuxpYb6HcW30XcnpFlbl5WftTIEiBWYAgM6bmjHUBaGR6FHjYSIiDF7e
P+Zv8jMOCpnovZBeyonA52VSG3M1sDTNovZrlIKwnouRuGJbw0ofjX86hfzO1pxAX2gQKR6pO6HV
7fMC/2J+GJcS76KfuS/90lswvx30HX9rLE1RJ0OWP4zoYpaW3amQQtkcUKkX2IubtdiMSytgAsgm
nyB5aG4Ah/lGRDHvzusimXbIlTGsB2tbAgeGO7I19ejuW2TIM3BK3QueAspbGxqrBr1gKNerngMP
LFir+N6CxYPIosppfAsGkjBTqGChCmxQUD4TvjQ="""

solution_regression_1 = """
Emqqe2H1sGEAbn9lQ/HeC61m2TLnfTVHx6E/3SQmFcoMxDDkEkS7CgonD5Rmw2/giYxBoRJTOYei
nW4tFPmKEYKc3L84SAMV4AUqM+YR4qeY92/WWFuHtpS84dmFLuaUk4nBaphgWghz6IkfOx9V/jgs
2mOfNujXWhH0dJzRU8V3+PTtIvqGdKzTgcXFW28aqPT5I23UiP3JPeiofFHKLoWeWVFh/DA5aOMX
+bIJFqVdWHKcZnA3kDJJ4PQQM+muOQ1fME+gvsHuK/2vjeH0wAxk/8fYyqoWiv1W6bCP63inobmx
E+XYCVf2zp3QMr+SJTb8mOAj84xIOp8+tz7FGA=="""

solution_regression_2 = """
Emqqe2H1sGEAbn9lQ/HeC61m2TLnfTVHx6E/3SQmFcoMxDDkEkS7CgonD5Rmw2/giYxBoRJTOYei
nW4tFPmKEYKc3L84SAMV4AUqM+YR4qeY92/WWFuHtpS84dmFLuaUk4nBaphgWghz6IkfOx9V/jgs
2mOfNujXWhH0dJzRU8V3+PTtIvqGdKzTgcXFW28aqPT5I23UiP3JPeiofFHKLoWeWVFh/DA5aOMX
+bIJFqUsird2l9vOXC/alvzxZHwaCZhaLtGIhMca26uKCV6XV0CsY6q8O9CtYkuyL9ptYrGIT5oG
eVKUW9ujsSEmWERK3QKg/ewUFSJnDxhpXHOuU75lROF5cyBQ/EZgjZXD2qsrYZSd5s6fThKrVFA4
l0O2zy0R7OCJk8wnbVqZFy3F75DaHL7nJYUa0ox8lF1VXkb5D451ytikG6pyYif64Tps"""

solution_regression_3 = """
Emqqe2H1sGEAbn9lQ/HeC61m2TLnfTVHx6E/3SQmFcoMxDDkEkS7CgonD5Rmw2/giYxBoRJTOYei
nW4tFPmKEYKc3L84SAMV4AUqM+YR4qeY92/WWFuHtpS84dmFLuaUk4nBaphgWghz6IkfOx9V/jgs
2mOfNujXWhH0dJzRU8V3+PTtIvqGdKzTgcXFW28an+Ndmm8TwZyyVxcJT84pAiQYjoInqYlY625P
YOIF7yw1Nzjb95Ltwngqlmqy6w7QoOvFiHJS/J+w2cfj27hyZEZ64t47yrkjUTKNjFSR/NmTWc0c
zZJDfVHZvNn3JIqrZMmWaUoT1oUX5E8mlQImMaCJCSYymNZ4I9RW8jZ06NP1ckOmHSnwCK0yLALk
xqf/Mxy76xrBD0Z0Y18WWJRUww3nH3o1W096u87IZYkKYK/CJHU1rx/XXKJZIkFu4qDYu2hmcyl0
JpdKOX4VsT6DB1Wrmg2mp54NGUUTpOiUSN2g1c6XbkXH5+hR+zUMcbbZBGNfSdfzu+ADcvEXMW/1
F2WdX4F0cqmhvfq2YBwGe6o="""

solution_regression_4 = """
Emqqe2H1sGEAbn9lQ/HeC61m2TLnfTVHx6E/3SQmFcoMxDDkEkS7CgonD5Rmw2/giYxBoRJTOYei
nW4tFPmKEYKc3L84SAMV4AUqM+YR4qeY92/WWFuHtpS84dmFLuaUk4nBaphgWghz6IkfOx9V/jtF
DHVIMhA+U7cJoFEquANG8T7nTtaH0B1bC3pHOMI7YJyC3JpTS7qvh9KdM+ZtBTc1wGTANmFj3X8q
yK3jWoWLgLAEjYeiKzDsFY41u0zS+KLKMkni85oqwyrbtb/OYWAx7309HsGbveUKG2ei47LYCt1l
tc8rWnRItz5XOHsaHlqLtzAoco/eGK2nr0KMAiyKt3aX285cL9qW/PFkfBoJmFou0YiExxrbq4oJ
XpdXQKxjqrw70K1iS7Iv2m1isYhPmgZ5UpRb26OxISZYRErdAqD97BQVImcPGGlcc65T6VDdUqd4
beB7YNILM9fbJik2f4rB5qeoqHZghtl0hWXPDxmJjxt6u46w2fhXJ1tWI6xT0lkdBXVADNNAXGUT
VBCRYW0xEmx7wcsFAN7tepe/P0ihincfgt7oC+q32KVEjwjLl3GtOBRG7GL2X8E9og=="""

solution_regression_5 = """
Emqqe2H1sGEAbn9lQ/HeC61m2TLnfTVHx6E/3SQmFcoMxDDkEkS7CgonD5Rmw2/giYxBoRJTOYei
nW4tFPmKEYKc3L84SAMV4AUqM+YR4qeY92/WWFuHtpS84dmFLuaUk4nBaphgWghz6IkfOx9V/txj
+hpwMOARshbHnDuMnETiXMZpEJRdQS99SikZmW7e3i21MAuh+MJWfnkJZTClb60SmmJoWSTbMQTu
jO+8xcPn3nI1MGIBYLNw8129fZPQFhmWDZxgA2Dg4kSXcENtSqes3a+usRzXRCXdp3d2QblkkMmW
7hcxrvCRNtVscpx9ektWLIUTPSuG7Y25e8djjGVcgbkg2mCVdmhGQVlPo0xXoOEc94Ii/QCXdLcR
fGxsbkBlKxpc6w8xf+nEw1vosw=="""
    

def _pad16(s):
    """Pad the string with spaces until its length is a multiple of 16.
    It is used before encoding a string with AES.
    """
    l = 16 - len(s) % 16
    if l < 16:
        s = s + ''.join([' '] * l)
    return s


def _generate_passphrase():
    """
    Generates a random password.
    """
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    letters = ''.join(random.choice(consonants + consonants.upper()) + random.choice(vowels + vowels.upper()) for _ in range(2))
    digits = '%04d' % random.randint(0, 9999)
    return letters + digits


def _highlight_source(src):
    """
    When packages 'pygments' is installed, the given source is formatted as
    Python source and colors are formatted for console output.
    """
    try:
        imp.find_module('pygments')
        from pygments import highlight
        from pygments.lexers.python import NumPyLexer
        from pygments.formatters.terminal import TerminalFormatter
        src = highlight(src, NumPyLexer(), TerminalFormatter(encoding='guess'))
    except ImportError:
        pass
    return src
    
    
def encrypt_solution(src, passphrase=None):
    """Prints an encrypted and base64-coded string.
    If no passphrase is given, a new one is generated."""
    if passphrase is None:
        passphrase = _generate_passphrase()
    src = 'OK!' + src
    src = _pad16(src)
    key_hash = MD5.new(passphrase).hexdigest()
    aes = AES.new(key_hash)
    encrypted_src = aes.encrypt(src)
    encrypted_src = base64.encodestring(encrypted_src)
    print encrypted_src
    print 'passphrase: ', passphrase


def decrypt_solution(encrypted_src, passphrase):
    """Takes the passphrase and encrypted source generated by encrypt_solution and
    prints the decrypted source."""
    key_hash = MD5.new(passphrase).hexdigest()
    aes = AES.new(key_hash)
    src = base64.decodestring(encrypted_src)
    src = aes.decrypt(src)
    if src[:3] == 'OK!':
        #print _highlight_source(src[3:])
        print src[3:]
    else:
        print '[wrong passphrase]' 


if __name__ == '__main__':
    encrypt_solution(src='import numpy as np', passphrase=None)
    #decrypt_solution(encrypted_src='44zzPpwOIYW7zo1CHsaM+YSI5u1Xercq5yw+3XUM5Q8=', passphrase='boZE3027')
