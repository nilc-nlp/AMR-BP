# Abstract Meaning Representation for Brazilian Portuguese

This repository contains all AMR-annotated corpora developed by the Interinstitutional Center for Computational Linguistics (NILC).

For more information about what is AMR and its specific notations, we indicate the [AMR guidelines](https://github.com/amrisi/amr-guidelines) GitHub repository.

## Organization

This repository is organized in subdirectories, which contain each individual corpus. All corpora are distributed under the [CC-BY-NC-SA license](LICENSE.md).

### [OpiSums-PT-AMR](OpiSums-PT-AMR-v1)

This corpus contains opinion texts from the [OpiSums-PT corpus](http://www.google.com/url?q=http%3A%2F%2Fconteudo.icmc.usp.br%2Fpessoas%2Ftaspardo%2Fsucinto%2Ffiles%2FOpiSums-PT.zip&sa=D&sntz=1&usg=AFQjCNH7mwRNQ3L4E_AYHlsXLCwKdmqgTA) manually annotated in AMR.

### [AMR](AMR-v1)

This corpus contains news texts from the Folha de São Paulo newspaper manually annotated in AMR.

### [AMR-LittlePrince](AMR-LittlePrince)

This corpus contains sentences from the Little Prince tale annotated in AMR through alignment from the [English version](https://amr.isi.edu/download/amr-bank-struct-v1.6.txt) and later manually revised.

---

For more detailed information about each corpus, please read the README file in the specific corpus directory.

## Corpus notation

The corpora follow a standard notation to ease the reading of files. A corpus file contains multiple sentences, each with some metainformation, which starts with a hashtag followed by double colons (# ::) and a keyword (id, snt, alignment...). Then, the AMR graph representation in the PENMAN notation is written. An example is shown below:

```
# ::id Fala-Serio-Mae.Documento_32.1
# ::snt Amei esse livro .
(a / amar-01
      :ARG0 (e2 / eu)
      :ARG1 (l / livro
            :mod (e3 / esse)))
```

A blank line separates each sentence.
