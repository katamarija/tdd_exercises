class Day2:
    def __init__(self):
        pass

    def count_valid_passwords(self, ruleset):
        valid_count = 0
        for row in ruleset:
            for line in row:
                full_line = line.split(": ")
                rule = full_line[0]
                password = full_line[1]
                lower = int(rule.split()[0].split("-")[0])
                upper = int(rule.split()[0].split("-")[1])
                chara = rule.split()[1]
                letter_dict = {}

                for letter in password:
                    letter_dict[letter] = letter_dict.get(letter, 0) + 1

                if letter_dict.get(chara) != None:
                    if letter_dict[chara] >= lower and letter_dict[chara] <= upper:
                        valid_count += 1

        return valid_count

    def count_valid_positions(self, ruleset):
        valid_count = 0
        for row in ruleset:
            for line in row:
                full_line = line.split(": ")
                rule = full_line[0]
                password = full_line[1]
                pos1 = int(rule.split()[0].split("-")[0]) - 1
                pos2 = int(rule.split()[0].split("-")[1]) - 1
                chara = rule.split()[1]

                if password[pos1] == chara and password[pos2] != chara:
                    valid_count+= 1
                if password[pos2] == chara and password[pos1] != chara:
                    valid_count+= 1

        return valid_count
