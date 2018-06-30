# Hash Deduplicator
hash deduplicator allows to identify duplicated hashes
this can be useful when you have a set of files with distinct names but with exactly the same content

# Example
```bash
netto@besta01 /media/netto/SAMSUNG $ cat dupl.md5
57e7de  documentacao/pdf/sp800_100_mar07_2007.pdf
57e7de  documentacao/pdf/s/sp800-100-mar07-2007.pdf
886c4b  software/exdev/DBAnalyser/bin/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
886c4b  software/exdev/DBAnalyser/src/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
886c4b  software/exdev/DBAnalyser/src/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
...
062388  documentacao/pdf/sm.pdf
062388  documentacao/pdf/sm.pdf.1
062388  documentacao/pdf/sm.pdf.1
062388  documentacao/pdf/s/sm.pdf
netto@besta01 /media/netto/SAMSUNG $ dedupl.py dupl.md5
57e7de  documentacao/pdf/sp800_100_mar07_2007.pdf
57e7de  documentacao/pdf/s/sp800-100-mar07-2007.pdf
886c4b  software/exdev/DBAnalyser/bin/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
886c4b  software/exdev/DBAnalyser/src/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
886c4b  software/exdev/DBAnalyser/src/net/sf/exdev/dbanalyser/resources/documentation/JSON-pt_files/object.gif
...
062388  documentacao/pdf/sm.pdf
062388  documentacao/pdf/sm.pdf.1
062388  documentacao/pdf/sm.pdf.1
062388  documentacao/pdf/s/sm.pdf
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
