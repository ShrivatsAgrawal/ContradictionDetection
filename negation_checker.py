# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:10:11 2019

@author: Shrivats Agrawal
"""

contr_negation=0
contradictionlist=list()

def checknegationcontradiction(antonym_tracker,negdoc1,negdoc2):
    temp_var=negdoc1+negdoc2+antonym_tracker
    if(temp_var%2!=0 and temp_var<3):
        return 1
    else:
        return 0
    '''if(negdoc1==1 or negdoc1=="") and (negdoc2=="neg" or negdoc2=="") :
        if ("not" in sent1 and "not" not in sent2) or ("not" in sent2 and "not" not in sent1) and antonym_tracker==1:
            contr_tracker=0
        elif ("not" in sent1 and "not" in sent2):
            contr_tracker=0
        elif (("not" in sent1 and "not" not in sent2) or ("not" in sent2 and "not" not in sent1) and antonym_tracker==0):
            contr_tracker=1
            contr_negation=1
    return contr_tracker'''
        
        
    
    