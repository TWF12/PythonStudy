with open("hello.txt", "w") as file:
    file.write("Hello, World!")
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)