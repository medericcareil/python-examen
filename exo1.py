from src.citation import Citation

def main() -> None:
    c = Citation()
    random_citation = c.random_citation()
    str_length = len(random_citation)
    decorate_str = ''

    for i in range(str_length + 12):
        decorate_str += '='

    random_citation = '====  ' + random_citation + '  ===='
    
    print(decorate_str + '\n')
    print(random_citation + '\n')
    print(decorate_str)

if __name__ == '__main__':
    main()
