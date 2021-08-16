def try_me(name):
    '''Evaluates wheter your name is cool using complex ML algorithms'''

    if name.lower() == "philipp":
        return "Great name! You passed the test"

    return "Too bad, apparently your name is not cool enough. You should consider changing it."


if __name__ == "__main__":
    name = "Philipp"
    check = try_me(name)
    print(check)
