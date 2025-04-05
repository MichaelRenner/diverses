import ldap
from lxml import etree

# Konfiguration
LDAP_SERVER = "ldap://sip.db0sda.hamnet.radio"
BASE_DN = "ou=sipusers,dc=db0sda,dc=ampr,dc=org"
XML_FILE = "fritzbox7_phonebook.xml"
PHONEBOOK_NAME = "Hamnet ohne Prefix"

def fetch_ldap_entries():
    # LDAP-Verbindung ohne SSL
    conn = ldap.initialize(LDAP_SERVER)
    conn.protocol_version = ldap.VERSION3

    # LDAP-Suche (öffentliches Adressbuch)
    search_filter = "(objectClass=person)"
    attributes = ["cn", "telephoneNumber"]
    results = conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, search_filter, attributes)
    return results

def create_phonebook_xml(entries):
    # XML-Baumstruktur erstellen
    root = etree.Element("phonebooks")
    phonebook = etree.SubElement(root, "phonebook", name=PHONEBOOK_NAME)

    for entry in entries:
        dn, attr = entry
        if "cn" in attr and "telephoneNumber" in attr:
            contact = etree.SubElement(phonebook, "contact")
            person = etree.SubElement(contact, "person")
            name = etree.SubElement(person, "realName")
            name.text = attr["cn"][0]

            telephony = etree.SubElement(contact, "telephony")
            telephony.set("nid", "1")
            for number in attr["telephoneNumber"]:
                number_element = etree.SubElement(telephony, "number")
                number_element.text = number
                number_element.set("type", "privat")

    return etree.tostring(root, pretty_print=True, encoding="utf-8", xml_declaration=True)

def main():
    print("Lade Einträge vom LDAP-Server...")
    entries = fetch_ldap_entries()

    print("Erstelle XML-Datei...")
    phonebook_xml = create_phonebook_xml(entries)

    with open(XML_FILE, "wb") as f:
        f.write(phonebook_xml)

    print(f"Telefonbuch '{PHONEBOOK_NAME}' wurde in '{XML_FILE}' gespeichert.")

if __name__ == "__main__":
    main()

