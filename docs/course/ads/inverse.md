---
date-created: 2022-04-18 08:51
date-updated: 2022-06-23 21:16
---

# Inverted File Index

## Definition

**Index** is a mechanism for locating a given term in a text.

**Inverted file** contains a list of pointers, Inverted because it lists for a **term**

## Modules

- Token analyzer + stop filter
	- Word Stemming
	- Stop Words
- index
	- search tree
	- hash table
		- distributed index
- Dynamic indexing
	- Docs come in / deleted
- Thresholding
	- only retrieve the top x documents

## **Measures**

- How fast does it index
- How fast does it search
- Expressiveness of query language

### Data retrieval performance

- index space
- response time

### Relevance measurement requires 3 elements

- A benchmark document collection
- A benchmark suite of queries
- A binary **assessment** of either relevent or irrelevant for each query-doc pair

	|              | relevant | Irrelevant |
	| ------------ | -------- | ---------- |
	| Retrived     | $R_R$    | $I_R$      |
	| Not Retrived | $R_N$    | $I_N$      |

	- _Precision_ $P =R_R/(R_R+I_R)$
	- _Recall_ $R = R_R/(R_R+R_N)$
