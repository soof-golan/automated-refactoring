"""
Source:
class SomeClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

Target:
class SomeClass:
    def __init__(self, value):
        self.value = value

    async def get_value(self):
        return self.value

    async def set_value(self, value):
        self.value = value
"""
import argparse
from typing import Self

import libcst
from libcst.codemod import VisitorBasedCodemodCommand


class ConvertToAsync(VisitorBasedCodemodCommand):
    DESCRIPTION: str = "Converts a class to use async methods."

    @staticmethod
    def add_args(arg_parser: argparse.ArgumentParser) -> None:
        arg_parser.add_argument(
            "method_names",
            nargs="+",
            help="The name of the methods to convert to async.",
        )

    def __init__(self: Self, context: libcst.codemod.CodemodContext, method_names: list[str]):
        super().__init__(context)
        self.method_names = set(method_names)

    def leave_FunctionDef(
            self: Self, node: libcst.FunctionDef, updated_node: libcst.FunctionDef
    ) -> libcst.FunctionDef:
        if node.name.value in self.method_names:
            return updated_node.with_changes(
                asynchronous=libcst.Asynchronous()
            )
        return updated_node
