"""Shared text utilities for voice-harness. Stdlib only. Deterministic."""
import re,statistics as st,glob,os
def body(path):
    t=open(path).read()
    m=re.match(r'---\n.*?\n---\n(.*)',t,re.S)
    return m.group(1).strip() if m else t
def strip_md(t):
    t=re.sub(r'^#+\s.*$','',t,flags=re.M)         # headings are not sentences
    t=re.sub(r'^\*\*\*$','',t,flags=re.M)
    t=re.sub(r'^- ','',t,flags=re.M)
    t=t.replace('**','')
    t=re.sub(r'(?<!\w)\*(?=\w)|(?<=\w)\*(?!\w)','',t)
    t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)
    t=re.sub(r'!?\[\]\([^)]*\)','',t)
    return t
ABBR=r'(?:Mr|Mrs|Ms|Dr|St|vs|etc|e\.g|i\.e|U\.S|Inc|No)'
def paragraphs(t):
    return [p.strip() for p in re.split(r'\n\s*\n',strip_md(t)) if p.strip()]
def sentences(par):
    par=re.sub(r'\b'+ABBR+r'\.',lambda m:m.group(0).replace('.','<D>'),par)
    s=re.split(r'(?<=[.!?…])["”’\)]*\s+(?=["“‘\(]?[A-Z0-9])|\n',par)
    return [x.replace('<D>','.').strip() for x in s if x.strip()]
def words(t): return re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)*",t)
def sent_lens(t):
    return [len(words(s)) for p in paragraphs(t) for s in sentences(p) if words(s)]
FUNC="the of and to a in that is it was for on with as i you he she they we this but at by not be have are from or an so if there what all about my your their one would can just like more when who which them out up do no had has were will been than then also because even only how really its into some other these those me him her us our any very still too much over such here where why while though yet still dont don’t".split()
FUNC=sorted(set(w.replace('’',"'") for w in FUNC))
def norm(t): return t.replace('’',"'").replace('‘',"'")
def func_profile(t):
    ws=[norm(w).lower() for w in words(strip_md(t))]
    n=len(ws); from collections import Counter; c=Counter(ws)
    return {w:1000*c[w]/n for w in FUNC}, n
def punct(t):
    raw=t; s=strip_md(t); n=len(words(s)); k=1000/n
    cnt=lambda p: len(re.findall(p,s))
    d={
     'em_dash':cnt('—'),'en_dash':cnt('–'),'spaced_hyphen_dash':cnt(r' - '),
     'comma':cnt(','),'semicolon':cnt(';'),'colon':cnt(':'),'paren_open':cnt(r'\('),
     'question':cnt(r'\?'),'exclaim':cnt('!'),'ellipsis':cnt('…|\.\.\.'),
     'curly_apos':cnt('’'),'straight_apos':cnt("'"),'curly_dq':cnt('[“”]'),'straight_dq':cnt('"'),
     'contraction':cnt(r"\b\w+['’](?:t|s|re|ve|ll|d|m)\b"),
     'italic_marks':len(re.findall(r'(?<!\*)\*(?!\*)[^*\n]+\*(?!\*)',raw)),
     'bold_marks':len(re.findall(r'\*\*[^*\n]+\*\*',raw)),
     'headings':len(re.findall(r'^#+\s',raw,re.M)),
     'list_items':len(re.findall(r'^- ',raw,re.M)),
    }
    out={a:b*k for a,b in d.items()}
    # oxford comma: ", and|or" preceded by a list (X, Y, and Z)
    ox=len(re.findall(r'\w+, \w+[^.,;]*, (?:and|or) ',s)); nox=len(re.findall(r'\w+, \w+[^.,;]* (?:and|or) (?!so )',s))
    out['oxford_comma_per_1000']=ox*k
    return out
DISC=['but','and','so','however','though','yet','instead','honestly','genuinely','actually','really','maybe','probably','basically','literally','look','sure','still','anyway']
def lexical(t):
    ws=[norm(w).lower() for w in words(strip_md(t))]; n=len(ws)
    from collections import Counter; c=Counter(ws)
    # MATTR window 500
    W=500; vals=[]
    for i in range(0,max(1,n-W),50): vals.append(len(set(ws[i:i+W]))/W)
    hap=sum(1 for w,v in c.items() if v==1)/len(c)
    ss=[s for p in paragraphs(t) for s in sentences(p)]
    starts=Counter(re.sub(r'^["“‘(]+','',s).split(' ')[0].lower().strip(',') for s in ss if s)
    d={'mattr500':st.mean(vals) if vals else len(set(ws))/n,'hapax_ratio':hap,
       'first_person_I_per_1000':1000*(c['i']+c["i'm"]+c["i've"]+c["i'd"]+c["i'll"])/n,
       'second_person_you_per_1000':1000*(c['you']+c['your']+c["you're"]+c["you've"]+c["you'll"]+c["you'd"])/n,
       'we_per_1000':1000*(c['we']+c['our']+c['us']+c["we're"]+c["we've"])/n}
    for w in DISC: d['disc_'+w+'_per_1000']=1000*c[w]/n
    for w in ['but','and','so','or','because','which','that']:
        d['sent_start_'+w+'_share']=starts[w]/len(ss)
    return d
def dist(vals):
    v=sorted(vals); n=len(v)
    q=lambda p: v[min(n-1,int(p*(n-1)+0.5))]
    return {'mean':st.mean(v),'sd':st.pstdev(v),'median':st.median(v),'p10':q(.1),'p90':q(.9),'min':v[0],'max':v[-1]}
