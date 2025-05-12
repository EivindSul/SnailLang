grammar Snail;
import SnailTokens;

program
	: sep* (stat sep?)*
	;

stat
	: LOCAL_KEYWORD? ID '=' expr # assignment
	| FOR_KEYWORD range block # forrange
	| FOR_KEYWORD EACH_KEYWORD each_range IN_KEYWORD atom block # foreach
	| WHILE_KEYWORD expr block # while
	| if elif* else? # conditional
	| patternmatch # patmat
	| RETURN_KEYWORD # return
	| expr # expression
	;

// Excuse the messy newline spam!
patternmatch
	: (TYPE COLON)? expr QUESTION_MARK NEWLINE* ARROW NEWLINE* LOCAL_KEYWORD? ID NEWLINE* COLON NEWLINE*
	  patterneval (COMMA NEWLINE* patterneval)*
	  NEWLINE* COMMA* NEWLINE* PERIOD
	;

patterneval
	: (pattern NEWLINE* ARROW)? NEWLINE* expr
	;

pattern
	: ((TYPE | WILDCARD) COLON)? (expr | WILDCARD)
	;

if
	: IF_KEYWORD expr block
	;

elif
	: ELSE_KEYWORD if
	;

else
	: ELSE_KEYWORD block
	;

block
	: BLOCK_START sep* (stat sep?)* BLOCK_END sep*
	;

range
	: ID ASSIGN INT (COMMA INT)*
	;

each_range
	: ID (COMMA ID)?
	;

pair
	: ID ASSIGN expr         # namedkey
	| atom ASSIGN expr       # exprkey
	| expr                   # listitem
	;

expr
	: expr OP_ADD expr       # add
	| expr OP_SUB expr       # sub
	| expr OP_MUL expr       # mul
	| expr OP_DIV expr       # div
	| expr SOP_CONCAT expr   # concat
	| BOP_NOT expr           # not
	| expr BOP_AND expr      # and
	| expr BOP_OR expr       # or
	| expr COMP_EQ expr      # equal
	| expr COMP_NEQ expr     # notequal
	| expr COMP_GT expr      # greaterthan
	| expr COMP_GEQ expr     # greaterorequal
	| expr COMP_LT expr      # lessthan
	| expr COMP_LEQ expr     # lessorequal
	| LIST_START (pair (COMMA pair)*)? LIST_END  # table
	| ID LIST_START expr LIST_END                # tablelookup
	| LOCAL_KEYWORD? FUNCTION_KEYWORD ID? '(' param_list? ')' block # functiondeclaration
	| atom                   # atomic
	;

atom
	: ID '(' arg_list? ')'   # call
	| '(' expr ')'           # nested
	| INT                    # intliteral
	| FLOAT                  # floatliteral
	| STRING                 # stringliteral
	| BOOL                   # boolliteral
	| NIL                    # nullliteral
	| ID                     # identifier
	;

arg_list
	: expr (COMMA expr)*
	;

param_list
	: param (COMMA param)* (COMMA VARIADIC)?
	| VARIADIC
	;

param
	: ID (ASSIGN expr)?
	;

sep
	: SEMI
	| NEWLINE
	;

