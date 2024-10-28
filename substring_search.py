from string_search_algos import *
import timeit

FIRST_TEXT_FILE_NAME = 'article_algo_in_libraries.txt'
SECOND_TEXT_FILE_NAME = 'article_social_db.txt'
POSITIVE_TEST_SUBSTRING = 'кількість' # presented in both files
NEGATIVE_TEST_SUBSTRING = 'неіснуюча комбінація слов і літер' # not presented in any file


def main():
    # setup
    test_subscrings = (POSITIVE_TEST_SUBSTRING, NEGATIVE_TEST_SUBSTRING)
    file_names = (FIRST_TEXT_FILE_NAME, SECOND_TEXT_FILE_NAME)
    algorithms = [
        (kmp_search, "KMP search"),
        (boyer_moore_search, 'Boyer-Moore search'),
        (rabin_karp_search, 'Rabin-Karp search')
    ]


    # parse actual texts
    texts = [read_text_from_file(file_name) for file_name in file_names]
    
    # run test
    for text_index, text in enumerate(texts):
        print(f"Testing text {text_index + 1}....")
        for target in test_subscrings:
            print(f"Testing by substring \'{target}\'....")

            for algo, tag in algorithms:
                result = measure_time(algo, text, target)
                print(f"Result for {tag} algorithm is {result:.8f}")
            print("\n")
            
        print("\n\n")


def read_text_from_file(filename) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


# measure time for 10 runs
def measure_time(algorithm, text, pattern):
    number_of_runs = 100

    # return average search time
    return timeit.timeit(lambda: algorithm(text, pattern), number=number_of_runs) / number_of_runs


if __name__ == '__main__':
    main()