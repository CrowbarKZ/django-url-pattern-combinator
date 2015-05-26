# django-url-pattern-combinator

A simple tool which produces all possible url's for url-patterns looking like this
```
 (r'^prefix'
   '/(?P<p1>office|school|carpet|window|'
   '-(?P<p2>cleaning|cleans|cleaner|cleaners)'
   '(-(?P<p3>uk|usa|france))?$')
```

Output for that input is:

```
set(['prefix/school-cleans-uk', 'prefix/school-cleans-france', 'prefix/carpet-cleaners-france', 'prefix/carpet-cleaning', 'prefix/window-cleaners-usa', 'prefix/office-cleans', 'prefix/window-cleaning-uk', 'prefix/window-cleaner-france', 'prefix/window-cleans', 'prefix/school-cleaning-france', 'prefix/window-cleans-france', 'prefix/office-cleaner-usa', 'prefix/office-cleaning', 'prefix/school-cleans-usa', 'prefix/carpet-cleaning-france', 'prefix/office-cleaners-usa', 'prefix/window-cleaners-france', 'prefix/office-cleaners', 'prefix/carpet-cleaners-usa', 'prefix/school-cleaning', 'prefix/office-cleans-usa', 'prefix/office-cleaning-usa', 'prefix/carpet-cleaning-usa', 'prefix/window-cleaner', 'prefix/window-cleans-usa', 'prefix/school-cleaners-usa', 'prefix/window-cleaning-usa', 'prefix/school-cleaners-france', 'prefix/school-cleaners', 'prefix/carpet-cleaners-uk', 'prefix/window-cleaners', 'prefix/school-cleans', 'prefix/carpet-cleaners', 'prefix/window-cleaning-france', 'prefix/office-cleaning-france', 'prefix/school-cleaner-france', 'prefix/carpet-cleans-usa', 'prefix/window-cleaner-usa', 'prefix/school-cleaners-uk', 'prefix/window-cleaners-uk', 'prefix/carpet-cleaner', 'prefix/office-cleaning-uk', 'prefix/carpet-cleans', 'prefix/office-cleans-uk', 'prefix/window-cleans-uk', 'prefix/school-cleaning-uk', 'prefix/carpet-cleaner-uk', 'prefix/carpet-cleaning-uk', 'prefix/carpet-cleaner-france', 'prefix/school-cleaner-usa', 'prefix/office-cleaners-france', 'prefix/office-cleaner-uk', 'prefix/office-cleans-france', 'prefix/carpet-cleans-uk', 'prefix/office-cleaner', 'prefix/carpet-cleaner-usa', 'prefix/window-cleaning', 'prefix/office-cleaner-france', 'prefix/school-cleaner-uk', 'prefix/school-cleaning-usa', 'prefix/office-cleaners-uk', 'prefix/carpet-cleans-france', 'prefix/school-cleaner', 'prefix/window-cleaner-uk'])
```
