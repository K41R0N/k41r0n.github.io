"""Lists lines in corpus/raw that look like footers, plugs or page furniture, so they can be removed before they teach the writer to end every piece with a plug. Stdlib only.
Usage: corpus_clean_check.py [corpus_dir]. Lists candidates for review; it never edits a file."""
import sys,os,re,glob
PAT=[r'subscribe',r'share this',r'if you enjoyed',r'leave a comment',r'read more',r'buy (my|the) book',r'newsletter',r'follow me',r'click here',r'sign up',r'©|copyright']
def run(c):
    out=[]
    for p in sorted(glob.glob(os.path.join(c,'*.md'))):
        for i,l in enumerate(open(p).read().splitlines(),1):
            if any(re.search(x,l,re.I) for x in PAT): out.append((os.path.basename(p),i,l.strip()[:110]))
    return out
if __name__=='__main__':
    c=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..','..','..','assets','voice-corpus','raw')
    r=run(c)
    for f,i,l in r: print(f'{f}:{i}: {l}')
    print(f'{len(r)} candidate line(s)')
