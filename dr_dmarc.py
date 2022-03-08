import subprocess

#Open file with domain addresses.  Each domain on its own line.
search_domain_txt_file = open("c:/Users/Dan/Documents/Code/python/dr_dmarc/domain_input.txt", "r")
#Read the file
domain_array_from_file = search_domain_txt_file.read()
#Create an array consisting of each domain
domain_array = domain_array_from_file.split("\n")
#Close file
search_domain_txt_file.close()

#loop through the domains..
for i in domain_array:
    #Perform nslookup 
    nslookup_raw = subprocess.getoutput("nslookup -type=txt _dmarc." + i + "| findstr \"v=DMARC1;\"")
    #Remove "Non-authoritative answer:" from the string
    nslookup_remove_non_auth = nslookup_raw.replace("Non-authoritative answer:", "")
    #Remove whitespace
    nslookup_with_quotes = nslookup_remove_non_auth.strip()
    #Remove double quotes
    dmarc = nslookup_with_quotes.strip('"')
    
    
    #SET DMARC PROVIDER HERE
    dmarc_provider = "agari"
    #SET DMARC PROVIDER HERE

    #Check to see if DMARC PROVIDER exists in the dmarc record, print to console
    if dmarc_provider in dmarc:
        print ("Yes," + i + ",\"" + dmarc + "\"")
    else:
        print ("No," + i + ",\"" + dmarc + "\"")
