# Case file reordering tool
Python script for content-based reorganization of law firm Slater Matsil's internal case files. Used by law firm Slater Matsil to save 12 hours of work per week. 

## Overview
The law firm Slater Matsil, LLP handles many cases simultaneously, each of which can have dozens of files containing descriptions of the various patent claims involved with the case. One step of their case workflow is verifying that the content of their files matches that of those on file with the US Patent & Trademark Office (USPTO).

Due to the fact that the claims within each USPTO file are almost always appear in a different order than those stored locally by Slater Matsil, this process often takes over 10 hours per week. My tool automates this process, allowing it to be carried out in almost no time.

This Python script reorganizes the claims within Slater Matsil's files to match those in the USPTO's files, and notifies the user if any files exist with claims that may not match.

## Installation / Usage
The most useful file is **reorder_docs.exe**, which reorders all the files in one folder named **local** to match those in another folder named **uspto**.

Download this file and move it to the directory containing folders **local** and **uspto**, as seen below. 

![](https://github.com/nglaze00/reorder_claims/blob/master/readme_pics/directories.png)

Double-click on the file to reorder the claims in **local**. Doing so will create a new folder, **local_reordered**. For each local file (e.g. **local1.docx**), a reordered file (e.g. **local1_reordered.docx**) is created in **local_reordered**.

If the software detects any disparities in the claims present in the documents, the console will output a line such as:
```
Claim 3 may not match; check it!
```
* USPTO files must contain a line beginning with **"What is claimed is:"** after its header, and local files must contain no additional information besides numbered claims (This formatting has held for all USPTO and Slater Matsil files the script has run on).

## Example

Below is an excerpt from a USPTO file (left) and a local Slater Matsil file (right) with sensitive information removed. This is before reordering, so the claims in the local file are in a different order than those in the USPTO file.

![](https://github.com/nglaze00/reorder_claims/blob/master/readme_pics/uspto_local.jpg)

After running **reorder_docs.exe** on the documents, comparing the USPTO file (left) and reordered local file (right) reveals that the claims in both files are now in the same order. A beneficial side effect of this script is that it also improves the often inconsistent paragraph formatting in Slater Matsil's local files.

![](https://github.com/nglaze00/reorder_claims/blob/master/readme_pics/reordered.png)

Console output:

![](https://github.com/nglaze00/reorder_claims/blob/master/readme_pics/output.png)
