class present_of_elements_in_amount:
    """ An expectation for checking that that there is a given amount of elements
    present on a web page.
    :Args:
    locator - used to find the elements
    number - an amount of elements
    returns list of WebElements once they are located
    """
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els
        else:
            return False
