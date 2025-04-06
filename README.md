# Content
smaller scripts and projects that do not require their own repository
## Phone book for the Hamnet 
It is possible to retrieve the complete RWTH Aachen telephone directory (excluding service numbers) via the LDAP interface and save it locally. This is then imported into the Fritzbox in a second step.
### Fetching the phone book
The phone book must be imported into the Fritzbox in two versions, this is an imperfection of the Fritzbox or a specialty of this particular application: once in its "original state" and once with the prefix assigned to the RWTH's SIP server (in my case: *124#
* * ldap7fritzbox.py * * this script is writing the phone book into the file * * fritzbox7_phonebook.xml * * (this is configurable) without changing anything
* * ldap5fritzbox.py * * this script is writing the phone book into the file * * fritzbox5_phonebook.xml * * (this is configurable) adding a prefix (the prefix is also configurable)
### Import into the Fritzbox
Currently manually via -> Telefonie -> Telefonbuch -> Neues Telefonbuch -> Name = Test -> OK -> Wiederherstellen - > Browse (and select file) - > Übernehmen
