import os

if not os.path.exists('315-message.txt'):
    message = open('315-message.txt', 'w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made")
    message.close()
else:
    message_test = open('315-message.txt', 'r')
    content = message_test.read()
    print(content)
    message_test.close()

# if os.path.exists('315-message.txt'):
#     os.remove('315-message.txt')
#     print("Message file removed")
# else:
#     print("There was no message file to remove")
