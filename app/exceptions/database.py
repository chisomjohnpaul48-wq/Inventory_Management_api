class UnsafeTestDatabaseError(Exception):
    """
    Raised when a test operation targets a database
    that has not been explicitly approved for testing.
    """
    pass