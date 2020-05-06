def generate_parenthesis_v1(n):
    def add_pair(res, s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return
        if right > 0:
            add_pair(res, s + ")", left, right - 1)
        if left > 0:
            add_pair(res, s + "(", left - 1, right + 1)

    res = []
    add_pair(res, "", n, 0)
    return res


def test_generate_parenthesis():
    print(generate_parenthesis_v1(3))
