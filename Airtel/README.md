# Assignment
Explaination 
Title: Airtel Business Solutions Sales Pitch and Discovery Questions

Description: Generate a brief sales pitch and relevant discovery questions for a medium-sized business owner in Faridabad, specializing in bathroom-ware distribution across Delhi, Haryana, and Punjab, focusing on Airtel's products.

*Customer Profile:*

Owner of a medium-sized business in Faridabad. Deals in distribution of bathroom-ware and fittings across Delhi, Haryana and Punjab. Uses Jio Wi-Fi in his home and office set-up. Has a small 20-seater office and is currently hiring more employees. Is hard pressed for time and looking to optimize.

*Airtel Business Solutions:*

Airtel offers high-speed 5G network connectivity, IoT infrastructure, and spam reduction features tailored for businesses.

*Problem Statement:*

Generate the following for the customer:
1) A brief pitch for a salesperson (not more than 70 words), focusing on Airtel's products and their benefits.
2) 4 leading questions a salesperson can ask to discover helpful responses for a customized sales pitch. Ensure diversity in the questions.

*Example Output:*

Pitch: "Transform your bathroom-ware distribution with Airtel's cutting-edge solutions. Leverage our high-speed 5G network for seamless connectivity across Delhi, Haryana, and Punjab. Integrate IoT infrastructure to optimize inventory management. Shield your operations with our advanced spam reduction features."

Questions:
1. How do you currently handle inventory tracking and distribution logistics?
2. What are the primary pain points in your office setup that hinder efficiency?
3. Have you explored leveraging 5G technology to enhance your business operations?
4. What measures are you taking to safeguard your network from spam and cyber threats?

Provide the Python code to generate the required outputs.
def generate_pitch():
    pitch = "Transform your bathroom-ware distribution with Airtel's cutting-edge solutions. Leverage our high-speed 5G network for seamless connectivity across Delhi, Haryana, and Punjab. Integrate IoT infrastructure to optimize inventory management. Shield your operations with our advanced spam reduction features."
    return pitch

   # example code attached-

def generate_questions():
    questions = [
        "How do you currently handle inventory tracking and distribution logistics?",
        "What are the primary pain points in your office setup that hinder efficiency?",
        "Have you explored leveraging 5G technology to enhance your business operations?",
        "What measures are you taking to safeguard your network from spam and cyber threats?"
    ]
    return questions

# Test
pitch = generate_pitch()
questions = generate_questions()

print("Pitch for the Customer:")
print(pitch)
print("\nQuestions for the Customer:")
for idx, q in enumerate(questions, 1):
    print(f"{idx}. {q}")
