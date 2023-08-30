user_action = input("Add a new member: ")

with open('members.txt', 'r') as file:
    members = file.readlines()
    file.close()

members.append(user_action + '\n')

with open('members.txt', 'w') as file:
    file.writelines(members)
    file.close()


# another way:
#
# member = input("Add a new member: ")
#
# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member + "\n")
#
# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()