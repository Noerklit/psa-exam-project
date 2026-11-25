import string
from fuzzingbook.Grammars import srange, is_valid_grammar
from fuzzingbook.GrammarFuzzer import GrammarFuzzer

TOML_GRAMMAR = {
    "<start>": ["<toml>"],

    # --- Dokument ---
    "<toml>": ["<keyvals>", "<keyvals>\n<sections>"],
    "<keyvals>": ["", "<keyval>\n<keyvals>", "<comment>\n<keyvals>"],
    "<sections>": ["<section>", "<section>\n<sections>"],
    "<section>": ["<table-header>\n<keyvals>", "<array-table-header>\n<keyvals>"],
    "<table-header>": ["[<key>]"],
    "<array-table-header>": ["[[<key>]]"],
    "<comment>": ["# <comment-chars>"],
    "<comment-chars>": ["", "<comment-char><comment-chars>"],
    "<comment-char>": srange(string.ascii_letters + string.digits + " _-"),

    # --- Nøgler ---
    "<keyval>": ["<key> = <value>", "<key> = <value> <comment>"],
    "<key>": ["<simple-key>", "<simple-key>.<key>"],
    "<simple-key>": ["<bare-key>", "<basic-string>", "<literal-string>"],
    # lille pulje af nøgler => større chance for interessante kollisioner
    "<bare-key>": ["a", "b", "name", "version", "<bare-char><bare-chars>"],
    "<bare-chars>": ["", "<bare-char><bare-chars>"],
    "<bare-char>": srange(string.ascii_letters + string.digits + "_-"),

    # --- Værdier ---
    "<value>": ["<string>", "<integer>", "<float>", "<boolean>",
                "<datetime>", "<array>", "<inline-table>"],

    # Strings
    "<string>": ["<basic-string>", "<literal-string>",
                 "<ml-basic-string>", "<ml-literal-string>"],
    "<basic-string>": ['"<basic-chars>"'],
    "<basic-chars>": ["", "<basic-char><basic-chars>"],
    "<basic-char>": srange(string.ascii_letters + string.digits + " ")
                    + ["\\n", "\\t", "\\\\", '\\"', "\\u00E9", "\\U0001F600"],
    "<literal-string>": ["'<literal-chars>'"],
    "<literal-chars>": ["", "<literal-char><literal-chars>"],
    "<literal-char>": srange(string.ascii_letters + string.digits + " \\"),
    "<ml-basic-string>": ['"""<basic-chars>\n<basic-chars>"""'],
    "<ml-literal-string>": ["'''<literal-chars>\n<literal-chars>'''"],

    # Integers
    "<integer>": ["<dec-int>", "<hex-int>", "<oct-int>", "<bin-int>"],
    "<dec-int>": ["0", "<sign><nonzero><digits>", "<nonzero><digits>",
                  "1_000", "<sign>0"],
    "<hex-int>": ["0x<hexdigit><hexdigits>"],
    "<oct-int>": ["0o<octdigit><octdigits>"],
    "<bin-int>": ["0b<bindigit><bindigits>"],
    "<sign>": ["+", "-"],
    "<digits>": ["", "<digit><digits>"],
    "<digits1>": ["<digit>", "<digit><digits1>"],
    "<hexdigits>": ["", "<hexdigit><hexdigits>"],
    "<octdigits>": ["", "<octdigit><octdigits>"],
    "<bindigits>": ["", "<bindigit><bindigits>"],
    "<digit>": srange(string.digits),
    "<nonzero>": srange("123456789"),
    "<hexdigit>": srange(string.hexdigits),
    "<octdigit>": srange("01234567"),
    "<bindigit>": ["0", "1"],

    # Floats
    "<float>": ["<dec-int>.<digits1>", "<dec-int>e<dec-int>",
                "<dec-int>.<digits1>E<dec-int>",
                "inf", "+inf", "-inf", "nan", "+nan", "-nan"],

    # Bool
    "<boolean>": ["true", "false"],

    # Datetime
    "<datetime>": ["<offset-dt>", "<local-dt>", "<local-date>", "<local-time>"],
    "<offset-dt>": ["<local-date>T<local-time>Z",
                    "<local-date>T<local-time>+<hh>:<mm>",
                    "<local-date> <local-time>-<hh>:<mm>"],
    "<local-dt>": ["<local-date>T<local-time>"],
    "<local-date>": ["<yyyy>-<month>-<day>"],
    "<local-time>": ["<hh>:<mm>:<ss>", "<hh>:<mm>:<ss>.<digits1>"],
    "<yyyy>": ["<digit><digit><digit><digit>"],
    "<month>": ["01", "02", "06", "12"],
    "<day>": ["01", "15", "28", "29", "31"],
    "<hh>": ["00", "07", "12", "23"],
    "<mm>": ["00", "30", "59"],
    "<ss>": ["00", "30", "59", "60"],

    # Arrays og inline tables (rekursive!)
    "<array>": ["[]", "[<array-values>]", "[<array-values>,]",
                "[\n<array-values>,\n]"],
    "<array-values>": ["<value>", "<value>, <array-values>"],
    "<inline-table>": ["{}", "{ <inline-keyvals> }"],
    "<inline-keyvals>": ["<key> = <value>", "<key> = <value>, <inline-keyvals>"],
}

assert is_valid_grammar(TOML_GRAMMAR)