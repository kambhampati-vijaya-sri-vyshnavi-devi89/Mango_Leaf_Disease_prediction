"""
Comprehensive mango leaf disease knowledge base.
Contains symptoms, causes, cures, prevention, and severity for each disease.
"""

DISEASE_INFO = {
    "Anthracnose": {
        "scientific_name": "Colletotrichum gloeosporioides",
        "type": "Fungal",
        "severity": "High",
        "severity_color": "#e63946",
        "description": (
            "Anthracnose is one of the most serious mango diseases worldwide, caused by the fungus "
            "Colletotrichum gloeosporioides. It affects leaves, flowers, and fruits at all stages."
        ),
        "symptoms": [
            "Dark brown to black irregular spots on leaves",
            "Spots enlarge and coalesce during humid conditions",
            "Premature defoliation in severe cases",
            "Sunken black lesions on fruits",
            "Blossom blight during flowering",
        ],
        "causes": [
            "Warm humid weather (25–30°C, >80% humidity)",
            "Rain splash spreads fungal spores",
            "Infected plant debris on soil",
            "Poor air circulation in dense canopy",
        ],
        "treatment": [
            "Apply copper-based fungicides (copper oxychloride 0.3%) at fortnightly intervals",
            "Spray carbendazim (0.1%) or mancozeb (0.25%) during flowering",
            "Remove and destroy infected plant parts immediately",
            "Apply systemic fungicide thiophanate-methyl for severe infections",
            "Use Bordeaux mixture (1%) as a protective spray",
        ],
        "prevention": [
            "Prune trees after harvest to improve air circulation",
            "Avoid overhead irrigation; use drip irrigation instead",
            "Apply preventive fungicide sprays before monsoon season",
            "Use disease-free planting material",
            "Maintain orchard sanitation — remove fallen leaves and fruits",
            "Apply lime to soil to reduce fungal spore viability",
        ],
        "spread_control": [
            "Quarantine infected trees immediately",
            "Disinfect pruning tools with 70% alcohol between cuts",
            "Apply mulch to prevent rain splash of soil-borne spores",
            "Establish buffer zones between infected and healthy trees",
            "Monitor weather forecasts and spray before predicted rain",
        ],
        "organic_options": [
            "Neem oil spray (2%) — apply every 7–10 days",
            "Trichoderma-based bio-fungicides",
            "Garlic extract spray as a natural antifungal",
        ],
    },

    "Bacterial Canker": {
        "scientific_name": "Xanthomonas campestris pv. mangiferaeindicae",
        "type": "Bacterial",
        "severity": "High",
        "severity_color": "#e63946",
        "description": (
            "Bacterial canker is a destructive disease caused by Xanthomonas bacteria, "
            "forming water-soaked lesions that become necrotic on leaves, twigs, and fruits."
        ),
        "symptoms": [
            "Water-soaked irregular spots turning brown with yellow halo",
            "Raised, cracked canker lesions on twigs and branches",
            "Gummy exudate from infected bark",
            "Leaf distortion and premature drop",
            "Star-shaped cracks on infected fruits",
        ],
        "causes": [
            "Entry through wounds, stomata, and lenticels",
            "Wind-driven rain spreads bacteria",
            "Infected nursery stock and pruning tools",
            "High temperatures with high humidity",
        ],
        "treatment": [
            "Spray copper hydroxide (0.2%) or copper oxychloride (0.3%)",
            "Apply streptomycin sulfate (500–1000 ppm) for severe cases",
            "Prune and destroy infected branches 15 cm below visible infection",
            "Swab cut surfaces with Bordeaux paste",
            "Inject tetracycline solution in severely infected trunks",
        ],
        "prevention": [
            "Use certified disease-free nursery plants",
            "Avoid creating wounds during cultural operations",
            "Disinfect all tools with bleach solution (1:9 ratio) before use",
            "Apply copper-based sprays prophylactically before rainy season",
            "Plant resistant varieties where available",
            "Avoid intercropping with other Xanthomonas host plants",
        ],
        "spread_control": [
            "Strict quarantine — do not move plant material from infected areas",
            "Notify agricultural authorities if outbreak is detected",
            "Burn (do not compost) all infected material",
            "Sterilize soil around infected trees with formaldehyde solution",
            "Install windbreaks to reduce wind-driven bacterial spread",
        ],
        "organic_options": [
            "Copper-based sprays (approved for organic use)",
            "Bacillus subtilis bio-bactericide applications",
            "Lime-sulfur sprays during dormant season",
        ],
    },

    "Cutting Weevil": {
        "scientific_name": "Deporaus marginatus",
        "type": "Insect Pest",
        "severity": "Medium",
        "severity_color": "#f4a261",
        "description": (
            "The mango leaf-cutting weevil (Deporaus marginatus) damages young leaves and shoots. "
            "Adult weevils cut leaves in a characteristic V-shape for egg laying."
        ),
        "symptoms": [
            "V-shaped or circular cuts on young leaf margins",
            "Rolled leaf tubes (for egg laying) hanging from branches",
            "Skeletonized young leaves",
            "Wilting and drying of young shoots",
            "Presence of small brown weevils (4–5 mm) on foliage",
        ],
        "causes": [
            "Adult weevil infestation during new flush periods",
            "High pest populations in unmanaged orchards",
            "Absence of natural predators",
            "Dense canopy providing shelter for pests",
        ],
        "treatment": [
            "Spray carbaryl (0.15%) or malathion (0.05%) during new flush",
            "Apply chlorpyrifos (0.04%) for heavy infestations",
            "Collect and destroy rolled leaf tubes containing eggs",
            "Apply insecticidal soap solution on affected areas",
            "Use systemic insecticide imidacloprid (0.005%) soil drench",
        ],
        "prevention": [
            "Monitor trees closely during new flush emergence",
            "Prune dense canopy to reduce pest-friendly microhabitats",
            "Install sticky yellow traps to monitor and trap adults",
            "Encourage natural predators (birds, beneficial insects)",
            "Apply diatomaceous earth around tree base",
        ],
        "spread_control": [
            "Remove and destroy all rolled leaf tubes promptly",
            "Avoid movement of infested plant material",
            "Coordinate spray programs with neighboring orchards",
            "Use pheromone traps for early detection and mass trapping",
        ],
        "organic_options": [
            "Neem seed kernel extract (NSKE 5%) spray",
            "Spinosad-based organic insecticides",
            "Beauveria bassiana bio-insecticide",
            "Release of Trichogramma parasitoids",
        ],
    },

    "Die Back": {
        "scientific_name": "Lasiodiplodia theobromae",
        "type": "Fungal",
        "severity": "High",
        "severity_color": "#e63946",
        "description": (
            "Die back (also called stem-end rot) is caused by the fungus Lasiodiplodia theobromae "
            "and causes progressive death of twigs and branches from tips backward."
        ),
        "symptoms": [
            "Drying and dying of shoots from tip downward",
            "Dark brown to black discoloration of wood under bark",
            "Wilting and browning of leaves without shedding",
            "Gummy exudate from infected bark",
            "Gradual death of entire branches in severe cases",
        ],
        "causes": [
            "Entry through pruning wounds and natural openings",
            "Stressed trees (drought, waterlogging, nutrient deficiency)",
            "High temperatures (30–35°C) favor fungal growth",
            "Mechanical damage from harvesting operations",
        ],
        "treatment": [
            "Prune infected branches 15 cm below the line of infection",
            "Apply copper oxychloride paste on cut ends immediately",
            "Spray thiophanate-methyl (0.1%) or carbendazim (0.1%)",
            "Apply Bordeaux mixture to wounds after pruning",
            "Inject carbendazim solution into severely infected trunks",
        ],
        "prevention": [
            "Always seal pruning wounds with copper-based paste or tree sealant",
            "Avoid pruning during wet or humid weather",
            "Maintain proper nutrition — adequate potassium strengthens plant defense",
            "Ensure good drainage to prevent waterlogging stress",
            "Apply silicon-based foliar sprays to strengthen cell walls",
            "Avoid creating unnecessary wounds during field operations",
        ],
        "spread_control": [
            "Sterilize all pruning tools before and after each cut",
            "Burn infected prunings — never leave on orchard floor",
            "Apply fungicide spray after any storm damage or pruning",
            "Reduce tree stress through proper irrigation and fertilization",
        ],
        "organic_options": [
            "Trichoderma harzianum application on wounds",
            "Neem cake soil application to suppress soil-borne inoculum",
            "Garlic and ginger extract wound dressings",
        ],
    },

    "Gall Midge": {
        "scientific_name": "Erosomyia mangiferae",
        "type": "Insect Pest",
        "severity": "Medium",
        "severity_color": "#f4a261",
        "description": (
            "The mango gall midge is a tiny fly whose larvae create characteristic galls (swellings) "
            "on mango leaves, shoots, and flower buds, reducing photosynthesis and yield."
        ),
        "symptoms": [
            "Globular or elongated galls on leaf surface",
            "Galls initially green, turning brown and hard",
            "Leaf distortion and curling around gall sites",
            "Premature leaf drop in heavy infestations",
            "Stunted shoot and flower growth",
        ],
        "causes": [
            "Adult midge egg-laying on young tender leaves",
            "Warm and humid conditions favor midge activity",
            "High midge populations in surrounding vegetation",
            "Absence of parasitic wasps (natural enemies)",
        ],
        "treatment": [
            "Spray imidacloprid (0.005%) or thiamethoxam (0.02%)",
            "Apply dimethoate (0.06%) during early flush stage",
            "Remove and burn heavily galled leaves and shoots",
            "Use systemic insecticides when 30% leaves show galls",
            "Apply chlorpyrifos (0.04%) soil drench to kill pupae",
        ],
        "prevention": [
            "Apply preventive insecticide spray at bud-break stage",
            "Monitor trees weekly during new flush period",
            "Avoid excessive nitrogen fertilization (produces excess flush)",
            "Prune to maintain open canopy structure",
            "Install light traps to monitor and trap adult midges",
        ],
        "spread_control": [
            "Remove galled leaves before adult emergence",
            "Till soil under canopy to expose and destroy pupae",
            "Release parasitic wasps (Platygaster sp.) for biological control",
            "Coordinate management with neighboring farms",
        ],
        "organic_options": [
            "Neem oil (2%) spray at weekly intervals during flush",
            "Kaolin clay spray to repel adult midges",
            "Sticky yellow traps for mass trapping",
            "Bacillus thuringiensis (Bt) for larval control",
        ],
    },

    "Healthy": {
        "scientific_name": "N/A",
        "type": "Healthy",
        "severity": "None",
        "severity_color": "#52b788",
        "description": (
            "The leaf appears healthy with no visible signs of disease, pest damage, or nutrient deficiency. "
            "Continue good agricultural practices to maintain tree health."
        ),
        "symptoms": [],
        "causes": [],
        "treatment": [
            "No treatment required — tree appears healthy",
            "Continue regular fertilization schedule",
            "Maintain irrigation as per crop water requirement",
        ],
        "prevention": [
            "Apply balanced NPK fertilizers (10:10:10) twice yearly",
            "Maintain soil pH between 5.5–7.5 for optimal nutrient uptake",
            "Conduct regular monitoring every 2 weeks for early pest/disease detection",
            "Apply preventive fungicide spray before monsoon season",
            "Practice regular pruning to maintain canopy health",
            "Ensure adequate spacing between trees for air circulation",
        ],
        "spread_control": [
            "No spread control needed — tree is healthy",
            "Maintain current management practices",
        ],
        "organic_options": [
            "Apply compost and organic matter annually",
            "Use biofertilizers (Rhizobium, Azospirillum) to improve nutrient uptake",
            "Spray micronutrient mix (zinc, boron, manganese) twice yearly",
        ],
    },

    "Powdery Mildew": {
        "scientific_name": "Oidium mangiferae",
        "type": "Fungal",
        "severity": "High",
        "severity_color": "#e63946",
        "description": (
            "Powdery mildew is caused by Oidium mangiferae and is one of the most damaging mango diseases, "
            "particularly at flowering. It covers leaves and flowers with a white powdery growth."
        ),
        "symptoms": [
            "White powdery growth on young leaves (upper surface)",
            "Severe blossom infection — white coating on flower panicles",
            "Infected flowers fail to set fruit (major yield loss)",
            "Distortion and curling of young leaves",
            "Premature shedding of infected flowers and young fruits",
        ],
        "causes": [
            "Cool nights (10–15°C) followed by warm days (25–30°C)",
            "Dry weather with dew or high humidity at night",
            "Poor ventilation in dense canopies",
            "High nitrogen levels promoting succulent growth",
        ],
        "treatment": [
            "Spray sulfur (0.2%) or wettable sulfur (0.3%) as first line treatment",
            "Apply triadimefon (0.1%) or hexaconazole (0.05%) for systemic control",
            "Use dinocap (0.1%) at 15-day intervals during flowering",
            "Apply myclobutanil (0.04%) for resistant strains",
            "Spray potassium bicarbonate (0.5%) as an organic fungicide",
        ],
        "prevention": [
            "Apply first protective sulfur spray at early panicle emergence",
            "Prune canopy after harvest to improve air flow",
            "Avoid excessive nitrogen fertilization in pre-flowering period",
            "Irrigate early morning so foliage dries by evening",
            "Plant disease-resistant varieties where available",
            "Apply silicon foliar spray to strengthen epidermal cells",
        ],
        "spread_control": [
            "Remove heavily infected panicles to reduce spore load",
            "Apply sulfur dust in dry conditions for rapid knockdown",
            "Maintain spray program every 10–14 days during susceptible period",
            "Avoid working in orchard when plants are wet (spreads spores on clothing)",
        ],
        "organic_options": [
            "Sulfur dust or wettable sulfur spray (approved organic)",
            "Neem oil (2%) + potassium bicarbonate (0.5%) combination",
            "Baking soda solution (1 tsp/L) as emergency treatment",
            "Ampelomyces quisqualis (mycoparasite) bio-fungicide",
        ],
    },

    "Sooty Mould": {
        "scientific_name": "Meliola mangiferae / Capnodium mangiferae",
        "type": "Fungal (Secondary)",
        "severity": "Medium",
        "severity_color": "#f4a261",
        "description": (
            "Sooty mould is a secondary fungal infection that grows on the honeydew secretions of sap-sucking "
            "insects (mealybugs, aphids, scales). The black coating blocks sunlight and reduces photosynthesis."
        ),
        "symptoms": [
            "Black powdery coating on upper leaf surfaces",
            "Coating can be rubbed off (unlike leaf diseases)",
            "Reduced photosynthesis and yellowing under black layer",
            "Presence of honeydew-producing insects (mealybugs, aphids)",
            "Sooty deposits on twigs, branches, and fruits",
        ],
        "causes": [
            "Honeydew secretions from aphids, mealybugs, scale insects",
            "High pest populations on trees",
            "Humid, warm conditions favoring fungal growth",
            "Ants farming honeydew-producing insects on the tree",
        ],
        "treatment": [
            "FIRST — control the honeydew-producing insects:",
            "Spray imidacloprid (0.005%) or thiamethoxam for insect control",
            "Apply starch solution (1%) to loosen sooty mould for washing",
            "Spray copper oxychloride (0.3%) to kill sooty mould fungus",
            "Use high-pressure water jet to physically remove sooty mould",
            "Apply white oil (horticultural oil 1%) to smother insects",
        ],
        "prevention": [
            "Regular monitoring for aphids, mealybugs, and scale insects",
            "Apply sticky bands around trunk to prevent ant access",
            "Prune dense canopy to reduce insect-friendly microhabitats",
            "Encourage natural predators: ladybugs, lacewings, parasitic wasps",
            "Apply preventive insecticide spray during new flush stage",
            "Remove ant colonies near tree base to protect insect predators",
        ],
        "spread_control": [
            "Control ant populations (ants protect honeydew insects from predators)",
            "Apply systemic insecticide to eliminate insect colonies",
            "Isolate heavily infested trees and treat aggressively",
            "Avoid nitrogen over-fertilization (creates succulent tissue that attracts insects)",
        ],
        "organic_options": [
            "Neem oil spray (2%) to control sap-sucking insects",
            "Insecticidal soap spray for aphids and mealybugs",
            "Release Cryptolaemus montrouzieri (mealybug destroyer) beetle",
            "Diatomaceous earth around tree base",
        ],
    },
}


def get_disease_info(disease_name):
    """Return disease info dict, with fallback for unknown diseases."""
    name = disease_name.strip()
    if name in DISEASE_INFO:
        return DISEASE_INFO[name]
    # Try case-insensitive match
    for key, val in DISEASE_INFO.items():
        if key.lower() == name.lower():
            return val
    # Fallback
    return {
        "scientific_name": "Unknown",
        "type": "Unknown",
        "severity": "Unknown",
        "severity_color": "#888",
        "description": f"Detailed information for '{name}' is not yet in our database.",
        "symptoms": [],
        "causes": [],
        "treatment": ["Consult a local agricultural extension officer for advice."],
        "prevention": ["Follow general good agricultural practices."],
        "spread_control": ["Isolate affected plants as a precautionary measure."],
        "organic_options": [],
    }
