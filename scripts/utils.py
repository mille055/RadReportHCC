import re
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, recall_score
from sklearn import metrics


def parse_report_text(data, col, new_col):
    df1=data.copy()
    df1[new_col]=df1.apply(lambda row: nltk.sent_tokenize(row[col]), axis=1)
    
    return df1

def structured_findings_and_conclusions(text, start_string='ABDOMEN: LIVER:', end_string = 'BILIARY', impression_string='CONCLUSION:'):

    beginning = 0
    end = 0
    impression = 0
    for i in range(len(text)):
        if text[i].startswith('ABDOMEN: LIVER: '):
            beginning = i
        if text[i].startswith('BILIARY'):
            end = i
        if text[i].startswith('CONCLUSION:'):
            impression = i
        
    findings = text[beginning:end]
    impression = text[impression:-1]
    return sub_sample, sub_impression

def find_relevant_text(text, start_string='ABDOMEN: LIVER:', end_string='BILIARY', impression_string='CONCLUSION:', keywords = ['hepatic', 'Hepatic','liver','Liver', 'hepato','Hepato', 'Couinad', 'caudate', 'HCC']):
    
    beginning = 0
    end = 0
    impression = 0
    finding_start=0
    
    findings_text = []
    impression_text = []
    relevant_impression = []
    
    
    for i in range(len(text)):
        if text[i].startswith('CONCLUSION:'):
            impression = i
            #print(f'conclusion {impression}')
        if text[i].startswith('FINDINGS:'):
            finding_start = i
        
        if ('LIVER:') in text[i]:
            beginning = i
            #print(f'beginning {beginning}')
        if (('BILIARY' or 'GALLBLADDER') in text[i]):
            end = i

    findings_text = text[beginning:end]
    if findings_text==[]:
        if (finding_start) and (impression>finding_start):
            findings_text = find_relevant_sentences(text[finding_start:impression], keywords)
        else:
            findings_text = find_relevant_sentences(text[finding_start:-1], keywords)
    if impression:
        impression_text = text[impression:] 
    
    #print(impression_text)
    relevant_impression = find_relevant_sentences(impression_text, keywords)
    total_text=findings_text+relevant_impression

    return findings_text, relevant_impression, total_text
   

def find_relevant_sentences(list, keywords):
    re_list=[]
    #print(f'keywords {keywords}')
    for item in list:
        for word in keywords:
            #print(f'checking {word}')
            if word in item:
                re_list.append(item)
    
    return re_list


def find_lesion_keyword(list, keywords):
    sentence_list=[]
    keyword_list = []
    #print(f'keywords {keywords}')
    for item in list:
        for word in keywords:
            #print(f'checking {word}')
            if word in item:
                sentence_list.append(item)
                keyword_list.append(word)
    return sentence_list, keyword_list



def Process_frame(data):
    df1=data.copy()
    df1 = df1.fillna(0)
    
    df1[parsed_column] = df1.apply(lambda row: nltk.sent_tokenize(row[column_to_check]), axis=1)
    
    df1[relevant_column] = df1.apply(lambda row: find_relevant_text(row[parsed_column], relevant_list)[2], axis=1)
    
    df1[benign_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], benign_list)[0], axis=1)
    df1[benign_keys_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], benign_list)[1], axis=1)
    df1[malignant_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], malignant_list)[0], axis=1)
    df1[malignant_keys_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], malignant_list)[1], axis=1)
    df1[indeterminate_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], indeterminate_list)[0], axis=1)
    df1[indeterminate_keys_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], indeterminate_list)[1], axis=1)
    df1[treatment_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], treatment_list)[0], axis=1)
    df1[treatment_keys_column] = df1.apply(lambda row: find_lesion_keyword(row[relevant_column], treatment_list)[1], axis=1)

    df1[benign_bool_column] = df1.apply(lambda row: int(bool(row[benign_column])), axis=1)
    df1[malignant_bool_column] = df1.apply(lambda row: int(bool(row[malignant_column])), axis=1)
    df1[treatment_bool_column] = df1.apply(lambda row: int(bool(row[treatment_column])), axis=1)
    
    df1[corrected_malignant_negation] = df1.apply(lambda row: find_lesion_keyword(row[malignant_column], negation_terms)[0], axis=1)
    #df1[corrected_malignant_remainder] = df1[df1[malignant_column],df1[corrected_malignant_negation]].apply(lambda x: [i for i in x[0] if i not in x[1]], axis=1)
    df1[corrected_malignant_remainder] = df1[['Malignant Sentences','Negation Malignant Sentences']].apply(lambda x: [i for i in x[0] if i not in x[1]], axis=1)
    #df1['Primary (extra-hepatic)'] = df1[['Malignant Diagnoses'].apply(lambda row: [i for i in row if ])
    df1[corrected_malignant_bool_column] = df1.apply(lambda row: int(bool(row[corrected_malignant_remainder] or row[treatment_bool_column])), axis=1)

    #columns for each type of lesion
    df1['Auto_Cyst'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['cyst','cysts'])[1])), axis=1)
    df1['Auto_FNH'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['FNH','focal nodular hyperplasia'])[1])), axis=1)
    df1['Auto_Adenoma'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['adenoma','Adenoma'])[1])), axis=1)
    df1['Auto_Abscess/Hematoma/Collection'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['abscess','Abscess', 'hematoma', 'Hematoma', 'fluid collection'])[1])), axis=1)
    df1['Auto_Hemangioma'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['hemangioma','Hemangioma'])[1])), axis=1)
    df1['Auto_Lipoma_aml'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['lipoma','Lipoma', 'AML', 'angiomyolipoma'])[1])), axis=1)
    df1['Auto_Focal_fat'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['focal fat', 'fatty infiltration'])[1])), axis=1)
    df1['Auto_Fatty_sparing'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['fatty sparing', 'focal fat sparing'])[1])), axis=1)
    df1['Auto_Perfusion_anomaly'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row[relevant_column], ['perfusion'])[1])), axis=1)
    df1['Auto_HCC'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row['Corrected Malignant Sentences'], ['HCC', 'hepatocellular', 'LI-RADS 4', 'LI-RADS 5', 'LI-RADS TR'])[1])), axis=1)
    df1['Auto_mets'] = df1.apply(lambda row: int(bool(find_lesion_keyword(row['Corrected Malignant Sentences'], ['metastas', 'metastatses', 'metastasis', 'metastatic'])[1])), axis=1)
    return df1


def compare_single(gt_row, auto_row):
    print(classification_report(gt_row, auto_row))
