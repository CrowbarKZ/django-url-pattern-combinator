# django-url-pattern-combinator

A simple tool which produces all possible url's for url-patterns looking like this
```
 (r'^prefix'
   '/(?P<p1>office|school|carpet|window|'
   '-(?P<p2>cleaning|cleans|cleaner|cleaners)'
   '(-(?P<p3>uk|usa|france))?$')
```
