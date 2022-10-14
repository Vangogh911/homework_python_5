# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "абвыаыаф раз два три фывабв красный"
text_list = text.split()
edited_text_list = []
for i in range(len(text_list)):
    if "абв" not in text_list[i]:
        edited_text_list.append(text_list[i])
edited_text = ""
for word in edited_text_list:
    edited_text += word + " "
print(edited_text.strip())
