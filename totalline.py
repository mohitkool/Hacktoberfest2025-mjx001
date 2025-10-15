import os

def count_code_lines(base_dir='.'):
    total = 0
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.py'):
                with open(os.path.join(root, f), encoding='utf-8') as file:
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            total += 1
    print(f"Total lines of code (excluding comments/blanks): {total}")

if __name__ == "__main__":
    count_code_lines()
