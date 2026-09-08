class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class UserNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class BookNotIssuedError(LibraryError):
    pass

class DuplicateIDError(LibraryError):
    pass
