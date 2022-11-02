from backend.src.ai import squiD
from backend.src.cards import dumpling, squid_nigiri, salmon_nigiri


def test_squiD():
    assert squiD([dumpling, squid_nigiri]) == 1
    assert squiD([dumpling, salmon_nigiri]) == 0