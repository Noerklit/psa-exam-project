# This grammar was generated using Claude. The prompt contained the language and library we want to parse
# with specifications in terms of what the grammar would be used for and with what libraries it would be used.

JS_GRAMMAR = {
    "<start>": ["<program>"],
    "<program>": ["<stmts>"],
    "<stmts>": ["<stmt>", "<stmt>\n<stmts>"],

    # ---------- Statements ----------
    "<stmt>": [
        "<var_decl>",
        "<expr_stmt>",
        "<if_stmt>",
        "<while_stmt>",
        "<do_while_stmt>",
        "<for_stmt>",
        "<for_in_stmt>",
        "<switch_stmt>",
        "<try_stmt>",
        "<func_decl>",
        "<throw_stmt>",
        "<labeled_stmt>",
        "<block>",
        ";",
    ],
    "<block>": ["{\n<stmts>\n}", "{\n}"],

    "<var_decl>": ["var <var_declarators>;"],
    "<var_declarators>": ["<var_declarator>", "<var_declarator>, <var_declarators>"],
    "<var_declarator>": ["<ident>", "<ident> = <expr>"],

    # Only forms that are always valid as a statement (avoids '{' / 'function' ambiguity)
    "<expr_stmt>": [
        "<ident> <assignop> <expr>;",
        "<member> <assignop> <expr>;",
        "<call>;",
        "<ident><incdec>;",
        "<new_expr>;",
    ],

    "<if_stmt>": [
        "if (<expr>) <block>",
        "if (<expr>) <block> else <block>",
        "if (<expr>) <block> else <if_stmt>",
    ],
    "<while_stmt>": ["while (<expr>) <loop_body>"],
    "<do_while_stmt>": ["do <loop_body> while (<expr>);"],
    "<for_stmt>": [
        "for (<for_init>; <opt_expr>; <opt_expr>) <loop_body>",
    ],
    "<for_init>": ["", "var <ident> = <expr>", "<ident> = <expr>"],
    "<opt_expr>": ["", "<expr>"],
    "<for_in_stmt>": [
        "for (var <ident> in <expr>) <loop_body>",
        "for (<ident> in <expr>) <loop_body>",
    ],
    "<loop_body>": [
        "{\n<stmts>\n}",
        "{\n<stmts>\nbreak;\n}",
        "{\n<stmts>\ncontinue;\n}",
        "{\nif (<expr>) break;\n}",
    ],
    "<labeled_stmt>": ["<label>: <for_stmt>", "<label>: <while_stmt>"],
    "<label>": ["outer", "lbl"],

    "<switch_stmt>": ["switch (<expr>) {\n<cases>\n}"],
    "<cases>": ["<case>", "<case>\n<cases>", "<case>\n<default_case>"],
    "<case>": ["case <expr>:\n<stmts>\nbreak;", "case <expr>:\n<stmts>"],
    "<default_case>": ["default:\n<stmts>"],

    "<try_stmt>": [
        "try <block> catch (<ident>) <block>",
        "try <block> finally <block>",
        "try <block> catch (<ident>) <block> finally <block>",
    ],
    "<throw_stmt>": ["throw <expr>;"],

    "<func_decl>": ["function <ident>(<params>) <func_body>"],
    "<func_body>": ["{\n<stmts>\n}", "{\n<stmts>\nreturn <expr>;\n}", "{\nreturn;\n}"],
    "<params>": ["", "<ident>", "<ident>, <params>"],

    # ---------- Expressions ----------
    "<expr>": [
        "<primary>",
        "<primary>",
        "<expr> <binop> <expr>",
        "<unop> <expr>",
        "<expr> ? <expr> : <expr>",
        "<ident> <assignop> <expr>",
        "<ident><incdec>",
        "<incdec><ident>",
        "(<expr>, <expr>)",
    ],
    "<primary>": [
        "<ident>",
        "<ident>",
        "<number>",
        "<number>",
        "<string>",
        "<regex>",
        "true", "false", "null", "this", "undefined",
        "(<expr>)",
        "<array_lit>",
        "<object_lit>",
        "<func_expr>",
        "<member>",
        "<call>",
        "<new_expr>",
    ],

    "<member>": ["<primary_nofunc>.<ident>", "<primary_nofunc>[<expr>]"],
    "<primary_nofunc>": ["<ident>", "this", "(<expr>)", "<string>", "<array_lit>"],
    "<call>": ["<ident>(<args>)", "<member>(<args>)", "(<func_expr>)(<args>)"],
    "<new_expr>": ["new <ident>(<args>)", "new <ident>"],
    "<args>": ["", "<expr>", "<expr>, <args>"],

    "<array_lit>": ["[]", "[<elements>]", "[<elements>,]", "[,<elements>]"],
    "<elements>": ["<expr>", "<expr>, <elements>"],

    "<object_lit>": ["({})", "({<props>})"],
    "<props>": ["<prop>", "<prop>, <props>"],
    "<prop>": [
        "<ident>: <expr>",
        "<string>: <expr>",
        "<number>: <expr>",
        "get <ident>() { return <expr>; }",
        "set <ident>(<ident>) { <ident> = <expr>; }",
    ],

    "<func_expr>": ["function (<params>) <func_body>", "function <ident>(<params>) <func_body>"],

    # ---------- Operators ----------
    "<binop>": [
        "+", "-", "*", "/", "%",
        "==", "!=", "===", "!==",
        "<", ">", "<=", ">=",
        "&&", "||",
        "&", "|", "^", "<<", ">>", ">>>",
        "instanceof", "in",
    ],
    "<unop>": ["-", "+", "!", "~", "typeof", "void", "delete"],
    "<assignop>": ["=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", ">>>=", "&=", "|=", "^="],
    "<incdec>": ["++", "--"],

    # ---------- Lexical ----------
    "<ident>": [
        "x", "y", "z", "i", "j", "a", "b", "foo", "bar", "obj", "arr", "fn",
        "_tmp", "$el", "<letter><idrest>",
    ],
    "<idrest>": ["", "<idchar><idrest>"],
    "<idchar>": ["<letter>", "<digit>", "_", "$"],
    "<letter>": list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    "<digit>": list("0123456789"),

    "<number>": [
        "<int>", "<int>", "<int>.<digits>", ".<digits>",
        "<int>e<exp_sign><digits>", "0x<hexdigits>", "0<octdigits>",
    ],
    "<int>": ["0", "<nonzero><digits_opt>"],
    "<nonzero>": list("123456789"),
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digits_opt>": ["", "<digits>"],
    "<exp_sign>": ["", "+", "-"],
    "<hexdigits>": ["<hexdigit>", "<hexdigit><hexdigits>"],
    "<hexdigit>": list("0123456789abcdefABCDEF"),
    "<octdigits>": ["<octdigit>", "<octdigit><octdigits>"],
    "<octdigit>": list("01234567"),

    "<string>": ['"<dq_chars>"', "'<sq_chars>'"],
    "<dq_chars>": ["", "<dq_char><dq_chars>"],
    "<sq_chars>": ["", "<sq_char><sq_chars>"],
    "<dq_char>": ["<strchar>", "'", "<escape>"],
    "<sq_char>": ["<strchar>", '"', "<escape>"],
    "<strchar>": list("abcxyzABC019 _-.,:;!?#%&*+=@^~()[]{}|/"),
    "<escape>": ["\\n", "\\t", "\\r", "\\b", "\\f", "\\v", "\\0",
                 "\\\\", "\\'", '\\"', "\\x41", "\\u0041"],

    "<regex>": ["/<re_body>/", "/<re_body>/<re_flags>"],
    "<re_body>": ["<re_atom>", "<re_atom><re_body>", "<re_atom>|<re_atom>"],
    "<re_atom>": ["a", "b", "c", ".", "\\d", "\\w", "\\s", "[a-z]", "[^0-9]",
                  "a*", "b+", "c?", "a{2,3}", "(ab)", "(?:ab)", "^", "$"],
    "<re_flags>": ["g", "i", "m", "gi", "gm", "im", "gim"],
}