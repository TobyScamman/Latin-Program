import copy
class LatinNoun():
    def __init__(self, dec, gender, stem, irregular, info):
        self.dec = dec
        self.gender = gender
        self.stem = stem
        if type(self.stem) == str and dec == 2:
            if gender == 2:
                self.stem = (self.stem + 'us', self.stem)
            else:
                self.stem = (self.stem + 'um', self.stem)
        self.irregular = irregular
        self.info = info

    def Decline(self, number, case):
        if type(self.stem) == str:
            TempVerb = TempStem = self.stem
        else:
            TempVerb, TempStem = self.stem
        if 'dec' in self.irregular:
            return self.irregular['dec'][case + (number - 1) * 6]
        elif self.dec == 1 and number == 1:
            if case == 1:
                return f'{TempStem}a'
            elif case == 2:
                return f'{TempStem}a'
            elif case == 3:
                return f'{TempStem}am'
            elif case == 4:
                return f'{TempStem}ae'
            elif case == 5:
                return f'{TempStem}ae'
            elif case == 6:
                return f'{TempStem}a'
        elif self.dec == 1 and number == 2:
            if case == 1:
                return f'{TempStem}ae'
            elif case == 2:
                return f'{TempStem}ae'
            elif case == 3:
                return f'{TempStem}as'
            elif case == 4:
                return f'{TempStem}arum'
            elif case == 5:
                return f'{TempStem}is'
            elif case == 6:
                return f'{TempStem}is'
        elif self.dec == 2 and number == 1:
            if case == 1:
                return f'{TempVerb}'
            elif case == 2:
                if TempStem[0][-2:] == 'us':
                    return f'{TempStem}e'
                else:
                    return f'{TempVerb}'
            elif case == 3:
                return f'{TempStem}um'
            elif case == 4:
                return f'{TempStem}i'
            elif case == 5:
                return f'{TempStem}o'
            elif case == 6:
                return f'{TempStem}o'
        elif self.dec == 2 and number == 2:
            if case == 1:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}i'
            elif case == 2:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}i'
            elif case == 3:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}os'
            elif case == 4:
                return f'{TempStem}orum'
            elif case == 5:
                return f'{TempStem}is'
            elif case == 6:
                return f'{TempStem}is'
        elif self.dec == 3 and number == 1:
            if case == 1:
                return TempVerb
            elif case == 2:
                return TempVerb
            elif case == 3:
                if self.gender == 3:
                    return TempVerb
                else:
                    return f'{TempStem}em'
            elif case == 4:
                return f'{TempStem}is'
            elif case == 5:
                return f'{TempStem}i'
            elif case == 6:
                return f'{TempStem}e'
        elif self.dec == 3 and number == 2:
            if case == 1:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}es'
            elif case == 2:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}es'
            elif case == 3:
                if self.gender == 3:
                    return f'{TempStem}a'
                else:
                    return f'{TempStem}es'
            elif case == 4:
                return f'{TempStem}um'
            elif case == 5:
                return f'{TempStem}ibus'
            elif case == 6:
                return f'{TempStem}ibus'
        elif self.dec == 4 and number == 1:
            if case == 1:
                return f'{TempStem}us'
            elif case == 2:
                return f'{TempStem}us'
            elif case == 3:
                return f'{TempStem}um'
            elif case == 4:
                return f'{TempStem}us'
            elif case == 5:
                return f'{TempStem}ui'
            elif case == 6:
                return f'{TempStem}u'
        elif self.dec == 4 and number == 2:
            if case == 1:
                return f'{TempStem}us'
            elif case == 2:
                return f'{TempStem}us'
            elif case == 3:
                return f'{TempStem}us'
            elif case == 4:
                return f'{TempStem}uum'
            elif case == 5:
                return f'{TempStem}ibus'
            elif case == 6:
                return f'{TempStem}ibus'
        elif self.dec == 5 and number == 1:
            if case == 1:
                return f'{TempStem}s'
            elif case == 2:
                return f'{TempStem}s'
            elif case == 3:
                return f'{TempStem}m'
            elif case == 4:
                return f'{TempStem}i'
            elif case == 5:
                return f'{TempStem}i'
            elif case == 6:
                return TempStem
        elif self.dec == 5 and number == 2:
            if case == 1:
                return f'{TempStem}s'
            elif case == 2:
                return f'{TempStem}s'
            elif case == 3:
                return f'{TempStem}s'
            elif case == 4:
                return f'{TempStem}rum'
            elif case == 5:
                return f'{TempStem}bus'
            elif case == 6:
                return f'{TempStem}bus'
        else:
            return ' Oh Dear! '

class EnglishNoun():
    def __init__(self, stem, irregular, info):
        self.stem = stem
        self.irregular = irregular
        self.info = info
        if 'plural' not in self.irregular:
            if self.stem[-2:] == 'ey':
                self.irregular['plural'] = f'{self.stem[:-2]}ies'
            elif self.stem[-1] == 'y' and self.stem[-2] not in ('a', 'i', 'o', 'u'):
                self.irregular['plural'] = f'{self.stem[:-1]}ies'
            else:
                self.irregular['plural'] = f'{self.stem}s'

    def Decline(self, number, case):
        if number == 2 and self.info['article'] == 'a':
            tempArticle = 'the '
        elif self.info['article'] == '':
            tempArticle = ''
        else:
            tempArticle = self.info['article'] + ' '
        
        if case == 2:
            tempArticle = ''
        elif case == 4:
            tempArticle = 'of ' + tempArticle 
        elif case == 5:
            tempArticle = 'to ' + tempArticle
        elif case == 6:
            tempArticle = 'with ' + tempArticle
        if number == 1:
            return tempArticle, self.stem
        elif number == 2:
            return tempArticle, self.irregular["plural"]
