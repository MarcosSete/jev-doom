from typesafe_sdk import TypeSafeClient

class JevClient:
    def __enter__(self) -> "JevClient":
        self._client = TypeSafeClient()
        return self

    def __exit__(self,exc_type, exc_value, traceback) -> None:
        self._client.close()

    def system_one(self, **kwargs):
        return self._client.system_one(**kwargs)
