'''
    First comment
'''

def hello():
    echap = chr(34)*3
    string = """'''
    First comment
'''

def hello():
    echap = chr(34)*3
    string = %s%s%s
    print(string%%(echap, string, echap))

if __name__ == '__main__':
    '''
        Second comment
    '''
    hello()"""
    print(string%(echap, string, echap))

if __name__ == '__main__':
    '''
        Second comment
    '''
    hello()
