grammar RachaConta;

program: title? statement* 'fechar' EOF;

title: 'evento' STRING NEWLINE;

statement: expense NEWLINE+;

//Ex: gasto 100.00 em "Cerveja" por Pedro para [Ana(2), Joao(1)]
expense: 'gasto' value 'em' description 'por' payer 'para' beneficiaries;

beneficiaries: 'todos' | list_of_people;

list_of_people: person_share (',' person_share)*;

//Nome da pessoa e opcionalmente o peso (ex: Ana ou Ana(2))
person_share: ID ('(' weight ')')?;

payer: ID;
value: NUMBER;
weight: INT;
description: STRING;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
INT: [0-9]+; 
NUMBER: [0-9]+ ('.' [0-9]+)?;
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;