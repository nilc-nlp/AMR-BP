# Abstract Meaning Representation for Brazilian Portuguese

This repository contains all AMR-annotated corpora developed by the Interinstitutional Center for Computational Linguistics (NILC).

For more information about what is AMR and its specific notations, we indicate the [AMR guidelines](https://github.com/amrisi/amr-guidelines) GitHub repository.

## Organization

This repository is organized in subdirectories, which contain each individual corpus. All corpora are distributed under the [CC-BY-NC-SA license](LICENSE.md).

### [OpiSums-PT-AMR](OpiSums-PT-AMR)

This corpus contains opinion texts from the [OpiSums-PT corpus](http://www.google.com/url?q=http%3A%2F%2Fconteudo.icmc.usp.br%2Fpessoas%2Ftaspardo%2Fsucinto%2Ffiles%2FOpiSums-PT.zip&sa=D&sntz=1&usg=AFQjCNH7mwRNQ3L4E_AYHlsXLCwKdmqgTA) manually annotated in AMR.

### [AMRNews](AMRNews)

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


## Statistics

Statistics of each corpus can be obtained by running the script `stats_amr.py` in this way:

```
python stats_amr.py <corpus_path> #For example: AMRNews/unsplit/amr.txt
```

## Publications

Both **OpiSums-PT-AMR and AMRNews** are presented and compared in more detail in the following paper, which has been accepted for publication in DELTA and is currently [available as in a pre-print format](https://doi.org/10.1590/1678-460x202255159).

```
@techreport{InacioEtAl2022,
  type = {Preprint},
  title = {The {{AMR-PT}} Corpus and the Semantic Annotation of Challenging Sentences from Journalistic and Opinion Texts},
  author = {In{\'a}cio, Marcio Lima and Cabezudo, Marco Antonio Sobrevilla and Ramisch, Renata and Di Felippo, Ariani and Pardo, Thiago Alexandre Salgueiro},
  year = {2022},
  month = aug,
  doi = {10.1590/1678-460x202255159},
  url = {https://preprints.scielo.org/index.php/scielo/preprint/view/4652/version/4928},
  urldate = {2022-08-31},
  copyright = {All rights reserved}
}
```

The **AMR-LittlePrince** corpus is described in:

```
@inproceedings{anchieta-pardo-2018-towards,
    title = "Towards {AMR}-{BR}: A {S}em{B}ank for {B}razilian {P}ortuguese Language",
    author = "Anchi{\^e}ta, Rafael  and
      Pardo, Thiago",
    booktitle = "Proceedings of the Eleventh International Conference on Language Resources and Evaluation ({LREC} 2018)",
    month = may,
    year = "2018",
    address = "Miyazaki, Japan",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://www.aclweb.org/anthology/L18-1157",
}
```
