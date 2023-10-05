from libcst.codemod import CodemodTest
from codemods.convert_to_async import ConvertToAsync


class TestConvertToAsync(CodemodTest):
    TRANSFORM = ConvertToAsync

    def test_convert_to_async(self):
        before = """
        class SomeClass:
            def __init__(self, value):
                self.value = value
                
            def get_value(self):
                return self.value
        """

        after = """
        class SomeClass:
            def __init__(self, value):
                self.value = value
                
            async def get_value(self):
                return self.value
        """

        self.assertCodemod(before, after, method_names=["get_value"])
