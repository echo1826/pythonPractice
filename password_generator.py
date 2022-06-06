def userPrompts():
    obj = {}
    pw_length = int(input(
        "How long would you like your password (must be between 8 and 128 characters?\n"))
    if pw_length < 8 or pw_length > 128:
        while pw_length < 8 or pw_length > 128:
            pw_length = int(input(
                "How long would you like your password (must be between 8 and 128 characters?\n"))
    obj['length'] = pw_length
    upper = input(
        "Would you like uppercase characters in your password (Y/N)?\n")
    if upper != 'Y' and upper != 'N':
        while upper != 'Y' and upper != 'N':
            upper = input(
                "Would you like uppercase characters in your password (Y/N)?\n")
    if upper == 'Y':
        upper_boolean = True

    else:
        upper_boolean = False

    obj['uppercase'] = upper_boolean
    lower = input(
        "Would you like lowercase characters in your password (Y/N)?\n")
    if lower != 'Y' and lower != 'N':
        while lower != 'Y' and lower != 'N':
            lower = input(
                "Would you like lowercase characters in your password (Y/N)?\n")

    if lower == 'Y':
        lower_boolean = True

    else:
        lower_boolean = False

    obj['lowercase'] = lower_boolean
    special = input(
        "Would you like special characters in your password (Y/N)?\n")
    if special != 'Y' and special != 'N':
        while special != 'Y' and special != 'N':
            special = input(
                "Would you like special characters in your password (Y/N)?\n")

    if special == 'Y':
        special_boolean = True

    else:
        special_boolean = False

    obj['special'] = special_boolean
    if obj['uppercase'] == False and obj['lowercase'] == False and obj['special'] == False:
        print("You must answer Y to at least one criteria!")
        obj = userPrompts()
    return obj


def main():
    answers = userPrompts()
    print(answers)


main()
