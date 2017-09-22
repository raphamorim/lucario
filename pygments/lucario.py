# -*- coding: utf-8 -*-
"""
    Lucario Colorscheme
    ~~~~~~~~~~~~~~~~~~~

		Simon Duff <simon.duff@gmail.com>

"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String, Error, Literal, Other, Punctuation, Text

class LucarioStyle(Style):
    default_style = "#f8f8f2"
    background_color = '#2b3e50'

    styles = {
			Text: '#f8f8f2',
			Error: 'bold #ffb3b5',
			Keyword: '#ffb3b5',
			Literal: '#e6b5ff',
			Name: '#f8f8f2',
			Name.Tag: '#ffb3b5',
			Operator: '#ffb3b5',
			Punctuation: '#f8f8f2',
			Comment: '#7ce5e6',
			Keyword.Namespace: '#ffb3b5',
			Literal.String: '#d7d787',
			Name.Class: '#b3d6b3',
			Name.Function: '#b3d6b3',
			Name.Namespace: '#f8f8f2',
			Name.Builtin.Pseudo: '#84dffe'
		}
