ES6_EXT = {
    "<stmt>": JS_GRAMMAR["<stmt>"] + ["<let_const_decl>", "<class_decl>"],
    "<let_const_decl>": ["let <ident> = <expr>;", "const <ident> = <expr>;"],
    "<class_decl>": ["class <ident> {\n<class_members>\n}",
                     "class <ident> extends <ident> {\n<class_members>\n}"],
    "<class_members>": ["", "<class_member>\n<class_members>"],
    "<class_member>": ["<ident>(<params>) <func_body>",
                       "static <ident>(<params>) <func_body>",
                       "constructor(<params>) <func_body>"],
    "<primary>": JS_GRAMMAR["<primary>"] + ["<arrow_fn>", "<template>"],
    "<arrow_fn>": ["(<params>) => <expr>", "<ident> => <expr>", "(<params>) => <func_body>"],
    "<template>": ["`<tpl_chars>`", "`<tpl_chars>${<expr>}<tpl_chars>`"],
    "<tpl_chars>": ["", "<strchar><tpl_chars>"],
}
JS_GRAMMAR_ES6 = {**JS_GRAMMAR, **ES6_EXT}