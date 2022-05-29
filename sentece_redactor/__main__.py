from sentece_redactor import __version__
from .prac_10.row_modifier import RowModifier

redactor = RowModifier()


def main():
    print(f"Sentece Redacrot\nVersion: {__version__}\n")

    enter_sentnce = input("Enter sentences to get started:\n")
    redactor.add_sentence(enter_sentnce)

    print(
        "\n• Longest words(amount: {}) - {}\n".format(
            len(redactor.view_longest_words),
            ", ".join(redactor.view_longest_words)
            )
        )
    print(
        "• Shortest words(amount: {}) - {}\n".format(
            len(redactor.view_shortest_words),
            ", ".join(redactor.view_shortest_words)
            )
        )

    words_delete = input("Enter the words to be removed: ")
    print(
        "\nNew sentences:\n• {}".format(
            " ".join(
                redactor.delete_word(words_delete)
            )
        )
    )


if __name__ == '__main__':
    main()
