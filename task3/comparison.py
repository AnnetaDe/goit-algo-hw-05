from bouer_moore import boyer_moore_search
from morris_pratt import kmp_search
from raben_karp import rabin_karp_search
from my_timer import time_it


def get_file_content(path: str) -> str:
    """Read file content safely."""

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return ""


path1 = "task3/text1.txt"
path2 = "task3/text2.txt"

text1 = get_file_content(path1)
text2 = get_file_content(path2)

default_algorithms = {
    "Rabe-Karp": rabin_karp_search,
    "Knuth-Morris-Pratt": kmp_search,
    "Boyer-Moore": boyer_moore_search,
}
existing_strings = {
    "text1": "найпростіший алгоритм пошуку",
    "text2": "поставленої мети визначена",
}
none_existing_strings = {
    "text1": "маленкі зелені чоловічки сприяли відкриттю",
    "text2": "навязливі думки відволікали від важливих справ",
}


@time_it
def run_algorithm(algorithm, text, x):
    return algorithm(text, x)


def compare_algorithms(text: str, x: str, algorithms: dict = default_algorithms):
    """
    Compare the performance of different searching algorithms.
    """
    time_array = []

    for name, algorithm in algorithms.items():
        sorted_items = run_algorithm(algorithm, text, x)
        time_array.append(sorted_items[1])

        print(f"{name} Result: {sorted_items[0], 'Time: ', sorted_items[1]}")

    print(
        "\n",
        "The fastest algorithm is number: ",
        time_array.index(min(time_array)) + 1,
        " with time: ",
        min(time_array),
    )


if __name__ == "__main__":
    print("Existing strings:")
    for text in existing_strings:
        print(f"Text: {text}")
        compare_algorithms(text1, existing_strings[text])

    print("\nNone existing strings:")
    for text in none_existing_strings:
        print(f"Text: {text}")
        compare_algorithms(text1, none_existing_strings[text])
