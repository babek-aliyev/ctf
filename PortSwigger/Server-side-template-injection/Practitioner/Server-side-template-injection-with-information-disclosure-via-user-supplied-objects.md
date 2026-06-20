# [Server-side template injection with information disclosure via Django's debug context dump] — [PortSwigger] — [Practitioner]
**Date:** 2026-06-20

---

## Vulnerability / core concept
Server-side Template Injection

## What made me stuck
This lab was not hard to solve by using good research through internet and AI.

## What unblocked me
`null`

---
## Attack path
1) During inspection, I found an injectable parameter that reflects into a server-rendered template. I started by testing with `alert(1)` as the value. This produced a Python traceback that revealed the file paths `django/template/base.py` and the exception class `django.template.exceptions.TemplateSyntaxError`, confirming the backend uses the **Django Template Language (DTL)**, running on **Python 2.7**.
2) Since DTL only permits variable lookups, attribute/dict/index access, and filters (no arbitrary function calls), I tested whether tag syntax (`{% %}`) was reachable in addition to variable syntax (`{{ }}`). I first confirmed block tags parse at all with a basic conditional, then tried `{% load admin_tags %}`. This produced an error stating `'admin_tags' is not a registered tag library. Must be one of: cache i18n l10n static tz` — a positive signal that `{% load %}` itself executes and that this list represents the full set of registered tag libraries.
3) With tag execution confirmed, I tried the built-in `{% debug %}` tag, which dumped the full template context (including a `product` dict and a `settings` object) and the interpreter's entire loaded module list — confirming `subprocess` and `os` were importable in-process, and that `settings` was a reachable context variable.
4) I then tried to walk the Python object graph from a context variable to reach a dangerous callable, using the classic `__class__.__mro__.__subclasses__` technique (e.g. `{{ product.name.__class__ }}`). This consistently failed with `Variables and attributes may not begin with underscores`, revealing that Django's `Variable` resolver has a hardcoded check rejecting any dotted segment starting with `_`. This is a deliberate, version-independent sandboxing measure in Django — it rules out the entire dunder-walking/RCE path in DTL.
5) With RCE via object-graph traversal ruled out, I pivoted to the `settings` object exposed in the context, since attribute access on it doesn't require underscores. I requested `{{ settings.SECRET_KEY }}`, which rendered the application's Django secret key directly in the response — solving the lab via sensitive information disclosure rather than RCE.

---
## Payload / key command
```
Add this to template text via edit: {{ settings.SECRET_KEY }} 
```

This abuses the fact that DTL's `{% debug %}` tag (or general context inspection) reveals a `settings` object is present in the template's render context. Because DTL allows plain dotted attribute access on any context variable, and `LazySettings` exposes Django settings as public (non-underscore) attributes, `settings.SECRET_KEY` resolves and renders without violating DTL's underscore restriction — leaking the `SECRET_KEY` despite DTL's sandboxing against `__class__`-style traversal.

---
## What I'd recognize faster next time
When a template engine blocks the classic dunder/MRO-walking technique outright (as DTL does, via its explicit underscore check), that's a strong signal to stop trying variations of that technique and instead look at *what's already sitting in the context* — settings objects, request objects, or app-specific variables — since plain attribute access without underscores is often still enough for a high-impact finding like secret disclosure, even when full RCE isn't reachable. Triggering `{% debug %}` early is a fast way to see the whole context and decide which path is actually worth pursuing before spending time on a dead end.
