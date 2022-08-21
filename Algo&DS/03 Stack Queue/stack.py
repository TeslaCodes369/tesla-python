from ast import main


class stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.list:
            return
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.list)


if __name__ == '__main__':
    st = stack()

    st.push(100)
    st.push(200)
    st.push(300)
    st.push(400)
    st.push(500)

    print('size', st.size())
    print('top:', st.top())
    print('pop:', st.pop())
    print('top:', st.top())
    print('Empty', st.empty())
    print('pop:', st.pop())
    print('pop:', st.pop())
    print('pop:', st.pop())
    print('pop:', st.pop())
    print('Empty', st.empty())
    print('pop:', st.pop())
    print('Empty', st.empty())
    print('size', st.size())
