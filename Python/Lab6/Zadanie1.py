import multiprocessing

def process_line(line):
    return line.upper()

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with multiprocessing.Pool() as pool:
        processed_lines = pool.map(process_line, lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(processed_lines)

    print("Przetwarzanie wieloprocesowe zakończone.")

if __name__ == "__main__":
    main()
