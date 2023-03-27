


file_name = '../Data/Book1_CMM.xlsx'

column_suffixes = ("rules": "rules_", "model": "model_")

benign_list = ['cyst', 'adenoma', 'adenomas', 'abscess', 'hemangioma', 'hematoma','fluid collection', 'lipoma','AML', 'angiomyolipoma', 'hamartoma', 'regenerative', 'focal nodular hyperplasia', 'focal fat', 'fatty infiltration','perfusion', 'fatty sparing', 'focal fat sparing', 'focal confluent fibrosis', 'FNH', 'scar', 'LIRADS 2', 'LIRADS 1', 'LR 1', 'LR 2']
indeterminate_list = ['lirads 3','lr 3', 'indeterminate', 'indeterminant', 'too small to characterize', 'versus', 'differential', 'tumor', 'dysplastic']
malignant_list = ['cancer', 'carcinoma', 'HCC', 'hcc', 'cholangiocarcinoma', 'metastasis', 'metastatic', 'metastases', 'LIRADS 4', 'LIRADS 5', 'LIRADS M', 'LIRADS TIV', 'tumor in vein', 'lirads 4', 'lirads 5', 'lirads m', 'lirads tiv']
primary_list = ['breast', 'lung', 'prostate', 'pancreatic', 'renal cell', 'RCC', 'Neuroendocrine', 'neuroendocrine', 'Carcinoid', 'carcinoid', 'lymphoma']
treatment_list = ['treated', 'Treated', 'lr-tr', 'lr-tr non-viable', 'non-viable', 'nonviable', 'viable', 'lr-tr viable', 'lr-tr equivocal', 'ablation', 'cavity', 'resection', 'hepatectomy', 'embolization', 'y-90', 'chemo-embolization', 'external beam', 'radiation', 'ebr', 'xrt', 'segmentectomy']
relevant_list = ['hepatic', 'liver', 'hepato', 'couinad', 'caudate', 'hcc']
negation_terms = ['negative', 'no evidence', 'no metastases', 'no definite']
column_to_check = 'RawReport'
column_to_check2 = 'Impression'
parsed_column = 'Parsed'
    


relevant_column = 'relevant_sentences'
benign_column = 'benign_sentences'
benign_keys_column = 'benign_diagnoses'
indeterminate_column = 'indeterminate_sentences'
indeterminate_keys_column = 'indeterminate_terms'
malignant_column = 'malignant_sentences'
malignant_keys_column = 'malignant_diagnoses'
treatment_column = 'treatment_sentences'
treatment_keys_column = 'treatment_terms'
corrected_malignant_negation = 'negation_malignant_sentences'
corrected_malignant_remainder = 'corrected_malignant_sentences'
corrected_malignant_keys_column = 'corrected_malignant_diagnoses'
    
benign_bool_column = 'benign'
malignant_bool_column = 'malignant'
indeterminate_bool_column = 'indeterminate'
treatment_bool_column = 'treatment'
corrected_malignant_bool_column = 'corrected_malignant'
    
lesion_list = ['cyst', 'FNH', 'adenoma', 'fluid_collection', 'hemangioma', 'lipoma', 'focal_fat', 'fatty sparing', 'perfusion_anomaly', 'metastasis','HCC']   