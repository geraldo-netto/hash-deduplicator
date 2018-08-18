# Hash Deduplicator
* Hash deduplicator allows to identify duplicated hashes
* This can be useful when you have a set of (hashed eg: md5) files with distinct names but with exactly the same content

# Example
```bash
netto@morpheus /media/netto/SAMSUNG $ cat dupl.md5
...
f38f8bb4528f88b7fb988df538d5b6d5  documentacao/pdf/sm.pdf
f38f8bb4528f88b7fb988df538d5b6d5  documentacao/pdf/sm.pdf.1
f38f8bb4528f88b7fb988df538d5b6d5  documentacao/pdf/s/sm.pdf
netto@morpheus /media/netto/SAMSUNG $ dedupl.py dupl.md5
...
d5b6d5  documentacao/pdf/sm.pdf
d5b6d5  documentacao/pdf/sm.pdf.1
d5b6d5  documentacao/pdf/s/sm.pdf
equal files: 51568 / 182253
```

# TODO
* implement mmap when opening files
* improve loop structure
* integrate with the metadata deduplicator
* add more documentation/use cases
* cleanup code

# License
[MIT License](https://opensource.org/licenses/MIT)

