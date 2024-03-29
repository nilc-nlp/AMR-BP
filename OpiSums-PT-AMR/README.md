# OpiSums-PT-AMR

This is OpiSums-PT-AMR, an AMR annotated corpus of opinion texts in Brazilian Portuguese. All sentences come from the [OpiSums-PT corpus](http://www.google.com/url?q=http%3A%2F%2Fconteudo.icmc.usp.br%2Fpessoas%2Ftaspardo%2Fsucinto%2Ffiles%2FOpiSums-PT.zip&sa=D&sntz=1&usg=AFQjCNH7mwRNQ3L4E_AYHlsXLCwKdmqgTA), which is a corpus created for Opinion Summarization in Brazilian Portuguese by Lopéz et al. (2015).

## Corpus

The corpus is organized in a single file [`amr-opisums-pt.txt`](amr-opisums-pt.txt) with multiple sentences. Each sentence is separated by a blank line.

Every sentence has a unique ID corresponding to their location in the OpiSums-PT original corpus. The ID has the following format: `directory.file.line`, in which `directory` indicates the name of the directory (product) in the original corpus, `file` indicates the file name within the directory and `line` indicates the line number within the file.

There is also an indication of the original sentence represented in AMR. An example is shown as follows:

```
# ::id Fala-Serio-Mae.Documento_24.0
# ::snt Achei o livro um pouco fútil .
(a / achar-02
      :ARG0 (e / eu)
      :ARG1 (l / livro)
      :ARG2 (f / fútil
            :degree (u / um-pouco)))
```

## New verbs

There is also a [`new-verbs.txt`](new-verbs.txt) file, which contains a list of verbs that do not exist within the [VerboBrasil](http://143.107.183.175:21380/verbobrasil/) repository. This is maintained as there may be researchers interested in further enhance this important resource for the Brazilian Portuguese language.

## How to cite

### Master's Thesis

Inácio, M. L. (2021). Sumarização de Opinião com base em Abstract Meaning Representation [Mestrado em ciências de computação e matemática computacional, Universidade de São Paulo]. https://doi.org/10.11606/D.55.2021.tde-13092021-141741

```bibtex
@mastersthesis{Inacio2021,
  type = {{Mestrado em ci\^encias de computa\c{c}\~ao e matem\'atica computacional}},
  title = {{Sumariza\c{c}\~ao de Opini\~ao com base em Abstract Meaning Representation}},
  author = {In{\'a}cio, Marcio Lima},
  year = {2021},
  month = sep,
  publisher = {{Universidade de S\~ao Paulo}},
  address = {{S\~ao Carlos}}
}
```

### Journal Article (Preprint)

Inácio, M. L., Cabezudo, M. A. S., Ramisch, R., Di Felippo, A., & Pardo, T. A. S. (2022). The AMR-PT corpus and the semantic annotation of challenging sentences from journalistic and opinion texts [Preprint]. https://doi.org/10.1590/1678-460x202255159

```bibtex
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

## References

López, R., Pardo, T., Avanço, L., Filho, P., Bokan, A., Cardoso, P., Dias, M., Nóbrega, F., Cabezudo, M., Souza, J., Zacarias, A., Seno, E., and Di Felippo, A. (2015). A qualitative analysis of a corpus of opinion summaries based on aspects. In *Proceedings of The 9th Linguistic Annotation Workshop*, pages 62–71, Denver, Colorado, USA, June. Association for Computational Linguistics.

## Acknowledgements

The authors are grateful to [CAPES](http://capes.gov.br/) and [USP Research Office](https://www5.usp.br/english/research/) for supporting this work. This work is part of the [OPINANDO project](https://sites.google.com/icmc.usp.br/opinando/).