class LatinVerb():
    def __init__(self, con, stem, irregular, usage, preposition, adverb):
        self.con = con
        self.stem = stem
        self.irregular = irregular
        self.usage = usage
        self.preposition = preposition
        self.adverb = adverb
        if 'imperfect' not in self.irregular and self.con == 4:
            self.irregular['imperfect'] = self.stem + 'eba'
        elif 'imperfect' not in self.irregular:
            self.irregular['imperfect'] = self.stem + 'ba'
        if 'perfect' not in self.irregular:
            self.irregular['perfect'] = self.stem + 'v'
        if 'fourth' not in self.irregular:
            self.irregular['fourth'] = self.stem + 't'
        if self.con < 3 and 'future' not in self.irregular:
            self.irregular['future'] = self.stem + 'b'

    def Infinitive(self, tense, number, gender):
        if number == 1 and gender == 1:
            ending = 'a'
        elif number == 1:
            ending = 'um'
        elif gender == 1:
            ending = 'as'
        elif gender == 2:
            ending = 'os'
        else:
            ending = 'a'
            
        if 'infinitive' in self.irregular:
            return self.irregular['infinitive'][tense - 1]
        elif tense == 1:
            return f'{self.stem}re'
        elif tense == 2:
            if type(self.irregular['perfect']) == list:
                return f'{self.irregular["perfect"][0]}sse'
            return f'{self.irregular["perfect"]}isse'
        elif tense == 3:
            return f'{self.irregular["fourth"] + "ur" + ending} esse'
        elif tense == 4 and self.con == 3:
            return f'{self.stem[:-1]}i'
        elif tense == 4:
            return f'{self.stem}ri'
        elif tense == 5:
            return f'{self.irregular["fourth"] + ending} esse'
        elif tense == 6:
            return f'{self.irregular["fourth"] + ending} iri'
             
    def PresentActive(self, person, gender):
        if 'present' in self.irregular:
            return self.irregular["present"][person - 1]
        elif person == 1 and (self.con == 1 or self.con == 3):
            return f'{self.stem[0:-1]}o'
        elif person == 1:
            return f'{self.stem}o'
        elif person == 2 and self.con == 3:
            return f'{self.stem[0:-1]}is'
        elif person == 2:
            return f'{self.stem}s'
        elif person == 3 and self.con == 3:
            return f'{self.stem[0:-1]}it'
        elif person == 3:
            return f'{self.stem}t'
        elif person == 4 and self.con == 3:
            return f'{self.stem[0:-1]}imus'
        elif person == 4:
            return f'{self.stem}mus'
        elif person == 5 and self.con == 3:
            return f'{self.stem[0:-1]}itis'
        elif person == 5:
            return f'{self.stem}tis'
        elif person == 6 and self.con == 3:
            return f'{self.stem[0:-1]}iunt'
        elif person == 6:
            return f'{self.stem}nt'
        
    def PresentPassive(self, person, gender):
        if 'presentPassive' in self.irregular:
            return self.irregular["presentPassive"][person -1]
        if person == 1 and (self.con == 1 or self.con == 3):
            return f'{self.stem[0:-1]}or'
        elif person == 1:
            return f'{self.stem}or'
        elif person == 2:
            return f'{self.stem}ris'
        elif person == 3 and self.con == 3:
            return f'{self.stem[0:-1]}itur'
        elif person == 3:
            return f'{self.stem}tur'
        elif person == 4 and self.con == 3:
            return f'{self.stem[0:-1]}imur'
        elif person == 4:
            return f'{self.stem}mur'
        elif person == 5 and self.con == 3:
            return f'{self.stem[0:-1]}imini'
        elif person == 5:
            return f'{self.stem}mini'
        elif person == 6 and self.con == 3:
            return f'{self.stem[0:-1]}untur'
        elif person == 6:
            return f'{self.stem}ntur'

    def PresentParticiple(self, number, gender, case):
        if 'presentParticiple' in self.irregular:
            TempStem = self.irregular['presentParticiple']
        else:
            TempStem = self.stem
        if self.con == 4:
            TempStem += 'e'
        if number == 2 and case == 4:
            return f'{TempStem}ntium'
        elif gender == 3 and 0 < case < 4:
            if 'presentParticipleVerb' in self.irregular:
                verb = self.irregular['presentParticipleVerb']
            else:
                verb = f'{TempStem}ns'
            stem = f'{TempStem}nti'
            return f'{LatinNoun(3, 3, (verb, stem), {}, {}).Decline(number, case)}'
        else:
            if 'presentParticipleVerb' in self.irregular:
                verb = self.irregular['presentParticipleVerb']
            else:
                verb = f'{TempStem}ns'
            stem = f'{TempStem}nt'
            return f'{LatinNoun(3, 2, (verb, stem), {}, {}).Decline(number, case)}'
        
    def ImperfectActive(self, person, gender):
        if person == 1:
            return f'{self.irregular["imperfect"]}m'
        elif person == 2:
            return f'{self.irregular["imperfect"]}s'
        elif person == 3:
            return f'{self.irregular["imperfect"]}t'
        elif person == 4:
            return f'{self.irregular["imperfect"]}mus'
        elif person == 5:
            return f'{self.irregular["imperfect"]}tis'
        elif person == 6:
            return f'{self.irregular["imperfect"]}nt'
        
    def ImperfectPassive(self, person, gender):
        if person == 1:
            return f'{self.irregular["imperfect"]}r'
        elif person == 2:
            return f'{self.irregular["imperfect"]}ris'
        elif person == 3:
            return f'{self.irregular["imperfect"]}tur'
        elif person == 4:
            return f'{self.irregular["imperfect"]}mur'
        elif person == 5:
            return f'{self.irregular["imperfect"]}mini'
        elif person == 6:
            return f'{self.irregular["imperfect"]}ntur'

    def ImperfectActiveSubjunctive(self, person, gender):
        if person == 1:
            return f'{self.Infinitive(1, 1, 2)}m'
        elif person == 2:
            return f'{self.Infinitive(1, 1, 2)}s'
        elif person == 3:
            return f'{self.Infinitive(1, 1, 2)}t'
        elif person == 4:
            return f'{self.Infinitive(1, 1, 2)}mus'
        elif person == 5:
            return f'{self.Infinitive(1, 1, 2)}tis'
        elif person == 6:
            return f'{self.Infinitive(1, 1, 2)}nt'

    def ImperfectPassiveSubjunctive(self, person, gender):
        if person == 1:
            return f'{self.Infinitive(1, 1, 2)}r'
        elif person == 2:
            return f'{self.Infinitive(1, 1, 2)}ris'
        elif person == 3:
            return f'{self.Infinitive(1, 1, 2)}tur'
        elif person == 4:
            return f'{self.Infinitive(1, 1, 2)}mur'
        elif person == 5:
            return f'{self.Infinitive(1, 1, 2)}mini'
        elif person == 6:
            return f'{self.Infinitive(1, 1, 2)}ntur'

    def PerfectActive(self, person, gender):
        if type(self.irregular['perfect']) == list:
            return self.irregular["perfect"][person]
        if person == 1:
            return f'{self.irregular["perfect"]}i'
        elif person == 2:
            return f'{self.irregular["perfect"]}isti'
        elif person == 3:
            return f'{self.irregular["perfect"]}it'
        elif person == 4:
            return f'{self.irregular["perfect"]}imus'
        elif person == 5:
            return f'{self.irregular["perfect"]}istis'
        elif person == 6:
            return f'{self.irregular["perfect"]}erunt'

    def PerfectPassive(self, person, gender):
        if person < 4 and gender == 1:
            ending = 'a'
        elif person < 4 and gender == 2:
            ending = 'us'
        elif person < 4 and gender == 3:
            ending = 'um'
        elif gender == 1:
            ending = 'ae'
        elif gender == 2:
            ending = 'i'
        else:
            ending = 'a'
        if person == 1:
            return f'{self.irregular["fourth"] + ending} sum'
        elif person == 2:
            return f'{self.irregular["fourth"] + ending} es'
        elif person == 3:
            return f'{self.irregular["fourth"] + ending} est'
        elif person == 4:
            return f'{self.irregular["fourth"] + ending} sumus'
        elif person == 5:
            return f'{self.irregular["fourth"] + ending} estis'
        elif person == 6:
            return f'{self.irregular["fourth"] + ending} sunt'

    def PerfectParticiple(self, number, gender, case):
        if gender == 1:
            return f'{LatinNoun(1, 1, self.irregular["fourth"], {}, {}).Decline(number, case)}'
        else:
            return f'{LatinNoun(2, gender, self.irregular["fourth"], {}, {}).Decline(number, case)}'

    def PluperfectActive(self, person, gender):
        if type(self.irregular['perfect']) == list:
            TempStem = self.irregular['perfect'][0]
        else:
            TempStem = self.irregular['perfect']
        
        if person == 1:
            return f'{TempStem}eram'
        elif person == 2:
            return f'{TempStem}eras'
        elif person == 3:
            return f'{TempStem}erat'
        elif person == 4:
            return f'{TempStem}eramus'
        elif person == 5:
            return f'{TempStem}eratis'
        elif person == 6:
            return f'{TempStem}erant'

    def PluperfectPassive(self, person, gender):
        if person < 4 and gender == 1:
            ending = 'a'
        elif person < 4 and gender == 2:
            ending = 'us'
        elif person < 4 and gender == 3:
            ending = 'um'
        elif gender == 1:
            ending = 'ae'
        elif gender == 2:
            ending = 'i'
        else:
            ending = 'a'
        if person == 1:
            return f'{self.irregular["fourth"] + ending} eram'
        elif person == 2:
            return f'{self.irregular["fourth"] + ending} eras'
        elif person == 3:
            return f'{self.irregular["fourth"] + ending} erat'
        elif person == 4:
            return f'{self.irregular["fourth"] + ending} eramus'
        elif person == 5:
            return f'{self.irregular["fourth"] + ending} eratis'
        elif person == 6:
            return f'{self.irregular["fourth"] + ending} erant'

    def PluperfectActiveSubjunctive(self, person, gender):
        if person == 1:
            return f'{self.Infinitive(2, 1, 2)}m'
        elif person == 2:
            return f'{self.Infinitive(2, 1, 2)}s'
        elif person == 3:
            return f'{self.Infinitive(2, 1, 2)}t'
        elif person == 4:
            return f'{self.Infinitive(2, 1, 2)}mus'
        elif person == 5:
            return f'{self.Infinitive(2, 1, 2)}tis'
        elif person == 6:
            return f'{self.Infinitive(2, 1, 2)}nt'

    def PluperfectPassiveSubjunctive(self, person, gender):
        if person < 4 and gender == 1:
            ending = 'a'
        elif person < 4 and gender == 2:
            ending = 'us'
        elif person < 4 and gender == 3:
            ending = 'um'
        elif gender == 1:
            ending = 'ae'
        elif gender == 2:
            ending = 'i'
        else:
            ending = 'a'
        if person == 1:
            return f'{self.irregular["fourth"] + ending} essem'
        elif person == 2:
            return f'{self.irregular["fourth"] + ending} esses'
        elif person == 3:
            return f'{self.irregular["fourth"] + ending} esset'
        elif person == 4:
            return f'{self.irregular["fourth"] + ending} essemus'
        elif person == 5:
            return f'{self.irregular["fourth"] + ending} essetis'
        elif person == 6:
            return f'{self.irregular["fourth"] + ending} essent'

    def FutureActive(self, person, gender):
        if self.con < 3:
            if person == 1:
                return f'{self.irregular["future"]}o'
            elif person == 2:
                return f'{self.irregular["future"]}is'
            elif person == 3:
                return f'{self.irregular["future"]}it'
            elif person == 4:
                return f'{self.irregular["future"]}imus'
            elif person == 5:
                return f'{self.irregular["future"]}itis'
            elif person == 6:
                return f'{self.irregular["future"]}unt'
        elif self.con > 2:
            TempStem = self.stem
            if self.con == 3:
                TempStem = self.stem[0:-1]
            if person == 1:
                return TempStem + 'am'
            elif person == 2:
                return TempStem + 'es'
            elif person == 3:
                return TempStem + 'et'
            elif person == 4:
                return TempStem + 'emus'
            elif person == 5:
                return TempStem + 'etis'
            elif person == 6:
                return TempStem + 'ent'

    def FuturePassive(self, person, gender):
        if self.con == 1 or self.con == 2:
            if person == 1:
                return f'{self.stem}bor'
            elif person == 2:
                return f'{self.stem}beris'
            elif person == 3:
                return f'{self.stem}bitur'
            elif person == 4:
                return f'{self.stem}bimur'
            elif person == 5:
                return f'{self.stem}bimini'
            elif person == 6:
                return f'{self.stem}buntur'
        elif self.con == 3 or self.con == 4:
            TempStem = self.stem
            if self.con == 3:
                TempStem = self.stem[0:-1]
            if person == 1:
                return TempStem + 'ar'
            elif person == 2:
                return TempStem + 'eris'
            elif person == 3:
                return TempStem + 'etur'
            elif person == 4:
                return TempStem + 'emur'
            elif person == 5:
                return TempStem + 'emini'
            elif person == 6:
                return TempStem + 'entur'

    def FutureParticiple(self, number, gender, case):
        TempStem = self.irregular["fourth"] + 'ur'
        if gender == 1:
            return f'{LatinNoun(1, 1, TempStem, {}, {}).Decline(number, case)}'
        else:
            return f'{LatinNoun(2, gender, TempStem, {}, {}).Decline(number, case)}'

    def Imperative(self, number):
        if 'imperative' in self.irregular:
            return self.irregular['imperative'][number - 1]
        if number == 1:
            return f'{self.stem}'
        elif self.con == 3:
            return f'{self.stem[:-1]}ite'
        else:
            return f'{self.stem}te'

    def GerundiveOfPurpose(self, number, gender):
        if 'presentParticiple' in self.irregular:
            TempStem = self.irregular['presentParticiple']
        else:
            TempStem = self.stem
        if self.con == 4:
            TempStem += 'end'
        else:
            TempStem += 'nd'
        if gender == 1:
            return f'{LatinNoun(1, 1, TempStem, {}, {}).Decline(number, 3)}'
        else:
            return f'{LatinNoun(2, gender, TempStem, {}, {}).Decline(number, 3)}'
        

        

