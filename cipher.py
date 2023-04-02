#encoding user passwords

def encrypt(inputText, N, D):
    rev = inputText[::-1]
    listString = list(rev)
    for i in range(len(rev)):
        char = ord(rev[i])
        for j in range(N):
            if D == 1:
                if char == 126:
                    char = 34
                else:
                    char += 1
            elif D == -1:
                if char == 34:
                    char = 126
                else:
                    char -= 1
            listString[i] = chr(char)
    finalString = "".join(listString)
    return finalString


def decrypt(inputText, N, D):
    rev = inputText[::-1]
    listString = list(rev)
    for i in range(len(rev)):
        char = ord(rev[i])
        for j in range(N):
            if D == 1:
                if char == 34:
                    char = 126
                else:
                    char -= 1
            elif D == -1:
                if char == 126:
                    char = 34
                else:
                    char += 1
            listString[i] = chr(char)
    finalString = "".join(listString)
    return finalString


