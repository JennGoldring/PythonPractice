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
#
# ranking = ['John', 'Sen', 'Lisa']
#
# user_input = input("Choose an athlete: ")
#
# if user_input in ranking:
#     position = ranking.index(user_input) + 1
#     print(position)

# filenames = ['document', 'report', 'presentation']
# #
# for index, item in enumerate(filenames):
#     row = f"{index}-{item.capitalize()}.txt"
#     print(row)

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     if total_value == 0:
#         exit("Your total value cannot be zero.")
#
#     percent = value / total_value * 100
#     print(f"That is {percent}%")
#
# except ValueError:
#     print("You need to enter a number. Run the program again.")

# colors = [11, 34, 98, 43, 45, 54, 54]
#
# for color in colors:
#     if color > 50:
#         print(color)

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    both = f"Max: {maximum}, Min: {minimum}"
    return both


print(get_max())
