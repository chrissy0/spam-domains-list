with open("spamdomains.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = sorted(line.strip() for line in lines if line.strip())

with open("spamdomains.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
