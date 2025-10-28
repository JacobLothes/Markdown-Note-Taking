import markdown
import sys
import re

def main():
    print(sys.argv[1])
    if re.search(r'(\.txt$)', sys.argv[1]) and re.search(r'(\.html$)', sys.argv[2]):
        with open(sys.argv[1]) as file:
            test = file.read()
        html = markdown.markdown(test)
        with open(sys.argv[2], 'w') as file2:
            file2.write(html)
        sys.exit("Finished")
    else:
        sys.exit("Please use 'python main.py input.txt output.html'")

if __name__ == '__main__':
    main()