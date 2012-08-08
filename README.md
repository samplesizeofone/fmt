fmt
===

A Jinja2 preprocessor and vim configuration for making it easier to work with Jinja and plain text formatting. 

# Requirements #
Requires Python 2.7.

# Usage #

Wrap whitespace that should not be rendered as part of the template output in [[ ]] . To insert a literal [[ or ]] use
[\[ and ]\] . To insert a literal [\[ or ]\] use [\\[ or ]\\] . This works for any number of backslashes, and will 
render any n backslashes surrounded by the same bracket as n - 1 backslashes surrounded by that bracket.

# Irritating limitations #

[[ and ]] must only enclose white space (thought that does include new lines).

# Vim configuration #

    "Highlight [[ ]] sequences
    au BufEnter *.jin :syn match ws '\(\[\[\_s\+\)\|\(\_s\+\]\]\)'
    au BufEnter *.jin :hi ws ctermbg=darkred guibg=darkred

    "Conceal [[ and ]] when the cursor is not on the containing line
    au BufEnter *.jin :syn match rws '\]\]' conceal containedin=ALL
    au BufEnter *.jin :syn match lws '\[\[[^\r]' conceal containedin=ALL

    " Highlight [[ when at the end of line
    au BufEnter *.jin :syn match endofline '\[\[$' containedin=ALL
    au BufEnter *.jin :hi endofline ctermbg=darkred guibg=darkred

    au BufEnter *.jin :set conceallevel=3
