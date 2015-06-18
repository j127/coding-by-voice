# Originally borrowed from github.com/simianhacker/code-by-voice/
from dragonfly import (Grammar, MappingRule, Key, Mimic)


rules = MappingRule(
    name='general',
    mapping={
        'slap': Key('enter'),
        'max when': Key('w-up'),
        'left when': Key('w-left'),
        'right when': Key('w-right'),
        'min win': Key('w-down'),
        'code mode': Mimic('\\no-caps-on') + Mimic('\\no-space-on'),
    }
)

grammar = Grammar('general')
grammar.add_rule(rules)
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
