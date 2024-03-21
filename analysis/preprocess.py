import regex as re
from nltk.tokenize import TweetTokenizer
import unicodedata
import emoji
import wordsegment
import contractions

wordsegment.load()
english_words = set()

def segment(text):
    if '-' in text or '_' in text:
        return re.sub(r'[_-]|((?<!-)(?=[A-Z]))', ' ', text).split(' ')
    else:
        return_list = list(wordsegment.segment(text))
        # if the word is not in the dictionary, return the original word
        if any(word not in english_words for word in return_list) and len(text) <= 10:
            return_list = [text]
        return return_list

def preprocess(text):
    # mask URLs as [URL]
    text = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', '[URL]', text)
    text = text.lower()
    text = contractions.fix(text)

    return text

def tokenize(text, vocab_set):
    english_words = vocab_set
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True)
    text = preprocess(text)
    tokens = list()
    
    for token in tokenizer.tokenize(text):
        if emoji.is_emoji(token):
            tokens.append(token)
            continue
        
        token = unicodedata.normalize('NFKD', token).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
        # segment hashtags
        if token.startswith('#'):
            tokens.append('#')
            tokens.extend(segment(token[1:]))
            continue

        elif token not in english_words:
            tokens.extend(segment(token))
            continue

        tokens.append(token)

    tokens = list(filter(lambda x: x != '' and x != ' ', tokens))
    return tokens