class DeponentVerb(LatinVerb):
    def Infinitive(self, tense, number, gender):
        if number == 1 and gender == 1:
            ending = 'a'
        elif number == 1:
            ending = 'um'
        elif gender == 1:
            ending = 'as'
        elif gender == 2:
            ending = 'os'
        else:
            ending = 'a'
            
        if tense == 1 and self.con == 3 and self.stem[-2] == 'i':
            return f'{self.stem[:-1]}'
        elif tense == 1 and self.con == 3:
            return f'{self.stem[:-1]}i'
        elif tense == 1:
            return f'{self.stem}ri'
        elif tense == 2:
            return f'{self.irregular["fourth"] + ending} esse'
        elif tense == 3:
            return f'{self.irregular["fourth"] + "ur" + ending} esse'
        elif tense == 4 and self.stem[-2] == 'i':
            return f'{self.stem[:-2]}ere'
        elif tense == 4:
            return f'{self.stem}re'
        
        
        
    def PresentActive(self, person, gender):
        if person == 1 and self.con == 2:
            return f'{self.stem}or'
        elif person == 1:
            return f'{self.stem[:-1]}or'
        elif person == 2 and self.con == 3:
            return f'{self.stem[0:-2]}eris'
        elif person == 2:
            return f'{self.stem}ris'
        elif person == 3 and self.con == 3 and self.stem[-2] == 'i':
            return f'{self.stem[0:-1]}tur'
        elif person == 3 and self.con == 3:
            return f'{self.stem[0:-1]}itur'
        elif person == 3:
            return f'{self.stem}tur'
        elif person == 4 and self.con == 3 and self.stem[-2] == 'i':
            return f'{self.stem[0:-1]}mur'
        elif person == 4 and self.con == 3:
            return f'{self.stem[0:-1]}imur'
        elif person == 4:
            return f'{self.stem}mur'
        elif person == 5 and self.con == 3 and self.stem[-2] == 'i':
            return f'{self.stem[0:-1]}mini'
        elif person == 5 and self.con == 3:
            return f'{self.stem[0:-1]}imini'
        elif person == 5:
            return f'{self.stem}mini'
        elif person == 6 and self.con == 3:
            return f'{self.stem[0:-1]}untur'
        elif person == 6:
            return f'{self.stem}ntur'
        

    def ImperfectActive(self, person, gender):
        return self.ImperfectPassive(person, gender)

    def ImperfectActiveSubjunctive(self, person, gender):
        if person == 1:
            return f'{self.Infinitive(4, 1, 2)}r'
        elif person == 2:
            return f'{self.Infinitive(4, 1, 2)}ris'
        elif person == 3:
            return f'{self.Infinitive(4, 1, 2)}tur'
        elif person == 4:
            return f'{self.Infinitive(4, 1, 2)}mur'
        elif person == 5:
            return f'{self.Infinitive(4, 1, 2)}mini'
        elif person == 6:
            return f'{self.Infinitive(4, 1, 2)}ntur'

    def PerfectActive(self, person, gender):
        return self.PerfectPassive(person, gender)

    def PluperfectActive(self, person, gender):
        return self.PluperfectPassive(person, gender)
    
    def PluperfectActiveSubjunctive(self, person, gender):
        return self.PluperfectPassiveSubjunctive(person, gender)

    def FutureActive(self, person, gender):
        return self.FuturePassive(person, gender)

    def Imperative(self, number):
        if number == 1:
            return self.Infinitive(4, 1, 2)
        elif self.con == 3 and self.stem[-2] == 'i':
            return f'{self.stem[:-1]}mini'
        elif self.con == 3:
            return f'{self.stem[:-1]}imini'
        else:
            return f'{self.stem}mini'

