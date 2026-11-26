import pytest
import jsparser_sut as js

def test_var():
    ast = js.parse("var a = 1;")
    assert ast["type"] == "Program"
    assert ast["body"][0]["type"] == "VariableDeclaration"

def test_function():
    ast = js.parse("function f(x){ return x + 1; }")
    assert ast["body"][0]["type"] == "FunctionDeclaration"

def test_if_for():
    js.parse("if (a) { b(); } else { c(); } for (var i=0;i<3;i++){}")

def test_invalid():
    with pytest.raises(Exception):
        js.parse("var = ;")