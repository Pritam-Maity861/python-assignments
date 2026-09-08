class LibraryException(Exception):
    pass

class BookNotFoundError(LibraryException):
    pass

class UserNotFoundError(LibraryException):
    pass

class BookUnavailableError(LibraryException):
    pass

class BookNotIssuedError(LibraryException):
    pass

class DuplicateIDError(LibraryException):
    pass
