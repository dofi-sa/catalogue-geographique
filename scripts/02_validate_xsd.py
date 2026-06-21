import sys
import ossS

sys.stdout.reconfigure(encoding='utf-8')

from lxml import etree

def validate_xml(xml_path: str, xsd_path: str, log_path: str = "rapport_validation.log"):
    try:
        with open(xsd_path, 'rb') as f:
            schema_doc = etree.parse(f)
        xmlschema = etree.XMLSchema(schema_doc)

        with open(xml_path, 'rb') as f:
            xml_doc = etree.parse(f)

        xmlschema.assertValid(xml_doc)
        print(f"OK - Le fichier '{xml_path}' est valide selon le schema XSD.")
        with open(log_path, 'w', encoding='utf-8') as log:
            log.write("Validation reussie : aucun probleme detecte.\n")
        return True

    except etree.DocumentInvalid as e:
        print(f"INVALIDE - Le fichier '{xml_path}' contient des erreurs.")
        errors = xmlschema.error_log
        with open(log_path, 'w', encoding='utf-8') as log:
            log.write("Rapport de validation XSD\n")
            log.write("=" * 40 + "\n")
            for error in errors:
                msg = f"Ligne {error.line}, Colonne {error.column} : {error.message}"
                print(msg)
                log.write(msg + "\n")
        return False

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return False

if __name__ == "__main__":
    xml_file = "catalogue.xml"
    xsd_file = "lieux.xsd"
    success = validate_xml(xml_file, xsd_file)
    sys.exit(0 if success else 1)
