from prepro_lib.preprocessor import TextOperations

path_out = 'Processed_Suicide_tweets.csv'
fout = open(path_out,'w',encoding="utf8")
fout.write("id\tcategory\ttweet\n")
#Assign "twId" the value of last review in case of adding in existing file
twId = 0 


path_in = 'Raw_Suicide_tweets.csv'
        
try:
        fin = open(path_in,'r',encoding="utf8")
except:
        print("File doesn't exist !")
        exit()
        
print('\n\nPlease wait while processing...')        

retText = ''
newLine = fin.readline()
if newLine != '':
        start = newLine.find(',')+1
        retText = retText + newLine[start:]
        text = str(retText)
        text = text.lower()
        textOp = TextOperations(text)
        resSent = textOp.reptWords()
        resWords = textOp.reptChar_spell(resSent)
        final = textOp.negWords(resWords)
        sent = ' '.join(final)
        sent = sent.capitalize()
        twId = twId + 1
        wSent = '\"' + str(twId) + '\"' + '\t' + '0' + '\t'+'\"' + sent + '\"' + '\n'
        fout.write(wSent)
else:
        pass
while newLine:
    current = fin.tell()
    fin.seek(current)
    retText = ''
    newLine = fin.readline()
    if newLine != '':
        start = newLine.find(',')+1
        retText = retText + newLine[start:]
        text = str(retText)
        text = text.lower()
        textOp = TextOperations(text)
        resSent = textOp.reptWords()
        resWords = textOp.reptChar_spell(resSent)
        final = textOp.negWords(resWords)
        sent = ' '.join(final)
        if sent!= '':
                sent = sent.capitalize()
                twId = twId + 1
                wSent = '\"' + str(twId) + '\"' + '\t' + '0' + '\t'+'\"' + sent + '\"' + '\n'
                fout.write(wSent)
    else:
            pass
fin.close()   

print("\n\nProcess Completed Successfully !")

fout.close()            
