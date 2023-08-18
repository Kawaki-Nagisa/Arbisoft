from WordGenerator import WordGenerator


def main():
    """
    Main function to start the typing test using the WordGenerator class.
    """
    test = WordGenerator()
    test.start_test()
    test.display_test_results()


if __name__ == "__main__":
    main()
