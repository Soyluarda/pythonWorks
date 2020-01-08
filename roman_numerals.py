
def roman_numerals(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and values[s[i]] > values[s[i - 1]]:
            result += values[s[i]] - 2 * values[s[i - 1]]
        else:
            result += values[s[i]]
    return result)

roman_numerals('MDCLXI')
