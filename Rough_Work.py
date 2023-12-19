import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Crime scenario input
crime_scenario = input("Describe the crime scenario: ")

# NLP for entity recognition
def extract_entities(text):
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return entities

entities = extract_entities(crime_scenario)

# Rule-based matching for IPC and CrPC sections
def match_sections(entities):
    ipc_sections = {
        "theft": "Section 378 IPC",
        "robbery": "Section 392 IPC",
        # Add more rules as needed
    }

    crpc_sections = {
        "arrest": "Section 46 CrPC",
        "search": "Section 100 CrPC",
        # Add more rules as needed
    }

    ipc_matches = [ipc_sections[entity.lower()] for entity in entities if entity.lower() in ipc_sections]
    crpc_matches = [crpc_sections[entity.lower()] for entity in entities if entity.lower() in crpc_sections]

    return ipc_matches, crpc_matches

ipc_matches, crpc_matches = match_sections(entities)

# Display results
print("IPC Sections:", ipc_matches)
print("CrPC Sections:", crpc_matches)
