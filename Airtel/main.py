customer_profiles = [
    {
        "name": "Customer A",
        "business": "Distribution of bathroom-ware and fittings",
        "location": "Faridabad",
        "internet_provider": "Jio Wi-Fi",
        "office_size": 20,
        "expansion_plans": "Hiring more employees"
    },
    {
        "name": "Customer B",
        "business": "Micro-finance company",
        "location": "Ahmedabad",
        "internet_provider": "Airtel Broadband - 100 mbps",
        "office_size": 100,
        "expansion_plans": "Shifting to a larger office location"
    }
]

def generate_pitch(customer_profile):
    if customer_profile["internet_provider"] == "Jio Wi-Fi":
        pitch = f"Upgrade to a reliable and fast internet connection with our business plans, perfect for your growing team of {customer_profile['office_size']} employees in {customer_profile['location']}."
    else:
        pitch = f"Take your business to the next level with our scalable internet solutions, ideal for your micro-finance company in {customer_profile['location']} with {customer_profile['office_size']} employees."
    return pitch

def generate_questions(customer_profile):
    questions = [
        f"How do you currently manage your internet connectivity across your {customer_profile['office_size']}-seater office?",
        f"What are your biggest pain points when it comes to internet speed and reliability in your {customer_profile['location']} office?",
        f"How do you envision your internet needs changing with your plans to {customer_profile['expansion_plans']}?",
        f"What kind of technology solutions are you currently exploring to support your business growth in {customer_profile['location']}?"
    ]
    return questions

for customer_profile in customer_profiles:
    print(f"**Customer Profile: {customer_profile['name']}**")
    print(f"**Pitch:** {generate_pitch(customer_profile)}")
    print(f"**Leading Questions:**")
    for question in generate_questions(customer_profile):
        print(f"- {question}")
    print()


