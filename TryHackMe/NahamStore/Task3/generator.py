from itertools import product, permutations

def load_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

names = load_file("names.txt")
envs = load_file("envs.txt")
years = load_file("years.txt")

output = set()

# Combine all lists into one big pool
all_words = [names, envs, years]

# Cartesian product
for combo in product(*all_words):
    # All order variations
    for perm in permutations(combo):
        output.add("-".join(perm))

# Write results
with open("generated.txt", "w") as f:
    for domain in sorted(output):
        f.write(domain + "\n")

print(f"[+] Generated {len(output)} unique domain variations.")

