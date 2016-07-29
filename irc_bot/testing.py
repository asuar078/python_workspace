string = ":bigby_!4931096b@gateway/web/freenode/ip.73.49.9.107 PRIVMSG ##superhiddenchannel576 :@!!@attack 192.168.1.111"

password = "@!!@"

print(password in string)

commands = string.split(password,1)[1]
print commands

words = commands.split(" ")

# for word in words:
#     print word

print words[0]
print words[1]


