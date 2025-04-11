class HelloWorld:
    def __init__(self):
        super(HelloWorld, self).__init__()

    def __call__(self, content=None):
        print(f"Hello World! Awesome! {content}")
