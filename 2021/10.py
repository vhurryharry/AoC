
with open('10.in') as infile:
    input = infile.read()

lines = input.splitlines()


def syntax_score(lines):
    syntax_score = 0
    ac_scores = []

    for line in lines:
        stack = []
        syntax_score_per_line = 0

        for ch in list(line):
            if ch == '(' or ch == '[' or ch == '<' or ch == '{':
                stack.append(ch)
            else:
                last = stack.pop()

                if (ch == ')' and last != '(') or (ch == ']' and last != '[') or (ch == '>' and last != '<') or (ch == '}' and last != '{'):
                    if ch == ')':
                        syntax_score_per_line = 3
                    elif ch == ']':
                        syntax_score_per_line = 57
                    elif ch == '}':
                        syntax_score_per_line = 1197
                    else:
                        syntax_score_per_line = 25137

                    break

        syntax_score += syntax_score_per_line

        if syntax_score_per_line == 0 and len(stack) > 0:
            ac_score = 0

            for ch in reversed(stack):
                ac_score *= 5

                if ch == '(':
                    ac_score += 1
                elif ch == '[':
                    ac_score += 2
                elif ch == '{':
                    ac_score += 3
                elif ch == '<':
                    ac_score += 4

            ac_scores.append(ac_score)

    ac_scores.sort()
    mid_ac_score = ac_scores[int((len(ac_scores) - 1) / 2)]
    return syntax_score, mid_ac_score


print(syntax_score(lines))
