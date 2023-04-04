#DICIONÁRIO

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December",

}

#print(monthConversions["Oct"])
print(monthConversions.get("Jan", "Not a valid key")) # NOT A VALID KEY PERMITE EFETUAR UM AVISO
print(monthConversions.get("Der", "Not a valid key"))
print(monthConversions.get("Mar", "Not a valid key"))
print(monthConversions.get("Apr", "Not a valid key"))
print(monthConversions.get("Nai", "Not a valid key"))

print(monthConversions.get(7, "Not a valid key")) # NOT A VALID KEY PERMITE EFETUAR UM AVISO
print(monthConversions.get(12, "Not a valid key"))
print(monthConversions.get(4, "Not a valid key"))
print(monthConversions.get(55, "Not a valid key"))
print(monthConversions.get(10, "Not a valid key"))