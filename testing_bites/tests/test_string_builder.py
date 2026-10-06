from golden_square.testing_bites.lib.string_builder import *

def test_str_size():
    builder = StringBuilder()
    builder.add("String")
    assert builder.size() == 6
    builder.add("s ")
    assert builder.size() == 8
    builder.add("are cool")
    assert builder.size() == 16
    builder.add("")
    assert builder.size() == 16

def test_str_output():
    builder = StringBuilder()
    builder.add("String")
    assert builder.output() == "String"
    builder.add("s ")
    assert builder.output() == "Strings "
    builder.add("are cool")
    assert builder.output() == "Strings are cool"
    builder.add("")
    assert builder.output() == "Strings are cool"