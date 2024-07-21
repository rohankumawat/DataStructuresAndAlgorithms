dict = {}
with open("poem.txt","r") as f:
    for line in f:
        print(line)
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n','')
            token = token.replace(',','')
            token = token.replace('.','')
            token = token.lower()
            if token in dict: # if the token is in the dictionary
                dict[token] += 1 # increment the count of the token
            else: # if the token is not in the dictionary
                dict[token] = 1 # add the token to the dictionary

print(dict)