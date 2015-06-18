# TODO: add from here: github.com/jprichardson/sublime-js-snippets
from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key,
                       Text, Integer, Mimic)
javascript = AppContext(title='javascript')
grammar = Grammar('javascript', context=(javascript))


noSpaceNoCaps = Mimic('\\no-caps-on') + Mimic('\\no-space-on')

rules = MappingRule(
    name='javascript',
    mapping={
        'smear': Text('err'),
        'function': Text('fn') + Key('tab') + noSpaceNoCaps,
    },

    extras=[
        Dictation('text', format=False),
        Integer('n', 1, 20000),
      ],
    defaults={
      'n': 1
      }
    )

grammar.add_rule(rules)
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
