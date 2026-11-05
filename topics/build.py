import json, collections
G=[('kids','Kids','8 to 12'),('teens','Teens','13 to 15'),('senior','Senior school','16 to 18, HSC and final exams'),('uni','Uni',''),('adults','Adults','')]
DEF={1:"Keep it short. One clear idea.",2:"One short paragraph.",3:"About 100 to 150 words.",4:"About 150 to 250 words.",5:"Take your time. Make every word count."}
out={}; tot=0; csv=['group,subject,level,topic,rule']
for k,_,_ in G:
  rows=[]
  for ln in open(f'topics/{k}.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln.strip(): continue
    s,l,p,r=ln.split('|'); l=int(l); r=r.strip() or DEF[l]
    rows.append([s,l,p.strip(),r])
    csv.append(','.join('"'+str(x).replace('"','""')+'"' for x in [k,s,l,p.strip(),r]))
  c=collections.Counter((s,l) for s,l,_,_ in rows)
  ps=[p for _,_,p,_ in rows]; d=[p for p,n in collections.Counter(ps).items() if n>1]
  print(k,len(rows),'subjects',sorted(set(s for s,_,_,_ in rows)),'cells not 5:',{x:n for x,n in c.items() if n!=5},'dupes',d)
  out[k]=rows; tot+=len(rows)
print('total',tot)
open('site/topics.js','w',encoding='utf-8').write('/* Wrimble topic bank: [subject, level 1-5, topic, rule]. Our own words. Built from topics/*.txt */\nconst TOPICS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
open('topics/wrimble-topics.csv','w',encoding='utf-8').write('\n'.join(csv)+'\n')
