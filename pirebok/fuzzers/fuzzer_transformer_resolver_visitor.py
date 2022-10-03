from functools import reduce
from operator import iconcat
from typing import Sequence

from pirebok.fuzzers import FuzzerVisitor, GenericFuzzer, SqlFuzzer
from pirebok.transformers import GenericTransformer, SqlTransformer, Transformer


class FuzzerTransformerResolverVisitor(FuzzerVisitor):
    transformers: Sequence[Transformer]

    def visit_generic(self, fuzzer: GenericFuzzer) -> None:
        self.transformers = list(map(lambda x: x(), GenericTransformer.__subclasses__()))  # type: ignore

    def visit_sql(self, fuzzer: SqlFuzzer) -> None:
        self.transformers = reduce(
            iconcat,
            [
                list(map(lambda x: x(), SqlTransformer.__subclasses__())),  # type: ignore
                list(map(lambda x: x(), GenericTransformer.__subclasses__())),  # type: ignore
            ],
            [],
        )
