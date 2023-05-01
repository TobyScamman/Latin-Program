from generator import *
from ladict import *
from random import *

def PrepositionalPhrase(prepVerb):
    latinPreposition = prepVerb.preposition[randint(0, len(prepVerb.preposition) - 1)]
    # post - after a phrase
    prepNoun = latinPreposition.subjects[randint(0, len(latinPreposition.subjects) - 1)]
    prepNoun = [i for i in LatinNouns if prepNoun in i.info['category']][randint(0, len([i for i in LatinNouns if prepNoun in i.info['category']]) - 1)]
    if 'number' in prepNoun.info:
        prepNumber = prepNoun.info['number']
    elif latinPreposition == inter:
        prepNumber = 2
    else:
        prepNumber = randint(1,2)
    englishPreposition = EnglishPrepositions[LatinPrepositions.index(latinPreposition)]
    englishPrepNoun = EnglishNouns[LatinNouns.index(prepNoun)]
    prepArticle, englishPrepNoun = englishPrepNoun.Decline(prepNumber, 3)
    return latinPreposition.prep + ' ' + prepNoun.Decline(prepNumber, latinPreposition.case) + ' ', englishPreposition.prep + ' ' + prepArticle + englishPrepNoun + ' '

def Nominative(nominativePerson):
    if (nominativePerson == 3 or nominativePerson == 6) and randint(1,3) > 1:
        nominative = [i for i in LatinNouns if 'person' in i.info['category']][randint(0, len([i for i in LatinNouns if 'person' in i.info['category']]) - 1)]
        if randint(1,2) == 1:
            latNomAdj, englishNomAdj, adjInfo = Adjective(nominativePerson // 3, nominative.gender, 1, 'person')
        else:
            latNomAdj = englishNomAdj = ''
            adjInfo = ['', False]
        englishNom = EnglishNouns[LatinNouns.index(nominative)]
        englishNomArticle, englishNom = englishNom.Decline(nominativePerson // 3, 1)
        if adjInfo[1]: #if the english adjective has a custom superlative i.e. greatest
            englishNomArticle = 'the '
        elif englishNomArticle == 'an ' and latNomAdj != '':
            englishNomArticle = 'a '
        if 'adjReplace' in adjInfo[0]:
            englishNom = englishNomAdj + englishNom + ' '
        elif 'adjBefore' in adjInfo[0]:
            englishNom = englishNomAdj + englishNomArticle + englishNom + ' '
        else:
            englishNom = englishNomArticle + englishNomAdj + englishNom + ' '
            
        return latNomAdj + nominative.Decline(nominativePerson // 3, 1) + ' ', englishNom, nominative.gender
    else:
        nominativeGender = randint(1,3)
        if nominativePerson == 1:
            return '', 'I ', nominativeGender
        elif nominativePerson == 2 or nominativePerson == 5:
            return '', 'you ', nominativeGender
        elif nominativePerson == 3:
            if nominativeGender == 1:
                return '', 'she ', 1
            elif nominativeGender == 2:
                return '', 'he ', 2
            else:
                return '', 'it ', 3
        elif nominativePerson == 4:
            return '', 'we ', nominativeGender
        elif nominativePerson == 6:
            return '', 'they ', nominativeGender
        else:
            return '', '', nominativeGender

def Adjective(number, gender, case, adjList=LatinAdjectives):
    if adjList == 'person':
        adjList = [alter, audax, bonus, celer, crudelis, diligens, felix, ferox, fidelis, fortis, gravis, infelix, ingens, iratus, laetus, lentus, magnus, malus, miser, multus, nonnulli, novus, nullus, omnis, parvus, pauci, perterritus, pulcher, Romanus, saevus, scelestus, solus, stultus, tristis, validus]
    elif adjList == 'describe':
        adjList = [alter, audax, bonus, celer, crudelis, diligens, felix, ferox, fidelis, fortis, gravis, infelix, ingens, iratus, laetus, lentus, magnus, malus, miser, novus, omnis, parvus, perterritus, pulcher, saevus, scelestus, solus, stultus, tristis, validus]
    if number == 1:
        latinAdj = [i for i in adjList if 'number' not in i.irregular][randint(0, len([i for i in adjList if 'number' not in i.irregular]) - 1)]
    else:
        latinAdj = adjList[randint(0, len(adjList) - 1)]
    englishAdj = EnglishAdjectives[LatinAdjectives.index(latinAdj)]
    if 'missing' in latinAdj.irregular:
        if 'superlative' in latinAdj.irregular['missing']:
            adjType = 1
        else:
            adjType = randint(1,2)
    else:
        adjType = randint(1,3)
    return latinAdj.Decline(adjType, number, gender, case) + ' ', englishAdj.Decline(adjType) + ' ', [englishAdj.position, type(englishAdj.stem) == list and adjType == 3]

def Adverb(advList=LatinAdverbs):
    latinAdv = advList[randint(0, len(advList) - 1)]
    englishAdv = EnglishAdverbs[LatinAdverbs.index(latinAdv)]
    if isinstance(latinAdv, LatinAdverb) and type(latinAdv.stem) == str:
        advType = 1
    else:
        advType = randint(1,6)
        if advType > 3:
            advType = 1
    return latinAdv.AdverbDecline(advType) + ' ', englishAdv.AdverbDecline(advType) + ' ', englishAdv.position


def Verb():
    latinVerb = LatinVerbs[randint(0, len(LatinVerbs) - 1)]
    person = randint(1,8)
    if person == 8:
        person = 6
    elif person == 7:
        person = 3
    return latinVerb, person
    
def ConjugateVerb(conLatinVerb, conjugatePerson, conjugateGender):
    conEnglishVerb = EnglishVerbs[LatinVerbs.index(conLatinVerb)]
    if randint(1,4) == 1 and conLatinVerb.stem not in ['vole', 'nole', 'sci', 'nesci', 'abse', 'adse']:
        status = False
    else:
        status = True
    if conLatinVerb.stem == 'coep':
        tense = choice([9, 12])
    elif isinstance(conLatinVerb, DeponentVerb) or isinstance(conLatinVerb, SemiDeponentVerb) or 'personPassive' not in conLatinVerb.usage or 'objectPassive' not in conLatinVerb.usage:
        if isinstance(conEnglishVerb, PerfectVerb):
            tense = choice([2, 9, 12, 16])
        else:
            tense = choice([2, 5, 9, 12, 16])
    else:
        tense = choice([2, 3, 5, 6, 9, 10, 12, 13, 16, 17])
    if tense == 2:
        conLatinVerb = conLatinVerb.PresentActive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PresentActive(conjugatePerson, status)
    elif tense == 3:
        conLatinVerb = conLatinVerb.PresentPassive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PresentPassive(conjugatePerson, status)
    elif tense == 5:
        conLatinVerb = conLatinVerb.ImperfectActive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.ImperfectActive(conjugatePerson, status)
    elif tense == 6:
        conLatinVerb = conLatinVerb.ImperfectPassive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.ImperfectPassive(conjugatePerson, status)
    elif tense == 9:
        conLatinVerb = conLatinVerb.PerfectActive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PerfectActive(conjugatePerson, status)
    elif tense == 10:
        conLatinVerb = conLatinVerb.PerfectPassive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PerfectPassive(conjugatePerson, status)
    elif tense == 12:
        conLatinVerb = conLatinVerb.PluperfectActive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PluperfectActive(conjugatePerson, status)
    elif tense == 13:
        conLatinVerb = conLatinVerb.PluperfectPassive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.PluperfectPassive(conjugatePerson, status)
    elif tense == 16:
        conLatinVerb = conLatinVerb.FutureActive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.FutureActive(conjugatePerson, status)
    elif tense == 17:
        conLatinVerb = conLatinVerb.FuturePassive(conjugatePerson, conjugateGender)
        conEnglishVerb = conEnglishVerb.FuturePassive(conjugatePerson, status)
    if not status:
        conLatinVerb = 'non ' + conLatinVerb
    return conLatinVerb + ' ', conEnglishVerb + ' ', tense, status

def Accusative(accLatinVerb):
    if 'accPerson' in accLatinVerb.usage:
        decAccLatin = [i for i in LatinNouns if 'person' in i.info['category']][randint(0, len([i for i in LatinNouns if 'person' in i.info['category']]) - 1)]
    elif 'accObject' in accLatinVerb.usage:
        decAccLatin = [i for i in LatinNouns if 'object' in i.info['category']][randint(0, len([i for i in LatinNouns if 'object' in i.info['category']]) - 1)]
    else:
        decAccLatin = [i for i in LatinNouns if 'abstract' not in i.info['category'] and 'time' not in i.info['category']][randint(0, len([i for i in LatinNouns if 'abstract' not in i.info['category'] and 'time' not in i.info['category']]) - 1)]
    decAccEnglish = EnglishNouns[LatinNouns.index(decAccLatin)]
    accusativeGender = decAccLatin.gender
    if 'number' in decAccLatin.info:
        accusativeNumber = decAccLatin.info['number']
    accusativeNumber = randint(1,2)
    if randint(1,2) == 1:
        latAccAdj, englishAccAdj, adjInfo = Adjective(accusativeNumber, decAccLatin.gender, 3, decAccLatin.info['adjective'])
    else:
        latAccAdj = englishAccAdj = ''
        adjInfo = ['', False]
    englishAccArticle, decAccEnglish = decAccEnglish.Decline(accusativeNumber, 3)
    if adjInfo[1]:
        englishAccArticle = 'the '
    elif englishAccArticle == 'an ' and latAccAdj != '':
        englishAccArticle = 'a '
    if 'adjReplace' in adjInfo[0]:
        englishAcc = englishAccAdj + decAccEnglish + ' '
    elif 'adjBefore' in adjInfo[0]:
        englishAcc = englishAccAdj + englishAccArticle + decAccEnglish + ' '
    else:
        englishAcc = englishAccArticle + englishAccAdj + decAccEnglish + ' '
        
        
    return latAccAdj + decAccLatin.Decline(accusativeNumber, 3) + ' ', englishAcc, accusativeNumber, accusativeGender


def Dative(datLatinVerb):
    if 'person' in datLatinVerb.usage:
        decDatLatin = [i for i in LatinNouns if 'person' in i.info['category']][randint(0, len([i for i in LatinNouns if 'person' in i.info['category']]) - 1)]
    else:
        decDatLatin = [i for i in LatinNouns if 'abstract' not in i.info['category'] and 'time' not in i.info['category']][randint(0, len([i for i in LatinNouns if 'abstract' not in i.info['category'] and 'time' not in i.info['category']]) - 1)]
    decDatEnglish = EnglishNouns[LatinNouns.index(decDatLatin)]
    datGender = decDatLatin.gender
    if 'number' in decDatLatin.info:
        datNumber = decDatLatin.info['number']
    else:
        datNumber = randint(1,2)
    if randint(1,2) == 1:
        latDatAdj, englishDatAdj, adjInfo = Adjective(datNumber, datGender, 5, decDatLatin.info['adjective'])
    else:
        latDatAdj = englishDatAdj = ''
        adjInfo = ['', False]
    englishDatArticle, decDatEnglish = decDatEnglish.Decline(datNumber, 5)
    if adjInfo[1]:
        englishDatArticle = 'the '
    elif englishDatArticle == 'an ' and latDatAdj != '':
        englishDatArticle = 'a '
    if 'adjReplace' in adjInfo[0]:
        englishDat = englishDatAdj + decDatEnglish + ' '
    elif 'adjBefore' in adjInfo[0]:
        englishDat = englishDatAdj + englishDatArticle + decDatEnglish + ' '
    else:
        englishDat = englishDatArticle + englishDatAdj + decDatEnglish + ' '
    
    
    return latDatAdj + decDatLatin.Decline(datNumber, 5) + ' ', englishDat

def Infinitive(infNumber, infGender, infCase, infStatus):
    conLatinInf = [i for i in LatinVerbs if 'infinitive' not in i.usage][randint(0, len([i for i in LatinVerbs if 'infinitive' not in i.usage]) - 1)]
    conEnglishInf = EnglishVerbs[LatinVerbs.index(conLatinInf)]
    if conLatinInf.stem == 'coep':
        infTense = randint(2,3)
    elif conLatinInf.stem in ['male', 'nole', 'posse', 'vole']:
        infTense = randint(1,2)
    elif isinstance(conLatinInf, DeponentVerb) or isinstance(conLatinInf, SemiDeponentVerb) or ('personPassive' not in conLatinInf.usage and 'objectPassive' not in conLatinInf.usage):
        infTense = randint(1,4)
        if infTense > 3:
            infTense = 1
    else:
        infTense = randint(1,10)
        if infTense > 6:
            infTense = 1
    if not infStatus or conLatinInf.stem in ['vole', 'nole', 'sci', 'nesci']:
        infStatus = 1
    else:
        infStatus = randint(0,3)
    if ('needsAccusative' in conLatinInf.usage or (('accPerson' in conLatinInf.usage or 'accObject' in conLatinInf.usage) and randint(1,2) == 1)) and infTense < 4:
        
        infDecLatinAcc, infDecEnglishAcc, infAccNumber, infAccGender = Accusative(conLatinInf)
    else:
        infDecLatinAcc = infDecEnglishAcc = ''
    if 'dative' in conLatinInf.usage:
        infDecDatLatin, infDecDatEnglish = Dative(conLatinInf)
    else:
        infDecDatLatin = infDecDatEnglish = ''
    if 'adjective' in conLatinInf.usage:
        infLatinAdj, infEnglishAdj, infAdjInfo = Adjective(infNumber, infGender, infCase, 'person')
        if infAdjInfo[1]:
            infEnglishAdj = 'the ' + infEnglishAdj
    else:
        infLatinAdj = infEnglishAdj = infAdjInfo = ''
    conEnglishInf = conEnglishInf.Infinitive(infTense, infStatus) + ' ' + infDecEnglishAcc + infDecDatEnglish + infEnglishAdj
    if infStatus:
        infStatus = ''
    else:
        infStatus = 'non '
    conLatinInf = infStatus + conLatinInf.Infinitive(infTense, infNumber, infGender) + ' ' + infDecLatinAcc + infDecDatLatin + infLatinAdj
    return conLatinInf, conEnglishInf

def Phrase():
    phraseLatinVerb, nomPerson = Verb()
    
    phraseDecLatinNom, phraseDecEnglishNom, nomGender = Nominative(nomPerson)
    
    phraseConLatinVerb, phraseConEnglishVerb, phraseTense, phraseStatus = ConjugateVerb(phraseLatinVerb, nomPerson, nomGender)
    
    if len(phraseLatinVerb.preposition) > 0 and randint(1,2) == 1 :
        phraseLatinPrep, phraseEnglishPrep = PrepositionalPhrase(phraseLatinVerb)
    else:
        phraseLatinPrep = phraseEnglishPrep = ''

    
    if ('needsAccusative' in phraseLatinVerb.usage or (('accPerson' in phraseLatinVerb.usage or 'accObject' in phraseLatinVerb.usage) and randint(1,2) == 1)) and phraseTense not in [3, 6, 8, 10, 13, 17]:
        phraseDecLatinAcc, phraseDecEnglishAcc, accNumber, accGender = Accusative(phraseLatinVerb)
    else:
        phraseDecLatinAcc = phraseDecEnglishAcc = ''

    if 'infinitive' in phraseLatinVerb.usage:
        if phraseDecLatinAcc == '':
            phraseConLatinInf, phraseConEnglishInf = Infinitive((nomPerson - 1) // 3 + 1, nomGender, 1, phraseStatus)
        else:
            phraseConLatinInf, phraseConEnglishInf = Infinitive(accNumber, accGender, 3, phraseStatus)
    else:
        phraseConLatinInf = phraseConEnglishInf = ''

    if 'dative' in phraseLatinVerb.usage:
        phraseDecDatLatin, phraseDecDatEnglish = Dative(phraseLatinVerb)
    else:
        phraseDecDatLatin = phraseDecDatEnglish = ''

    if 'adjective' in phraseLatinVerb.usage:
        phraseLatinAdj, phraseEnglishAdj, phraseAdjInfo = Adjective((nomPerson - 1) // 3 + 1, nomGender, 1, 'person')
        if phraseAdjInfo[1]:
            phraseEnglishAdj = 'the ' + phraseEnglishAdj
    else:
        phraseLatinAdj = phraseEnglishAdj = phraseAdjInfo = ''

    if randint(1,2) == 1:
        phraseLatinAdv, phraseEnglishAdv, phraseAdvPosition = Adverb(phraseLatinVerb.adverb)
        if 'advAfter' in phraseAdvPosition:
            phraseEnglishVerbClause = phraseDecEnglishNom + phraseConEnglishVerb + phraseDecEnglishAcc + phraseEnglishAdv
        elif 'advStart' in phraseAdvPosition:
            phraseEnglishVerbClause = phraseEnglishAdv + phraseDecEnglishNom + phraseConEnglishVerb + phraseDecEnglishAcc
        else:
            phraseEnglishVerbClause = phraseDecEnglishNom + phraseEnglishAdv + phraseConEnglishVerb + phraseDecEnglishAcc
    else:
        phraseLatinAdv = ''
        phraseEnglishVerbClause = phraseDecEnglishNom + phraseConEnglishVerb + phraseDecEnglishAcc

    LatinSentence = phraseLatinPrep + phraseDecLatinNom + phraseDecLatinAcc + phraseDecDatLatin + phraseLatinAdj + phraseLatinAdv + phraseConLatinVerb + phraseConLatinInf
    EnglishSentence =  phraseEnglishVerbClause + phraseEnglishAdj + phraseDecDatEnglish + phraseConEnglishInf + phraseEnglishPrep
    EnglishSentence = EnglishSentence[0].upper() + EnglishSentence[1:-1] + '.'
    return LatinSentence, EnglishSentence
for i in range(0,10):
    x, y = Phrase()
    print(x + '\n' + y)

