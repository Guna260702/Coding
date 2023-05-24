def compare(word1,word2):
    if sorted(word1) == sorted(word2):
        return True
    return False

def anagram(dictioanry,query):
    res=[]
    for word in query:
        count=0
        for word1 in dictioanry:
            if len(word) == len(word1):
                val = compare(word,word1)
                if val == True:
                    count+=1
        res.append(count)
    return res

dic = ['heater','abc','bac','terhea','potti']
query = ["abc","eaterh","ttipo"]
res = anagram(dic,query)
print(res)