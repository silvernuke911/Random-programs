# file_path = r"C:\Users\verci\Downloads\words.txt"
file_path = 'words_alpha.txt'
with open(file_path, 'r') as file: 
    lines = file.readlines() 
    words= [line.strip() for line in lines]
import re
badletters=list('kmqvwxzKMQVWXZ')
numberletters=list('acdfhjkmnpqrtuvwxyACDFHJKMNPQRTUVWXYZ')

def has_badletters(testword):
    x=0
    for char in badletters:
        if char in testword:
            x+=1
    if x==0:
        return False
    else:
        return True

def not_only_numberletters(testword):
    x=0
    for char in numberletters:
        if char in testword:
            x+=1
    if x==0:
        return False
    else:
        return True


longest_acceptable_word=""
for testword in words:
    if len(testword)<=len(longest_acceptable_word):
        continue
    if has_badletters(testword):
        continue
    longest_acceptable_word=testword
print(longest_acceptable_word)
print(len(longest_acceptable_word))

longest_acceptable_number_word=""
for testword in words:
    if len(testword)<=len(longest_acceptable_number_word):
        continue
    if not_only_numberletters(testword):
        continue
    longest_acceptable_number_word=testword
print(longest_acceptable_number_word)
print(len(longest_acceptable_number_word))


file = open ('5words_norepeats.txt', 'w')

def check_repeat_letters(input_string):
    seen_letters = set()
    for char in input_string:
        if char in seen_letters:
            return True
        seen_letters.add(char)
    return False
    
for word in words:
    if len(word)==5:
        if check_repeat_letters(word)==False:
            file.write(word+'\n')
file.close()

# allowedwords=""
# allowedwordslist=[]
# for testword in words:
#     if lettertest(testword)==1:
#         continue
#     allowedwords=testword
#     allowedwordslist.append(allowedwords)
# print(len(allowedwordslist))


# longestword=""
# for testword in words:
#     if len(testword)<=len(longestword):
#         continue
#     longestword=testword
#     print(longestword)

# def lettertest(testword,letterlist):
#     x=0
#     for char in letterlist:
#         if charpresent(testword,char)==1:
#             x+=1
#     if x==0:
#         return 0
#     else:
#         return 1

#def numbertest.

    #     if char not in testword:
    #         x+=1
    # print(x)
    # if x==0:
    #     return True
    # else:
    #     return False 

