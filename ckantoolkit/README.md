# ckantoolkit

ckantoolkit is a library that wraps ckan.plugins.toolkit with backported
attributes to ease developing CKAN extensions that work with a wide
range of CKAN versions.

## Example

```python
from ckan.plugins.toolkit import ungettext # CKAN >= 2.5 only
```

becomes:

```python
from ckantoolkit import ungettext
```

## Extras

ckantoolkit includes a `tests` submodule that points to the correct
ckan test module. If your extension builds on ckan's test factories
your:

```python
try:
    from ckan.tests.factories import Sysadmin
except ImportError: # for ckan <= 2.3
    from ckan.new_tests.factories import Sysadmin
```

becomes:

```python
from ckantoolkit.tests.factories import Sysadmin
```
