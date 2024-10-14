class PageHolder:
    def __init__(self ):
        self.pages = []
        self.current_index = 0

    def add_page(self, page , ):
        self.pages.append(page)

    def set_current_index(self, index):
        if 0 <= index < len(self.pages):
            self.current_index = index
            return self.pages[index]
        return None

    def get_current_page(self):
        return self.pages[self.current_index] if self.pages else None
