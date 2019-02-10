import re
import sys
import argparse
from logger import get_logger

logger = get_logger()

parser = argparse.ArgumentParser()
parser.add_argument('--filename', help='Enter file name with extension. '
                    'For test sample file name is: sample-input-file.txt',
                    type=str, required=True)
parser.add_argument('--topword', help='Number of top most frequent words in files', type=str, required=True)
args = parser.parse_args()

filename = args.filename
top_word_limit = int(args.topword)
logger.info("Provided arguments accepted")


def find_n_most_frequest_word(filename, top_word_limit):
    """
    :param filename: Exact full filename with extension
    :param top_word_limit: Number of top most frequent words in files
    :return: List all asked most top frequent words with occurrence
    """
    try:
        # opening file with "with open" doesn't require to close file
        with open(filename) as file:
            # Assuming the result is not case sensitive. So making all lowercase.
            text_string = file.read().lower()
            logger.debug("Accessing and reading entire file")

        # to make it more meaningful, avoiding worlds which is less than 3 or greater than 20.
        # So it will ignore i, of, too big false words, ok, etc...
        # Since we want to walk through multiple words in the document, we can use the findall function
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

        logger.debug("Each word separation in file completed")

        # Using dictionary data structure to have key as a word and value as a occurance of that word
        frequency = {}
        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        logger.debug("Dictionary is ready with word and occurrence")

        sorted_dict = sorted(
            frequency.items(), key=lambda x: x[1], reverse=True)

        logger.debug("Dictionary is sorted and ready to yield number of top most frequent words requested")

        return sorted_dict[:top_word_limit]

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except:
        e = sys.exc_info()[0]
        print(e)
    finally:
        print("Process completed.")


if __name__ == '__main__':
    logger.critical(find_n_most_frequest_word(filename, top_word_limit))


