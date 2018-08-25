import nltk

from nltk.corpus import*
from nltk.tokenize import*
from speechtotext import SpeechToText
from sound_recorder import*
def record():
    rec = Recorder(channels=1)
    with rec.open('audio.wav', 'wb') as recfile2:
        recfile2.start_recording()
        input("press enter to end recording")
        recfile2.stop_recording()
        
def speechtotext(filename):
    STT=SpeechToText('AIzaSyAxfmMWqj3U_8UTPqIB2N9VxVkuh-_-UlQ')
    sentence=STT(filename)
    return(sentence)
def getEntityDict(tree):
    '''
    takes an input of a tree object and returns a dictionary
    containing data in the form:
        {Entity:{"Type":"","Adjs":[],"Position":""}}
    Parameters:
        tree (obj)
    Returns:
        EntityDict (dict)
    '''
    EntityDict={}
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        NP=subtree.leaves()
        Entity=False
        noun=""
        adj_list=[]
        
        for i in NP:
            if(i[1]=="NN")or(i[1]=="NNP"):
                noun=i[0]
                EntityDict[noun]={"Type":"","Adjs":[],"Position":""}
                Entity=True
                break
            else:
                pass
        if(Entity):    
            for i in NP:
                if(i[1]=="JJ"):
                    adj_list.append(i[0])
            EntityDict[noun]["Adjs"]=adj_list
        else:
            pass
    print(EntityDict)

        
            
def getRelationDict():
    pass

def understand(sentence):

    words = nltk.word_tokenize(sentence)
    tagged= nltk.pos_tag(words)
    grammar =r"""
    NP: {<DT|PP\$>?<JJ>*<NN>}
        {<NNP>+}
        

    """
    chunks=nltk.RegexpParser(grammar,loop=2)
    tree = chunks.parse(tagged)
    getEntityDict(tree)
    
while True:
    input("please press enter to start recording")
    record()
    sentence=speechtotext("audio.wav")
    print(sentence)
    understand(sentence)
    

