class NotAvailable(BaseException):
    # raised when the user selects an occupied slot
    pass

if __name__ == "__main__":
    try:
        raise NotAvailable
    except NotAvailable:
        print("a")