class SemiDeponentVerb(LatinVerb):
    def Infinitive(self, tense, number, gender):
        if number == 1 and gender == 1:
            ending = 'a'
        elif number == 1:
            ending = 'um'
        elif gender == 1:
            ending = 'as'
        elif gender == 2:
            ending = 'os'
        else:
            ending = 'a'

        if tense == 1:
            return f'{self.stem}re'
        elif tense == 2:
            return f'{self.irregular["fourth"] + ending} esse'
        elif tense == 3:
            return f'{self.irregular["fourth"] + "ur" + ending} esse'
        elif tense == 4:
            return f'{self.stem}re'

    def ImperfectActiveSubjunctive(self, person, gender):
        if person == 1:
            return f'{self.Infinitive(4, 1, 2)}m'
        elif person == 2:
            return f'{self.Infinitive(4, 1, 2)}s'
        elif person == 3:
            return f'{self.Infinitive(4, 1, 2)}t'
        elif person == 4:
            return f'{self.Infinitive(4, 1, 2)}mus'
        elif person == 5:
            return f'{self.Infinitive(4, 1, 2)}tis'
        elif person == 6:
            return f'{self.Infinitive(4, 1, 2)}nt'
    def PerfectActive(self, person, gender):
        return self.PerfectPassive(person, gender)

    def PluperfectActive(self, person, gender):
        return self.PluperfectPassive(person, gender)

    def PluperfectActiveSubjunctive(self, person, gender):
        return self.PluperfectPassiveSubjunctive(person, gender)

