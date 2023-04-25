# def vignere_decoder(coded_message, keyword):
#     # Part 1 - Creating keyword phrase:
#     keyword_charindx = 0
#     keyword_phrase = ""
#     # Part 1a & 1b can be interswitched (doesn't matter if you work on the characters/letters in or out of the punctuation list)
#     # Part 1a - Including all punctuations in keyword phrase
#     for i in range(0, len(coded_message)):
#         if coded_message[i] in punctuation: 
#             keyword_phrase += coded_message[i] #add it as it is
#     # Part 1b - Skipping punctuations while mapping keyword phrase to coded message
#         else:
#             keyword_phrase += keyword[keyword_charindx]
#             keyword_charindx = (keyword_charindx + 1) % len(keyword)
#     # print(keyword_phrase) # just to check how it looks

#     # Part 2 - Decoding the message
#     decoded_msg = ''
#     # Part 2a - Including all punctuations in decoded message
#     for i in range(0, len(coded_message)):
#         if coded_message[i] in punctuation:
#             decoded_msg += coded_message[i]  #add it as it is
#     # Part 2b - Deducing the char index of the decoded char
#         else:
#             decoded_charindx = alphabet.find(coded_message[i]) - alphabet.find(keyword_phrase[i])
#             decoded_msg += alphabet[decoded_charindx % len(alphabet)]
            
#     return decoded_msg

# message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
# keyword = "friends"

# print(vignere_decoder(message, keyword))
# # prints "you were able to decode this? nice work! you are becoming quite the expert at crytography!"

hours = 0
minutes = 155

if minutes >= 60:
    hours = int(minutes/60)
    minutes %= 60
print('{hours}:{minutes}'.format(hours=hours, minutes=minutes))
print((8 / 2) + 4 * 8)
primos = [2, 3, 5, 7, 11, 13, 17, 19]
print(primos[3])

hola = False or True
print(hola)