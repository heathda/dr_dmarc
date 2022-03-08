# dr_dmarc
Checks a list of domains for their DMARC provider

### dr_dmarc.py - Search and print DMARC to console
Designed to perform a NSLOOKUP for DMARC from a list of domains and then print it to the console so it can be easily copy/imported into excel for further analysis/sharing/presentation.

##### Directions
- Create a file called domain_input.txt.
- Paste a single domain address on each line.
- Run dr_dmarc.py in the same directory as domain_input.txt  
<br/>

In dr_dmarc.py:  
```python
    #SET DMARC PROVIDER HERE  
    dmarc_provider = "agari"  
    #SET DMARC PROVIDER HERE  
```

Ex Input (in file domain_input.txt):  
  
Secureserver.net  
Cornell.edu  
Mapquest.com  


Ex Output (in the console you ran this in):

No,Secureserver.net,"v=DMARC1; p=none; fo=1; rua=mailto:report@<span></span>dmarc.em.secureserver.net, mailto:dmarc_agg@<span></span>dmarc.250ok.net"  
No,Cornell.edu,"v=DMARC1; p=none; rua=mailto:rua-reports@<span></span>cornell.edu"   
Yes,Mapquest.com,"v=DMARC1; p=none; fo=1; rua=mailto:aol@<span></span>rua.agari.com; ruf=mailto:aol@<span></span>ruf.agari.com"  
