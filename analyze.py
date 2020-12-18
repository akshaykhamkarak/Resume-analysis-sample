import os.path
import csv
import PyPDF2
import spacy
import docx2txt
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
#matcher = PhraseMatcher(nlp.vocab)
#matcher.add("OBAMA", None, nlp("JAVA"),nlp("java"))
matcher = Matcher(nlp.vocab)

def Analyze(file_id,company_name):

  with open("media/job_criteria/"+company_name+".csv", newline='') as f:
      reader = csv.reader(f)
      data = list(reader)

#pattern = [{"LOWER": "java"}]
  i=1
  for d in data:
    matcher.add(""+str(i), None, [{"LOWER":d[0]}])
    i=i+1


  text=""
  if os.path.exists("media/resumes/"+str(file_id)+".pdf"):
   # print("pdf")
    with open("media/resumes/"+str(file_id)+".pdf", mode='rb') as f:
      reader = PyPDF2.PdfFileReader(f)
      page = reader.getPage(0)
      text=text+page.extractText()
  
  if os.path.exists("media/resumes/"+str(file_id)+".docx"):
    #print("docx")
    with open("media/resumes/"+str(file_id)+".docx", mode='rb') as f:
      
      text=docx2txt.process("media/resumes/"+str(file_id)+".docx")


  doc = nlp(text)
  matches = matcher(doc)
#print(matches)
  #print(len(matches))
  return len(matches)

#print(Analyze("file.pdf"))