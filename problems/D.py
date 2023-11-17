def main():
    stack = []
    arr = []
    d = 0
    while True:
        l = input()
        if l.startswith("//down"):
            d += 1
            stack.append(0)
        elif l.startswith("//title"):
            title = l.split(" ", 1)[1].strip()
            stack[-1] += 1
            if stack:
                section_number = ".".join(map(str, stack))
                arr.append(f"{section_number}. {title}")
            else:
                arr.append(f"1 {title}")
        elif l.startswith("//up"):
            d -= 1
            if d == 0:
                break
            if stack:
                stack.pop()
    return arr


for i in main():
    print(i)
