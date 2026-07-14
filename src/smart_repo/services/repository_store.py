class RepositoryStore:
    """
    Temporary in-memory storage.
    Later this will be replaced by SQLite.
    """

    _repository = None

    @classmethod
    def save(cls, repository):
        cls._repository = repository

    @classmethod
    def get(cls):
        return cls._repository