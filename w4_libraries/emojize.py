from emoji import emojize

def main():
    s = input("Input: ")
    print(emo(s))


def emo(s):
        s_parts = s.split(" ")
        result = []
        for part in s_parts:
            if ":" in part:
                 result.append(emojize(part, language="alias"))
            else:
                result.append(part)
        return f"Output: {" ".join(result)}"


main()
