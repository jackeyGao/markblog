# -*- coding: utf-8 -*-
'''
File Name: markbook/markdown.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: Fri May  1 13:51:14 2015
'''

import misaka as m
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create a custom renderer
class BleepRenderer(m.HtmlRenderer, m.SmartyPants):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                text.strip()
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

if __name__ == '__main__':
    # And use the renderer
    renderer = BleepRenderer()
    md = m.Markdown(renderer,
        extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS)
    
    print md.render("""```python
    # -*- coding:utf-8 -*-
    import os
    import sys
    ```
    
    Some Markdown text.""")
