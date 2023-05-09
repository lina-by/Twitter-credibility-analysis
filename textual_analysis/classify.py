import pandas as pd
df = pd.read_csv("train.csv")
df=pd.DataFrame(df)
# print(df.rows)

def train(df):
    from textblob.classifiers import NaiveBayesClassifier
    toxic, severe_toxic, obscene, threat, insult, identity_hate=[],[],[],[],[],[]
    n=len(df)

    # Pour chaque ligne on ajoute la phrase dans les catégories dont elle fait partie
    for i in range(n):
        row=df.iloc[i,:]
        
        # Le texte est-il toxic ?
        '''
        if row["toxic"]==1:
            toxic = toxic + [(row["comment_text"],"toxic")]
        else :
            toxic = toxic + [(row["comment_text"],"non_toxic")]
        
        # Le texte est-il severe_toxic ?
        if row["severe_toxic"]==1:
            severe_toxic = severe_toxic + [(row["comment_text"],"severe_toxic")]
        else :
            severe_toxic = severe_toxic + [(row["comment_text"],"non_severe_toxic")]
        
        # Le texte est-il obscene ?
        if row["obscene"]==1:
            obscene = obscene + [(row["comment_text"],"obscene")]
        else :
            obscene = obscene + [(row["comment_text"],"non_obscene")]
        
        # Le texte est-il threat ?
        if row["threat"]==1:
            threat = threat + [(row["comment_text"],"threat")]
        else :
            threat = threat + [(row["comment_text"],"non_threat")]
        
        # Le texte est-il insult ?
        if row["insult"]==1:
            insult = insult + [(row["comment_text"],"insult")]
        else :
            insult = insult + [(row["comment_text"],"non_insult")]
        '''
        # Le texte est-il identity_hate ?
        if row["identity_hate"]==1:
            identity_hate = identity_hate + [(row["comment_text"],"identity_hate")]
        else :
            identity_hate = identity_hate + [(row["comment_text"],"non_identity_hate")]
        
    #création des classifiers
    #toxic = NaiveBayesClassifier(toxic)
    #severe_toxic = NaiveBayesClassifier(severe_toxic)
    #obscene = NaiveBayesClassifier(obscene)
    #threat = NaiveBayesClassifier(threat)
    #insult = NaiveBayesClassifier(insult)
    identity_hate=NaiveBayesClassifier(identity_hate)
    print("ok")
    #return [toxic, severe_toxic, obscene, threat, insult, identity_hate]
    return identity_hate
cl=train(df)

import pickle
# save the classifier
'''
with open('toxic_classifier.pkl', 'wb') as tox:
    pickle.dump(cl[0], tox) 
with open('severe_toxic_classifier.pkl', 'wb') as stox:
    pickle.dump(cl[1], stox)
with open('obscene_classifier.pkl', 'wb') as obs:
    pickle.dump(cl[2], obs)
with open('threat_classifier.pkl', 'wb') as thr:
    pickle.dump(cl[3], thr)
with open('insult_classifier.pkl', 'wb') as ins:
    pickle.dump(cl[4], ins)
'''
with open('identity_hate_classifier.pkl', 'wb') as idh:
    pickle.dump(cl, idh)      



