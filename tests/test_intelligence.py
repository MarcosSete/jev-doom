from jev_doom.intelligence.client import JevClient


def test_jev_client_is_context_manager() -> None:
    assert hasattr(JevClient, "__enter__")
    assert hasattr(JevClient, "__exit__")