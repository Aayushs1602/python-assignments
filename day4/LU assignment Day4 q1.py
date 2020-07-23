string = "what we think we become; we are python programmers"
substring = "we"
list_string = string.split(" ")

for i in range(len(list_string)):
    if substring == list_string[i]:
        print("found substring at index ", i+1)

