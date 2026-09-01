def example_a_plus_mode():
    with open('exam_w+.txt', 'a') as file:

        file.seek(0)

        content = file.read
        print("Content of the file:")
        print(content)

        file.write("Appending a new line at the end.\n")

        file.seek(0)
        print("\nUpdated")

example_a_plus_mode()