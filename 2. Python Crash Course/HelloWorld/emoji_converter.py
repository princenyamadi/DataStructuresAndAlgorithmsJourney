def emoji_converter(message):
    words = message.split(' ')

    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😄",
        ":P": "😛",
        ":O": "😮",
        ":|": "😐",
        ";)": "😉",
        ":*": "😘",
        ":@": "😠",
        ":$": "😳",
        ":^)": "😎",
        ":3": "😜",
        ":>": "😈",
        ":<": "😈",
        ":?": "😕",
        ":!": "😱",
        ":L": "😡",
        ":@": "😠",
        ":S": "😈",
        ":X": "😈",



    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)
    return output


message = input(">")
emoji_converter(message)

# for word in words:
#     output = ""
#     for letter in word:
#         output += emojis.get(letter, letter) + " "
#     print(output)
