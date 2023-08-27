# country = input("Enter a country: ")
#
# match country:
#     case "USA":
#         print("Hello")
#     case "India":
#         print("Namaste")
#     case "Germany":
#         print("Hallo")

# amount = input("how much?")
# rate = 2
# dollar = float(amount)
# print(dollar * rate)


# ranking = ['John', 'Sen', 'Lisa']
# user_input = int(input("Which Ranking? "))
# print(ranking[user_input - 1])

ranking = ['John', 'Sen', 'Lisa']

user_input = input("Choose an athlete: ")

if user_input in ranking:
    position = ranking.index(user_input) + 1
    print(position)