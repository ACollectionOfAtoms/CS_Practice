class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_to_stack(self, item):
        self.items.append(item)

    def remove_from_stack(self):
        self.items.pop()

    def peak(self):
        return self.items[-1]


class VerifyHTML(Stack):
    def __init__(self):
        super(VerifyHTML, self).__init__()
        self.EXCEPTIONS = ['br', 'meta']

    def get_tags(self):
        f = open('./htmlfile.html', 'r')
        tag = ''
        while True:
            ch = f.read(1)
            if not ch:
                break
            tag += ch
            if tag[0] != '<':
                tag = ''
            elif tag != '' and tag[1:] in self.EXCEPTIONS:
                print 'Tag is ' + tag + ' does not need to match: stack is now ' + str(self.items)
                tag = ''
            elif tag != '' and tag[0] == '<' and tag[-1] == '>':
                tag_name = tag[1:-1]
                tag = ''
                if tag_name[0] != '/':
                    self.add_to_stack(tag_name)
                    print "Tag is " + tag_name + " :pushed: " + "stack is now " + str(self.items)
                elif tag_name[1:] == self.peak():
                    self.remove_from_stack()
                    print "Tag is " + tag_name + " :matches: " + "stack is now " + str(self.items)
                else:
                    print "Error: tag is " + tag_name + " but top of stack is " + str(self.peak())
                    break

    def verify(self):
        self.get_tags()


fun = VerifyHTML()
fun.verify()
