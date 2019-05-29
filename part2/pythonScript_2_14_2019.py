import pandas as pd
import scipy as sp

ucsc = pd.read_table("built_with_change_types_2_14_2019.tsv", sep='\t', header=0)
variants = pd.read_csv('allBRCAVariantsRSA.csv', index_col=None)

f = open("brca1_scores.csv", "a")

chromosome = 0
for i in range(0, len(variants)):
    cDNA = variants['cDNA'][i]
    print(cDNA)
    if(variants['sequenceID'][i] == "NP_009225"):
        chromosome = 17
    else:
        chormosone = 13
    for j in range(0, len(ucsc)):
        if (chromosome == ucsc['Chr'][j] and ucsc['Clinical_Significance_ClinVar'][j] != '-' ):
            targetCDna = ucsc['pyhgvs_cDNA'][j]
            target = targetCDna[12:]
            if (cDNA == target):
                f.write(str(variants['sequenceID'][i]) + ',' + str(variants['cDNA'][i]) + ',' + str(variants['aaChange'][i]) + ',' + str(variants['rsa'][i]) + ',' + str(variants['pPrior'][i]) + ',' + str(variants['aPrior'][i]) + ',' + str(ucsc['proteinPrior'][j]) + ',' + str(ucsc["applicablePrior"][j]) + ',' + str(ucsc['pyhgvs_cDNA'][j]) + ',"' + str(ucsc['Clinical_Significance_ClinVar'][j]) + '"\n')
                break
            
