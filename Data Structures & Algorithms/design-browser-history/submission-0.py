class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage) # current is like head

    def visit(self, url: str) -> None:
        self.current.next = None # Clear history onn visit
        new_visit = Node(url) # Create new visit Node
        new_visit.prev = self.current # Add current page as history
        self.current.next = new_visit # Attach new node to history
        self.current = new_visit # Move to new node
    
    def back(self, steps: int) -> str:
        page = self.current
        while steps > 0 and page.prev: # Move number of steps and check that .prev exists
            page = page.prev
            steps -= 1
        self.current = page # Set back page as new current
        return self.current.url

    def forward(self, steps: int) -> str:
        page = self.current
        while steps > 0 and page.next: # Move number of steps and check that .next exists
            page = page.next
            steps -= 1
        self.current = page # Set foward page as new current
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)