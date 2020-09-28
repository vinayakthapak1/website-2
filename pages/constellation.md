<!--
.. title: AskOmics constellation
.. slug: constellation
.. date: 2020-09-21 12:21:55 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. hidetitle: true
-->

## AskOmics constellation

AskOmics constellation is a set of tool that generate TSV files than can be uploaded into AskOmics to be converted into a RDF datasets and interrogated and
cross referenced with other RDF data with the visual interface of AskOmics.

### Abstractor

[Abstractor](https://github.com/askomics/abstractor) is a command line tool that generate an AskOmics abstraction of a distant SPARQL endpoint.
This abstraction can be loaded into AskOmics to explore distant SPARQL endpoint.

### AskoR

[AskoR](https://github/askomics/askoR) is a R library that perform statistical analysis from RNA-seq data.
Its outputs are an enriched lists of differentially expressed genes from each contrast derived from the experimental design.
This files can then be loaded in AskOmics to perform complex queries.

[bbip AskOmics instance](https://bbip.askomics.org) contain differential expression
data of *Brassica* species obtained with AskoR.
This instance makes it possible to interrogate these data with the graphical interface of AskOmics.

### AuReMe

[AuReMe](http://aureme.genouest.org/) workspace is designed for tractable reconstruction of metabolic networks.
The toolbox allows for the Automatic Reconstruction of Metabolic networks based on the combination of multiple
heterogeneous data and knowledge sources ([Aite *et al.*, 2018](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006146)).

The main added-values are the inclusion of graph-based tools relevant for the study of non-classical organisms
(Meneco and Menetools packages), the possibility to trace the reconstruction and curation procedures (the Padmet package),
and the exploration of reconstructed metabolic networks with [wikis](http://aureme.genouest.org/wiki.html).

After a metabolic network has been reconstructed from the genbank file associated with a species and a reference metabolic database,
the content of the metabolic network can be explored through AskOmics thanks to the following commands:

```bash
usage:
    padmet_to_tsv.py --padmetSpec=FILE [--padmetRef=FILE] --output_dir=DIR [-v]
    padmet_to_tsv.py --padmetRef=FILE [--padmetSpec=FILE] --output_dir=DIR [-v]

options:
    -h --help     Show help.
    --padmetSpec=FILE    path of the padmet representing the network to convert
    --padmetRef=FILE    path of the padmet representing the database
    --output_dir=DIR
    -v
```
Obtained TSV file can be loaded into an AskOmics instance to be converted into RDF and explored with the visual interface.

The AskOmics endpoint can then be enriched with additional information: include several metabolic networks
associated with the name reference metabolic database, enrich with gene expression measurements for one or several species.
