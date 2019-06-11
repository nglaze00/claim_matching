import docx, time
from collections import defaultdict




def slice(claim):
    """
    Removes "*." from the beginning of claim
    :param claim: string
    :return: claim w/ prefix removed
    """
    return claim.split(".", 1)[1]

def compare_strings(str1, str2):
    """
    Returns the difference in word counts between str1 and str2, based on str1.
    :param str1: string
    :param str2: string
    :return: int
    """
    diff = 0
    words1 = str1.split(" ")
    words2 = str2.split(" ")
    counts1, counts2 = defaultdict(int), defaultdict(int)

    for word in words1:
        counts1[word] += 1
    for word in words2:
        counts2[word] += 1
    diff = 0
    for word in counts1.keys():
        diff += abs(counts1[word] - counts2[word])

    return diff

def compute_diffs(key, other, slice, fast):
    """
    Compares.
    :param key: list of strings
    :param other: list of strings
    :param slice: function to format strings before comparing
    :param fast: boolean; True: only computes scores for unmatched elements of other
    :return: diffs: matrix of ints where diffs[i, j] = compare_strings score between key[i] and other[j]; last index
                    in each row is index of min difference
    """
    reorder = [""] * len(other)
    matched = [False] * len(other)
    diffs = []  #Score matrix: row = scores for key
    for index, item in enumerate(key):
        diffs_row = []
        closest = (None, float("inf"))
        for index, test in enumerate(other):
            if not matched[index] or not fast:
                diff = compare_strings(slice(item), slice(test))
                diffs_row.append(diff)
                if diff < closest[1]:
                    closest = (index, diff)
            else:
                diffs_row.append(float("inf"))
        matched[closest[0]] = True
        diffs_row.append(closest[0])
        diffs.append(diffs_row)

    return diffs

def reorder_lists(key, other, diffs):
    """
    Reorders the items of other to match those of key so that string differences are minimized
    :param key: list of strs
    :param other: list of strs
    :param diffs: difference matrix computed by compute_diffs
    :return: key and other, with other reordered to match key as closely as possible
    """
    reordered = [""] * len(other)
    for i in range(len(key)):
        reordered[i] = other[diffs[i][-1]]
    return key, reordered

def patent_to_list(file):
    """
    Extracts and returns the claims present in a Google Patents file
    :param file: filename of patent document
    :return: list of strings, each representing a claim
    """
    doc = docx.Document(file)
    paras = []
    after_header = False

    after_header, before_footer = False, True
    i = 0
    while i < len(doc.paragraphs):
        para = doc.paragraphs[i].text
        if after_header and para == "":
            before_footer = False
        if after_header and before_footer:
            paras.append(para)
            i += 1
        if para[:4] == "What":
            after_header = True
            i += 1
        i += 1
    return paras
#patent_to_list("patent example.docx")
def case_to_list(file):
    """
    Extracts and returns the claims present in a case file
    :param file: filename of case document
    :return: list of strings, each representing a claim
    """
    doc = docx.Document(file)
    paras = []
    after_header = False

    after_header, before_footer = False, True
    i = 0
    para = ""
    while i < len(doc.paragraphs):

        item = doc.paragraphs[i].text
        if "(Canceled)" not in item:
            item = item.replace("\n", "")
            item = item.replace("\t", " ")
            if len(item) > 1 and "." in item[1:5]:
                paras.append(para)
                para = ""
            para += " " + item

        i += 1              #Account for paragraphs split & \n, \t
    paras.append(para)
    return paras[1:]

def reorder_case_claims(patent_file, case_file):
    """
    Reorders the claims in case_file, using patent_file as the key.
    :param patent_file: string - filename
    :param case_file: string - filename
    :return: none; produces case_file_reordered.docx
    """
    other, key = case_to_list(case_file), patent_to_list(patent_file)

    diffs = compute_diffs(key, other, slice, False)
    _, reordered = reorder_lists(key, other, diffs)
    doc = docx.Document(case_file)
    doc._body.clear_content()
    for claim in reordered:
        doc.add_paragraph(claim)
        doc.add_paragraph("")
    doc.save(case_file.split(".")[0] + "_reordered.docx")

try:
    reorder_case_claims("patent.docx", "case.docx")
    print("Claims matched successfully. Closing in 5 seconds...")
    time.sleep(5)
except:
    time.sleep(5)