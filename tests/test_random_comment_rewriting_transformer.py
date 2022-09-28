import pytest

from pirebok.transformers.random_comment_rewriting_transformer import RandomCommentRewritingTransformer
from pirebok.transformers.transformer import Transformer


@pytest.fixture
def transformer() -> Transformer:
    return RandomCommentRewritingTransformer()


def test_mutation(transformer: Transformer) -> None:
    payload = "# <script> /**/ "

    result = transformer.transform(payload)

    assert result != payload
