# -*- coding: utf-8 -*-
"""
    Lucario Colorscheme
    ~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class LucarioStyle(Style):

    background_color = '#2b3e50'
    styles = {
        Token:              'noinherit #f8f8f2 bg:#2b3e50',
        Comment.Preproc:    'noinherit #ff6541',
        Name.Entity:        'noinherit #f8f8f2',
        Generic.Heading:    '#f8f8f2 bold',
        Generic.Emph:       'underline',
        Name.Tag:           'noinherit #ff6541',
        Name.Function:      'noinherit #72c05d',
        Generic.Traceback:  'noinherit #f8f8f0 bg:#f92672',
        Name.Variable:      'noinherit #66d9ef italic',
        Generic.Subheading: '#f8f8f2 bold',
        Generic.Output:     'noinherit #61bbc8 bg:#354758',
        Keyword:            'noinherit #ff6541',
        Generic.Inserted:   '#f8f8f2 bg:#478815 bold',
        Number.Float:       'noinherit #ca94ff',
        Keyword.Type:       'noinherit',
        Name.Constant:      'noinherit',
        String:             'noinherit #e6db74',
        Comment:            'noinherit #5c98cd',
        Name.Attribute:     'noinherit #72c05d',
        Number:             'noinherit #ca94ff',
        Name.Label:         'noinherit #e6db74',
        Generic.Deleted:    'noinherit #8c0c10',
        Operator.Word:      'noinherit #ff6541',
    }
