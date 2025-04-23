from database import engine, drug_interactions, symptom_mapping

def validate_prescription(prescription_text, symptoms):
    with engine.connect() as conn:
        # Check symptom-to-medicine mapping
        medicines = []
        for symptom in symptoms:
            result = conn.execute(symptom_mapping.select().where(symptom_mapping.c.symptom == symptom))
            medicines.extend([row['medicine'] for row in result])
        
        # Check interactions between prescribed drugs
        warnings = []
        prescribed_drugs = prescription_text.split(", ")
        for i, drug_a in enumerate(prescribed_drugs):
            for drug_b in prescribed_drugs[i+1:]:
                interaction = conn.execute(drug_interactions.select().where(
                    (drug_interactions.c.drug_a == drug_a) & (drug_interactions.c.drug_b == drug_b)
                )).fetchone()
                if interaction:
                    warnings.append(f"Interaction between {drug_a} and {drug_b}: {interaction['interaction']}")
        
        return {
            "medicines": medicines,
            "warnings": warnings
        }
