import random

questions = [
    {
        "question": "What is the IUPAC name of CH₃–CH₂–OH?",
        "options": ["Methanol", "Ethanol", "Propanol", "Butanol"],
        "answer": "Ethanol",
        "chapter": "Organic Chemistry",
        "explanation": "CH₃–CH₂–OH has two carbon atoms and a hydroxyl group, making its IUPAC name Ethanol."
    },
    {
        "question": "Which of the following is an example of a strong acid?",
        "options": ["Acetic acid", "Hydrochloric acid", "Formic acid", "Citric acid"],
        "answer": "Hydrochloric acid",
        "chapter": "Acids, Bases and Salts",
        "explanation": "Hydrochloric acid ionizes completely in water, making it a strong acid."
    },
    {
        "question": "Which element is the most electronegative?",
        "options": ["Oxygen", "Fluorine", "Chlorine", "Nitrogen"],
        "answer": "Fluorine",
        "chapter": "Periodic Table",
        "explanation": "Fluorine has the highest electronegativity value on the Pauling scale."
    },
    {
        "question": "Which gas is produced during the reaction of zinc with HCl?",
        "options": ["Oxygen", "Hydrogen", "Nitrogen", "Carbon dioxide"],
        "answer": "Hydrogen",
        "chapter": "Chemical Reactions",
        "explanation": "Zinc reacts with hydrochloric acid to produce hydrogen gas and zinc chloride."
    },
    {
        "question": "Mark the correct order of decreasing acid strength of the following compounds.",
        "options": ["e > d > b > a > c", " b > d > a > c > e", "d > e > c > b > a", "e > d > c > b > a"],
        "answer": " b > d > a > c > e",
        "chapter": "Acids and Bases",
        "explanation": "Acid strength is affected by electronegativity and stability of conjugate base."
    },
    {
        "question": "Which acid is used in car batteries?",
        "options": ["Sulphuric acid", "Nitric acid", "Hydrochloric acid", "Acetic acid"],
        "answer": "Sulphuric acid",
        "chapter": "Daily Life Chemistry",
        "explanation": "Car batteries contain dilute sulphuric acid as the electrolyte."
    },
    {
        "question": "What is the oxidation number of Cr in K₂Cr₂O₇?",
        "options": ["+2", "+3", "+6", "+7"],
        "answer": "+6",
        "chapter": "Redox Reactions",
        "explanation": "The sum of oxidation states equals the total charge. Each Cr must be +6 to balance."
    },
    {
        "question": "Which block element is potassium?",
        "options": ["s-block", "p-block", "d-block", "f-block"],
        "answer": "s-block",
        "chapter": "Periodic Table",
        "explanation": "Potassium has its outer electron in an s-orbital (4s¹), so it's an s-block element."
    },
    {
        "question": "Which indicator is used in acid-base titration?",
        "options": ["Phenolphthalein", "Methyl orange", "Litmus", "All of the above"],
        "answer": "All of the above",
        "chapter": "Acids, Bases and Salts",
        "explanation": "Different titrations use different indicators depending on acid/base strength."
    },
    {
        "question": "What is the hybridization of carbon in methane?",
        "options": ["sp", "sp2", "sp3", "None"],
        "answer": "sp3",
        "chapter": "Chemical Bonding",
        "explanation": "Carbon in methane forms 4 sigma bonds using sp³ hybrid orbitals."
    },
    {
        "question": "The common name of NaHCO₃ is?",
        "options": ["Caustic soda", "Baking soda", "Washing soda", "Bleaching powder"],
        "answer": "Baking soda",
        "chapter": "Basic Chemistry",
        "explanation": "NaHCO₃ is commonly known as baking soda and is used in cooking."
    },
    {
        "question": "Which bond is strongest?",
        "options": ["Ionic", "Covalent", "Hydrogen", "Van der Waals"],
        "answer": "Covalent",
        "chapter": "Chemical Bonding",
        "explanation": "Covalent bonds involve shared electrons and are stronger than ionic or intermolecular forces."
    },
    {
        "question": "Tollen’s reagent is used to test for?",
        "options": ["Alcohol", "Ketone", "Aldehyde", "Carboxylic acid"],
        "answer": "Aldehyde",
        "chapter": "Organic Chemistry",
        "explanation": "Tollen's reagent gives a silver mirror test with aldehydes, not ketones."
    },
    {
        "question": "In Le Chatelier's principle, increasing pressure favors:",
        "options": ["More moles", "Less moles", "No effect", "Endothermic reactions"],
        "answer": "Less moles",
        "chapter": "Equilibrium",
        "explanation": "The system shifts to the side with fewer gas molecules to reduce pressure."
    },
    {
        "question": "Which gas turns limewater milky?",
        "options": ["O₂", "CO₂", "SO₂", "NO₂"],
        "answer": "CO₂",
        "chapter": "Air and Environment",
        "explanation": "CO₂ reacts with calcium hydroxide in limewater to form calcium carbonate (milky ppt)."
    },
    {
        "question": "Which of the following is not an isomer of butane?",
        "options": ["n-butane", "iso-butane", "cyclobutane", "methylpropane"],
        "answer": "cyclobutane",
        "chapter": "Organic Chemistry",
        "explanation": "Cyclobutane is a ring compound, not a structural isomer of butane."
    },
    {
        "question": "Which of these is used to bleach flour?",
        "options": ["Ozone", "Chlorine", "Bromine", "Hydrogen peroxide"],
        "answer": "Chlorine",
        "chapter": "Industrial Chemistry",
        "explanation": "Chlorine is a strong oxidizing agent and is used for bleaching purposes."
    },
    {
        "question": "Which element has the highest ionization energy?",
        "options": ["Fluorine", "Neon", "Helium", "Oxygen"],
        "answer": "Helium",
        "chapter": "Periodic Properties",
        "explanation": "Helium has a full shell and the smallest atomic size, making ionization hardest."
    },
    {
        "question": "Which metal is used in galvanization?",
        "options": ["Iron", "Aluminium", "Zinc", "Copper"],
        "answer": "Zinc",
        "chapter": "Metals and Non-Metals",
        "explanation": "Zinc coating prevents rusting of iron by forming a protective layer."
    },
    {
        "question": "Which acid is present in vinegar?",
        "options": ["Formic acid", "Citric acid", "Acetic acid", "Oxalic acid"],
        "answer": "Acetic acid",
        "chapter": "Organic Acids",
        "explanation": "Vinegar contains 4–8% acetic acid by volume."
    },
    {
        "question": "Which reagent distinguishes aldehydes from ketones?",
        "options": ["Fehling’s reagent", "Tollen’s reagent", "Brady’s reagent", "All"],
        "answer": "All",
        "chapter": "Organic Chemistry",
        "explanation": "All these reagents can help identify aldehydes over ketones via specific reactions."
    },
    {
        "question": "Name the first member of the alkyne series.",
        "options": ["Ethene", "Ethyne", "Methyne", "Propene"],
        "answer": "Ethyne",
        "chapter": "Hydrocarbons",
        "explanation": "Ethyne (C₂H₂) is the simplest alkyne with a triple bond."
    },
    {
        "question": "Which salt is used in photography?",
        "options": ["Sodium chloride", "Silver nitrate", "Potassium chloride", "Zinc sulphate"],
        "answer": "Silver nitrate",
        "chapter": "Applications of Salts",
        "explanation": "Silver nitrate is sensitive to light and is used in photographic films."
    },
    {
        "question": "What is the molecular formula of glucose?",
        "options": ["C₆H₁₂O₆", "C₆H₁₂O₅", "C₆H₁₀O₆", "C₆H₆O₆"],
        "answer": "C₆H₁₂O₆",
        "chapter": "Biomolecules",
        "explanation": "Glucose is a simple sugar with the molecular formula C₆H₁₂O₆."
    },
    {
        "question": "The process of loss of electrons is called?",
        "options": ["Reduction", "Oxidation", "Hydrolysis", "Neutralization"],
        "answer": "Oxidation",
        "chapter": "Redox Reactions",
        "explanation": "Oxidation involves the loss of electrons; reduction is the gain of electrons."
    },
    {
        "question": "Who proposed the modern periodic table?",
        "options": ["Dobereiner", "Mendeleev", "Bohr", "Moseley"],
        "answer": "Moseley",
        "chapter": "Periodic Table",
        "explanation": "Moseley arranged elements by atomic number, forming the basis of the modern table."
    },
    {
        "question": "The correct order of acidic strength is?",
        "options": ["HF > HCl > HBr > HI", "HI > HBr > HCl > HF", "HCl > HF > HI > HBr", "HBr > HCl > HF > HI"],
        "answer": "HI > HBr > HCl > HF",
        "chapter": "Acidic Properties",
        "explanation": "Acid strength increases down the group due to decreasing bond strength."
    },
    {
        "question": "Which is a biodegradable polymer?",
        "options": ["Teflon", "PHBV", "PVC", "Polystyrene"],
        "answer": "PHBV",
        "chapter": "Polymers",
        "explanation": "PHBV is a biopolymer that can degrade naturally by microorganisms."
    },
    {
        "question": "The green color of leaves is due to?",
        "options": ["Chlorophyll", "Carotene", "Anthocyanin", "Xanthophyll"],
        "answer": "Chlorophyll",
        "chapter": "Photosynthesis",
        "explanation": "Chlorophyll absorbs sunlight and gives the green pigment to plants."
    },
    {
        "question": "Which of the following is not a greenhouse gas?",
        "options": ["CO₂", "CH₄", "N₂", "O₃"],
        "answer": "N₂",
        "chapter": "Environment",
        "explanation": "N₂ is inert and does not trap heat, unlike greenhouse gases like CO₂ and CH₄."
    },
    {
        "question": "The pH of pure water is:",
        "options": ["0", "7", "14", "1"],
        "answer": "7",
        "chapter": "pH and Indicators",
        "explanation": "Pure water is neutral with equal H⁺ and OH⁻ ions, giving pH 7."
    }
    
]

random.shuffle(questions)
