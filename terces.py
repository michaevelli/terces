from array import *
import string

def cut(seq, idfun = None):
    if idfun is None:
        def idfun(x): return x
    seen = {};result = []
    for item in seq:
        marker = idfun(item);
        if marker in seen: continue
        seen[marker] = 1; result.append(item)
    return result
def low(s):
    try: string.ascii_lowercase.index(s); return True
    except: return False
def upp(s):
    try: string.ascii_uppercase.index(s); return True
    except: return False
def encrypt():
    text = str(open('input', 'r').read()); code = ""
    for x,y in enumerate(text): code += str(betal[string.ascii_lowercase.index(text[x])]) if low(text[x]) else str(betau[string.ascii_uppercase.index(text[x])]) if upp(text[x]) else str(text[x])
    return(code)
def decrypt():
    text = str(open('input', 'r').read()); code = ""
    for x,y in enumerate(text): code += str(alpha[betal.index(text[x])]).lower() if low(text[x]) else str(alpha[betau.index(text[x])]).upper() if upp(text[x]) else str(text[x])
    return(code)

#text = str(input("pass"))
alpha = list(str(input("Key: ").lower()))
alpha.reverse()
betal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,len(alpha)):
    betal.insert(0, alpha[i])
betal = cut(betal)
betau = [x.upper() for x in betal]
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

write = "";
print("Decrypt/Encrypt?");
crypt = str(input("(D/E): "));
write = encrypt() if crypt == "E" else decrypt() if crypt == "D" else ""
file = open('output', 'w');
file.write(write);
