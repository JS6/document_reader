# Document Reader, NER


## Project Objectives:

The objective of this project is to build a document reader that can extract named entities from different types of documents. In this repository, you will find a set of work items that describe the expected deliverables. The project is divided into three types of work items: Architecture, Coding and Methodology. Each work item has a set of expected artifacts.

### Architecture Work Item (WI)
The first expected work item is a Global Architecture Document (GAD) that describes the interactions between
the CMI Information System (IS) components and the document reader. The reader can be invoked programmatically
via APIs, and will also provide a User Interface (UI) enabling end users to upload a document and launch a classification,
summarization, topic modelling, NER or Q&A feature. Documents will vary in size, format and level of confidentiality.
They can be sent through different communication channels and processed in a synchronous or asynchronous way.

### Coding Work Item (WI)
Some kind of documents (e.g. docx files) can be processed by a rule-based parser coded in Python.
For this work item, the expected artifact is a program that takes a document as input and returns
a set of named entity values. The entities to extract are listed in the next slide. You can choose
which Python packages to use and the format of the output files.

### Coding Work Item (WI)
Other kind of documents (e.g. chats) can be processed by a NER model. This work item is a combination
of Python code and a Global Methodology Document (GMD). The Python code will give an overview of how to
download and run a general-purpose NER model to extract named entities. You can choose which model to use.
The methodology document will explain how this model can be fine-tuned to extract the financial entities
listed in the next slide.

### Methodology Work Item (WI)
The last type of documents (e.g. pdf files) are more verbose,
unstructured and require a more advanced language model.
For this work item a GMD will explain how to build an entity
extraction pipeline that relies on LLMs. The document will also include a
description of the prompting and/or Retrieval-Augmented Generation (RAG) techniques to be used.


## Setup environment

 ` make setup_env `

## hook pre-commit

`pre-commit install`
