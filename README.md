## Terces Substitution Cipher
Encodes/Decodes a message using the Terces Substitution Cipher. Python3.  
Terces Cipher is from "The Secret Series". It is a standard substitution cipher (https://en.wikipedia.org/wiki/Substitution_cipher) where the rearranged alphabet begins with the given key (duplicate letters removed) followed by the remaining alphabet in order.  
For example, the key "terces" would give the rearranged alphabet 
```
abcdefghijklmnopqrstuvwxyz
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
tercsabdfghijklmnopquvwxyz
```

Uses an input and output file.

## Usage

<pre>
$ <b>python3 terces.py</b>
Key: <b>terces</b>
Decrypt/Encrypt?
(D/E) <b>E</b>
</pre>
<pre>
$ <b>python3 terces.py</b>
Key: <b>tErCeS</b>
Decrypt/Encrypt
(D/E) <b>D</b>
</pre>

## Installation

1. Install Python 3
2. `python3 terces.py`

## Contributing

Do as you wish, I suppose

## License

MIT