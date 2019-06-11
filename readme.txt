Slater Matsil often compares internal case claim files with official USPTO files, but these claims almost always are ordered differently between the two documents, making comparisons tedious. This tool uses content-based text analysis to reorder the claims within internal case documents, saving approx. 12 hours of work per week.

reorder_table.py:
Given a table produced by claim compare, reorders the claims in the left column (case) to match the order of the claims in the right column (patent)

Table must be named "table.docx" (case sensitive); table within document must have column titles in row 1, then alternating claim rows & blank rows every other row.

Produces a reordered table in "table_reordered.docx".

reorder_docs.py:

Given case and patent files, reorders the claims in the case file to match the order of the claims in the patent file.

Case file must be named "case.docx"; patent file must be named "patent.docx" (both case sensitive)

Patent file must contain a line beginning with "What is claimed is:" after its header, and case file must contain no additional information besides numbered claims.
