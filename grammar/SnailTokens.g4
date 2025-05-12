lexer grammar SnailTokens;

FOR_KEYWORD
	: 'for'
	;

EACH_KEYWORD
	: 'each'
	;

IN_KEYWORD
	: 'in'
	;

WHILE_KEYWORD
	: 'while'
	;

IF_KEYWORD
	: 'if'
	;

ELSE_KEYWORD
	: 'else'
	;

BLOCK_START
	: '{'
	;

BLOCK_END
	: '}'
	;

LIST_START
	: '['
	;

LIST_END
	: ']'
	;

LOCAL_KEYWORD
	: 'local'
	;

FUNCTION_KEYWORD
	: 'function'
	;

VARIADIC
	: '...'
	;

RETURN_KEYWORD
	: 'return'
	;

OP_ADD
	: '+'
	;

OP_SUB
	: '-'
	;

OP_MUL
	: '*'
	;

OP_DIV
	: '/'
	;

COMP_EQ
	: '=='
	;

COMP_NEQ
	: '!='
	;

COMP_GT
	: '>'
	;

COMP_GEQ
	: '>='
	;

COMP_LT
	: '<'
	;

COMP_LEQ
	: '<='
	;

BOP_NOT
	: 'not'
	;

BOP_AND
	: 'and'
	;

BOP_OR
	: 'or'
	;

SOP_CONCAT
	: '++'
	;

ASSIGN
	: '='
	;

COMMA
	: ','
	;

SEMI
	: ';'
	;

COLON
	: ':'
	;

WILDCARD
	: '_'
	;

ARROW
	: '->'
	;

QUESTION_MARK
	: '?'
	;

PERIOD
	: '.'
	;

TYPE
	: 'int'
	| 'string'
	| 'float'
	;

NEWLINE
	: [\n\r]+
	;

FLOAT
	: [0-9]+ '.' [0-9]+
	;

INT
	: [0-9]+
	;

STRING
	: '"' (~["])* '"'
	;

BOOL
	: 'true'
	| 'false'
	;

NIL
	: 'nil'
	;

ID
	: [a-z]+
	;

COMMENT
	: '--' (~[\r\n])* NEWLINE -> skip
	;

WS
	: [ \t]+ -> skip
	;

