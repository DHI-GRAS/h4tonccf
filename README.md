# h4tonccf

Convert HDF-EOS HDF4 files to CF compliant netCDF files from Python

Includes and wraps the binaries from http://hdfeos.org/software/h4cflib.php

## Usage

```python
import h4tonccf
outfile = h4tonccf.run('/path/to/some/file.hdf')
assert outfile.endswith('.nc')
```