class LatinPreposition():
    def __init__(self, prep, case, subjects):
        self.prep = prep
        self.case = case
        self.subjects = subjects

class EnglishPreposition():
    def __init__(self, prep):
        self.prep = prep




        

class EnglishVerb():
    def __init__(self, stem, irregular):
        self.stem = stem
        self.irregular = irregular
        if 'perfect' not in irregular:
            if self.stem[-1] == 'y':
                self.irregular['perfect'] = stem[:-1] + 'ied'
            elif self.stem[-1] == 'e':
                self.irregular['perfect'] = stem + 'd'
            else:
                self.irregular['perfect'] = stem + 'ed'
        if 'presentParticiple' not in irregular:
            if self.stem[-1] == 'n':
                self.irregular['presentParticiple'] = stem + stem[-1] + 'ing'
            elif self.stem[-2:] == 'ie':
                self.irregular['presentParticiple'] = stem[:-2] + 'ying'
            elif self.stem[-1] == 'e':
                self.irregular['presentParticiple'] = stem[:-1] + 'ing'
            else:
                self.irregular['presentParticiple'] = stem + 'ing'
        if 'perfectParticiple' not in irregular:
            self.irregular['perfectParticiple'] = self.irregular['perfect']
        if 'after' not in irregular:
            self.irregular['after'] = ''

    def Infinitive(self, tense, status):
        if status:
            if tense == 1:
                return f'to {self.stem}{self.irregular["after"]}'
            elif tense == 2:
                return f'to have {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 3:
                return f'to be about to {self.stem}{self.irregular["after"]}'
            if tense == 4:
                return f'to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif tense == 5:
                return f'to have been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 6:
                return f'to be about to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            if tense == 1:
                return f'to not {self.stem}{self.irregular["after"]}'
            elif tense == 2:
                return f'to have not {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 3:
                return f'to not be about to {self.stem}{self.irregular["after"]}'
            if tense == 4:
                return f'to not be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif tense == 5:
                return f'to have not been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 6:
                return f'to not be about to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        
    def PresentActive(self, person, status):
        if person == 1:
            return f'am {self.PresentParticiple(status)}'
        elif person == 3:
            return f'is {self.PresentParticiple(status)}'
        else:
            return f'are {self.PresentParticiple(status)}'

    def PresentPassive(self, person, status):
        if status:
            if person == 1:
                return f'am being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif person == 3:
                return f'is being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'are being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            if person == 1:
                return f'I am not being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif person == 3:
                return f'is not being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'are not being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        
    def PresentParticiple(self, status):
        if status:
            return f'{self.irregular["presentParticiple"]}{self.irregular["after"]}'
        else:
            return f'not {self.irregular["presentParticiple"]}{self.irregular["after"]}'

    def ImperfectActive(self, person, status):
        if person == 1 or person == 3:
            return f'was {self.PresentParticiple(status)}'
        else:
            return f'were {self.PresentParticiple(status)}'

    def ImperfectPassive(self, person, status):
        if status:
            if person or person == 3:
                return f'was being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'were being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            if person == 1 or person == 3:
                return f'was not being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'were not being {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def PerfectActive(self, person, status):
        if status:
            return f'{self.irregular["perfect"]}{self.irregular["after"]}'
        else:
            return f'did not {self.stem}{self.irregular["after"]}'

    def PerfectPassive(self, person, status):
        if status:
            if person == 1 or person == 3:
                return f'was {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'were {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            if person == 1 or person == 3:
                return f'was not {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            else:
                return f'were not {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def PerfectPassiveParticiple(self, status):
        if status:
            return f'having been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'having not been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def PluperfectActive(self, person, status):
        if status:
            return f'had {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'had not {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            

    def PluperfectPassive(self, person, status):
        if status:
            return f'had been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'had not been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def FutureActive(self, person, status):
        if status:
            return f'will {self.stem}{self.irregular["after"]}'
        else:
            return f'will not {self.stem}{self.irregular["after"]}'

    def FuturePassive(self, person, status):
        if status:
            return f'will be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'will not be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            
    def FutureParticiple(self, status):
        if status:
            return f'about to {self.stem}{self.irregular["after"]}'
        else:
            return f'about to not {self.stem}{self.irregular["after"]}'
        
    def Imperative(self, status):
        if status:
            return f'{self.stem}{self.irregular["after"]}'
        else:
            return f'do not {self.stem}{self.irregular["after"]}'


class PerfectVerb(EnglishVerb):
    def __init__(self, stem, irregular):
        self.stem = stem
        self.irregular = irregular
        if 'perfect' not in irregular:
            if self.stem[-1] == 'y':
                self.irregular['perfect'] = stem[:-1] + 'ied'
            elif self.stem[-1] == 'e':
                self.irregular['perfect'] = stem + 'd'
            else:
                self.irregular['perfect'] = stem + 'ed'
        if 'presentParticiple' not in irregular:
            if self.stem[-1] == 'n':
                self.irregular['presentParticiple'] = stem + stem[-1] + 'ing'
            elif self.stem[-2:] == 'ie':
                self.irregular['presentParticiple'] = stem[:-2] + 'ying'
            elif self.stem[-1] == 'e':
                self.irregular['presentParticiple'] = stem[:-1] + 'ing'
            else:
                self.irregular['presentParticiple'] = stem + 'ing'
        if 'perfectParticiple' not in irregular:
            self.irregular['perfectParticiple'] = self.irregular['perfect']
        if 'after' not in irregular:
            self.irregular['after'] = ''
        if 'status' in self.irregular:
            status = self.irregular['status']

    def Infinitive(self, tense, status):
        if status:
            if tense == 1:
                return f'to {self.stem}{self.irregular["after"]}'
            elif tense == 2:
                return f'to have {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 3:
                return f'to be about to {self.stem}{self.irregular["after"]}'
            if tense == 4:
                return f'to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif tense == 5:
                return f'to have been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 6:
                return f'to be about to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            if tense == 1:
                return f'to not {self.stem}{self.irregular["after"]}'
            elif tense == 2:
                return f'to not have {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 3:
                return f'to not be about to {self.stem}{self.irregular["after"]}'
            if tense == 4:
                return f'to not be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            elif tense == 5:
                return f'to have not been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
            if tense == 6:
                return f'to not be about to be {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        
            
    def PresentActive(self, person, status):
        if 'present' in self.irregular:
            TempStem = self.irregular['present'][person - 1]
        else:
            TempStem = self.stem
        if status:
            if person == 3 and TempStem == self.stem:
                return f'{TempStem}s{self.irregular["after"]}'
            else:
                return f'{TempStem}{self.irregular["after"]}'
        else:
            if self.stem == 'be':
                return f'{TempStem} not{self.irregular["after"]}'
            else:
                if person == 3:
                    return f'does not {TempStem}{self.irregular["after"]}'
                else:
                    return f'do not {TempStem}{self.irregular["after"]}'

    def PresentParticiple(self, status):
        if status:
            return f'{self.irregular["presentParticiple"]}{self.irregular["after"]}'
        else:
            return f'not {self.irregular["presentParticiple"]}{self.irregular["after"]}'

    def ImperfectActive(self, person, status):
        if self.stem == 'be':
            return self.PerfectActive(person, status)
        if status:
            if person == 1 or person == 3:
                return f'was {self.irregular["presentParticiple"]}{self.irregular["after"]}'
            else:
                return f'were {self.irregular["presentParticiple"]}{self.irregular["after"]}'
        else:
            if person == 1 or person == 3:
                return f'was not {self.irregular["presentParticiple"]}{self.irregular["after"]}'
            else:
                return f'were not {self.irregular["presentParticiple"]}{self.irregular["after"]}'
        
    def PerfectActive(self, person, status):
        if status:
            if type(self.irregular['perfect']) == list:
                TempStem = self.irregular['perfect'][person - 1]
            else:
                TempStem = self.irregular['perfect']
            return f'{TempStem}{self.irregular["after"]}'
        else:
            if type(self.irregular['perfect']) == list:
                TempStem = self.irregular['perfect'][person - 1]
            else:
                TempStem = self.stem
            if self.stem == 'be':
                return f'{TempStem} not{self.irregular["after"]}'
            else:
                return f'did not {TempStem}{self.irregular["after"]}'

    def PerfectPassiveParticiple(self, status):
        if status:
            return f'having been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'having not been {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def PluperfectActive(self, person, status):
        if status:
            return f'had {self.irregular["perfectParticiple"]}{self.irregular["after"]}'
        else:
            return f'had not {self.irregular["perfectParticiple"]}{self.irregular["after"]}'

    def FutureActive(self, person, status):
        if status:
            return f'will {self.stem}{self.irregular["after"]}'
        else:
            return f'will not {self.stem}{self.irregular["after"]}'

    def FutureParticiple(self, status):
        if status:
            return f'about to {self.stem}{self.irregular["after"]}'
        else:
            return f'not about to {self.stem}{self.irregular["after"]}'

    def Imperative(self, status):
        if status:
            return f'{self.stem}{self.irregular["after"]}'
        else:
            return f'do not {self.stem}{self.irregular["after"]}'

class LatinAdjective():
    def __init__(self, dec, stem, irregular={}):
        self.dec = dec
        self.stem = stem
        self.irregular = irregular

    def Decline(self, adjType, number, gender, case):
        if type(self.stem) == str:
            TempVerb = TempStem = self.stem
        else:
            TempVerb = self.stem[0]
            TempStem = self.stem[1]
        if self.dec == 0:
            return self.stem
        if adjType == 1:
            if type(self.stem) == list and len(self.stem) == 3:
                TempVerb = TempStem = self.stem[0]
            if self.dec == 3:
                if TempVerb == 'celer' and gender == 1 and case < 3 and number == 1:
                    return f'celeris'
                elif gender == 3 and case < 4 and number == 1 and (TempVerb[-2:] == 'is' or TempVerb == 'celer'):
                    return f'{TempStem}e'
                elif gender == 3 and case < 4 and number == 2:
                    return f'{TempStem}ia'
                elif case == 6 and number == 1:
                    return f'{TempStem}i'
                elif case == 4 and number == 2:
                    return f'{TempStem}ium'                
                return LatinNoun(3, gender, (TempVerb, TempStem), {}, {}).Decline(number, case)
            elif (TempVerb == 'tot' or TempVerb == 'null') and number == 1 and case == 4:
                return f'{TempVerb}ius'
            elif (TempVerb == 'tot' or TempVerb == 'null') and number == 1 and case == 5:
                return f'{TempVerb}i'
            elif type(self.stem) == list and len(self.stem) == 2 and gender == 2  and case < 3 and number == 1:
                return TempVerb
            return LatinNoun(gender // 2 + 1, gender, TempStem, {}, {}).Decline(number, case)
        elif adjType == 2:
            if type(self.stem) == list and len(self.stem) == 3:
                TempStem = self.stem[1]
            if TempStem == 'plus':
                if number == 1:
                    return LatinNoun(3, 3, ['plus', 'plur'], {}, {}).Decline(number, case)
                elif number == 2:
                    if case == 4:
                        return 'plurium'
                    return LatinNoun(3, gender, ['plus', 'plur'], {}, {}).Decline(number, case)
            elif gender == 3:
                if TempStem == 'min':
                    return LatinNoun(3, gender, ['minorius', 'minor'], {}, {}).Decline(number, case)                
                return LatinNoun(3, gender, [TempStem + 'ius', TempStem + 'ior'], {}, {}).Decline(number, case)
            elif TempStem == 'min':
                return LatinNoun(3, gender, [TempStem + 'or', TempStem + 'or'], {}, {}).Decline(number, case)                
            else:
                return LatinNoun(3, gender, [TempStem + 'ior', TempStem + 'ior'], {}, {}).Decline(number, case)
        else:
            if type(self.stem) == list and len(self.stem) == 3:
                TempStem = self.stem[2]
            elif TempVerb[-2:] == 'er':
                TempStem = TempVerb + 'rim'
            elif TempVerb[-4:] == 'ilis':
                TempStem = TempStem + 'lim'        
            else:
                TempStem += 'issim'
            if gender == 1:
                return LatinNoun(1, gender, TempStem, {}, {}).Decline(number, case)
            else:
                return LatinNoun(2, gender, TempStem, {}, {}).Decline(number, case)

    def AdverbDecline(self, advType):
        if 'adverb' in self.irregular:
            return self.irregular['adverb'][advType - 1]
        if type(self.stem) == str:
            TempVerb = TempStem = self.stem
        else:
            TempVerb = self.stem[0]
            TempStem = self.stem[1]
        if advType == 1:
            if self.dec == 3:
                return f'{TempStem}iter'
            else:
                return f'{TempStem}e'
        elif advType == 2:
            return f'{TempStem}ius'

        else:
            return self.Decline(3, 1, 2, 2)
            
            

class EnglishAdjective():
    def __init__(self, stem, position=['adjAfter', 'advAfter'], adverb=[]):
        self.stem = stem
        self.position = position
        if adverb == []:
            if type(self.stem) == str:
                self.adverb = self.stem
            else:
                self.adverb = self.stem[0]
        else:
            self.adverb = adverb
        
    def Decline(self, adjType):
        if type(self.stem) == list:
            return self.stem[adjType - 1]
        if adjType == 1:
            return self.stem
        elif adjType == 2:
            return f'more {self.stem}'
        elif adjType == 3:
            return f'very {self.stem}'

    def AdverbDecline(self, advType):
        if type(self.adverb) == list:
            return self.adverb[advType - 1]
        elif self.adverb[-1] == 'y':
            TempAdv = f'{self.adverb[:-1]}ily'
        elif self.adverb[-2:] == 'le':
            TempAdv = f'{self.adverb[:-1]}y'
        else:
            TempAdv = f'{self.adverb}ly' 
        if advType == 1:
            return TempAdv
        elif advType == 2:
            return 'more ' + TempAdv
        else:
            return 'very ' + TempAdv


class LatinAdverb():
    def __init__(self, stem):
        self.stem = stem

    def AdverbDecline(self, advType):
        if type(self.stem) == str:
            return self.stem
        else:
            return self.stem[advType - 1]

class EnglishAdverb():
    def __init__(self, stem, position=['advAfter']):
        self.stem = stem
        self.position = position

    def AdverbDecline(self, advType):
        if type(self.stem) == str:
            return self.stem
        else:
            return self.stem[advType - 1]
            
            
        

    
        
        
def PrintAll(word):
    if isinstance(word, LatinAdjective):
        for i in range(1,4):
            for j in range(1,4):
                for k in range(1,3):
                    for l in range(1,7):
                        print(word.Decline(i, k, j, l))
                print('')
    elif isinstance(word, LatinNoun):
        for i in range(1,3):
            for j in range(1,7):
                print(word.Decline(i,j))
    elif isinstance(word, DeponentVerb) or isinstance(word, SemiDeponentVerb) or (hasattr(word, 'usage') and ('personPassive' not in word.usage and 'objectPassive' not in word.usage)):
        for i in range(1,7):
            print(word.PresentActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PerfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.FutureActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectActiveSubjunctive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectActiveSubjunctive(i, 2))
        print('')
        for i in range(1,7):
            print(word.Infinitive(i, 1, 2))
        print('')
        for i in range(1,3):
            print(word.Imperative(i))
        print('')
        for i in range(1,3):
            for j in (1, 4, 5, 3, 6):
                print(word.PresentParticiple(i, 2, j))
        print('')
        for i in range(1,3):
            for j in (1, 4, 5, 3, 6):
                print(word.FutureParticiple(i, 2, j))
        print('')
        for i in range(1,3):
            for j in (1, 4, 5, 3, 6):
                print(word.PerfectParticiple(i, 2, j))
        print('')
        for i in range(1,3):
            print(word.GerundiveOfPurpose(i, 2))
        print('')
##    elif isinstance(word, PerfectVerb):   
##        for i in range(1,7):
##            print(word.PresentActive(i, True))
##        print('')
##        for i in range(1,7):
##            print(word.ImperfectActive(i, True))
##        print('')
##        for i in range(1,7):
##            print(word.PerfectActive(i, True))
##        print('')
##        for i in range(1,7):
##            print(word.PluperfectActive(i, True))
##        print('')
##        for i in range(1,7):
##            print(word.FutureActive(i, True))
##        print('')
##        for i in range(1,4):
##            print(word.Infinitive(i, True))
##        print('')
##        print(word.Imperative(True))
##        print('')
##        print(word.PresentParticiple(True))
##        print('')
##        print(word.FutureParticiple(True))
##        print('')
##        print(word.PerfectActiveParticiple(True))
##        print('')
    elif isinstance(word, EnglishVerb):
        for i in range(1,7):
            print(word.Infinitive(i, True))
        print('')
        for i in range(1,7):
            print(word.PresentActive(i, True))
        print('')
        for i in range(1,7):
            print(word.PresentPassive(i, True))
        print('')
        print(word.PresentParticiple(True))
        print('')
        for i in range(1,7):
            print(word.ImperfectActive(i, True))
        print('')
        for i in range(1,7):
            print(word.ImperfectPassive(i, True))
        print('')
        for i in range(1,7):
            print(word.PerfectActive(i, True))
        print('')
        for i in range(1,7):
            print(word.PerfectPassive(i, True))
        print('')
        print(word.PerfectPassiveParticiple(True))
        print('')
        for i in range(1,7):
            print(word.PluperfectActive(i, True))
        print('')
        for i in range(1,7):
            print(word.PluperfectPassive(i, True))
        print('')
        for i in range(1,7):
            print(word.FutureActive(i, True))
        print('')
        for i in range(1,7):
            print(word.FuturePassive(i, True))
        print('')
        print(word.FutureParticiple(True))
        print('')
        print(word.Imperative(True))
        print('')

        
    else:
        for i in range(1,7):
            print(word.PresentActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PerfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.FutureActive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectActiveSubjunctive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectActiveSubjunctive(i, 2))
        print('')
        for i in range(1,7):
            print(word.Infinitive(i, 1, 2))
        print('')
        for i in range(1,3):
            print(word.Imperative(i))
        print('')
        for i in range(1,7):
            print(word.PresentPassive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectPassive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PerfectPassive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectPassive(i, 2))
        print('')
        for i in range(1,7):
            print(word.FuturePassive(i, 2))
        print('')
        for i in range(1,7):
            print(word.ImperfectPassiveSubjunctive(i, 2))
        print('')
        for i in range(1,7):
            print(word.PluperfectPassiveSubjunctive(i, 2))
        print('')
        for i in range(1,3):
            for j in range(1,7):
                print(word.PresentParticiple(i, 2, j))
        print('')
        for i in range(1,3):
            for j in range(1,7):
                print(word.FutureParticiple(i, 2, j))
        print('')
        for i in range(1,3):
            for j in range(1,7):
                print(word.PerfectParticiple(i, 2, j))
        print('')
        for i in range(1,3):
                print(word.GerundiveOfPurpose(i, 2))
        print('')


