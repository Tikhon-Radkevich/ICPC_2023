class People:
    def __init__(self, Sur, Name):
        if Sur > Name:
            self.Sur = Sur
            self.Name = Name
        else:
            self.Sur = Name
            self.Name = Sur


def search(target, array):
    for p in array:
        if p is None:
            break
        if target.Name == p.Name and target.Sur == p.Sur:
            return True
    return False


def main():
    Factsize = int(input())
    Fact = []
    for _ in range(Factsize):
        Name, Sur = input().split()
        Fact.append(People(Name, Sur))

    Prizesize = int(input())
    Prize = []
    buffer = [None] * Prizesize

    for _ in range(Prizesize):
        Name, Sur = input().split()
        Prize.append(People(Name, Sur))

    idx = 0
    for i in range(Prizesize):
        if search(Prize[i], buffer):
            print("Laughter")
            continue
        if not search(Prize[i], Fact):
            print("Noise")
            continue
        print("Applause")
        buffer[idx] = Prize[i]
        idx += 1


if __name__ == "__main__":
    main()
