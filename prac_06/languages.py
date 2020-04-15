from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # test printing objects
    print(ruby)
    print(python)
    print(visual_basic)

    # testing if language does have dynamic typing
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    # testing if language does not have dynamic typing
    languages = [ruby, python, visual_basic]
    print("The languages that are not dynamically typed are:")
    for language in languages:
        if not language.is_dynamic():
            print(language.name)


main()
