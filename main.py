import random


def Coding():
  ran = random.Random()
  alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'x', 'y', 'z'
  ]
  englishText = input("Enter the text you want to code: ")
  text = englishText.split(" ")
  for i in range(len(text)):
    if(len(text[i]) <= 3):
      code = text[i][::-1]
      text[i] = code
    else:
      r1 = ran.choice(alphabets) + ran.choice(alphabets) + ran.choice(
        alphabets)
      r2 = ran.choice(alphabets) + ran.choice(alphabets) + ran.choice(
        alphabets)
      text[i] = text[i] + text[i][0]
      prefixremove = text[i][1:]
      text[i] = prefixremove
      text[i] = r1 + text[i] + r2

  for item in text:
    print(item, end=" ")


def Decoding_multi(Text):
  for i in range(len(Text)):
    if(len(Text[i])<=3):
      Text[i] = Text[i][::-1]
    else:
      prefixremove = Text[i][3:]
      Text[i] = prefixremove
      Text[i] = Text[i][len(Text[i]) - 4] + Text[i]
      suffixremove = Text[i][:-4]
      Text[i] = suffixremove
  for item in Text:
    print(item, end=" ")
def Decoding_one_word(Text):
  if(len(Text[0]) <= 3):
    Text[0] = Text[0][::-1]
  else:
    prefixremove = Text[0][3:]
    Text[0] = prefixremove
    Text[0] = Text[0][len(Text[0]) - 4]+Text[0]
    suffixremove = Text[0][:-4]
    Text[0]  = suffixremove
  for item in Text:
    print(item, end=" ")
choice = input("What do you want to do : a) Coding \t b) Decoding: \n")
if (choice.upper() == "A"):
  Coding()
else:
  codedText = input("Enter the coded text: ")
  Text = codedText.split(" ")
  if(len(Text) == 1):
    Decoding_one_word(Text)
  else:
    Decoding_multi(Text)
