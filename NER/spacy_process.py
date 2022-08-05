import spacy
import os
import json
import pandas as pd

class spacy_ner():
  def __init__(self):
    self.spacy_nlp = spacy.load('en_core_web_sm')

    self.spacy_dict = {}
    self.spacy_dataframe = pd.DataFrame()

  def _to_spacy_token(self,doc):
    spacy_tokens = self.spacy_nlp(doc)
    

    for token in spacy_tokens:
      # print(token.text, "   token tag   ",token.tag_)
      if not token.tag_ in self.spacy_dict.keys():
        self.spacy_dict[token.tag_] = []

      self.spacy_dict[token.tag_].append(token.text)

      self._to_dataframe()

    return spacy_tokens

  def _to_dataframe(self):
    self.spacy_dataframe = pd.DataFrame.from_dict(self.spacy_dict)
    print(self.spacy_dataframe)
    self.spacy_dataframe.to_csv(os.path.join("/content/drive/MyDrive/Document_searcher/spacy_csvs","yo.csv"))
    #save to csv to keep progress

