import random

# Function to simulate ethical decision-making scenario
def generate_ethics_scenario(policy_question):
    """
    Simulate an ethical decision-making scenario based on the policy question.
    """
    # Predefined set of ethical scenarios and outcomes
    scenarios = [
        "Using AI in hiring decisions may result in faster, data-driven choices, but it could lead to bias if the training data is not diverse enough.",
        "AI in hiring decisions could increase fairness by removing human bias, but it may also reinforce existing biases if not carefully monitored.",
        "If AI is used in hiring, it may streamline the process, but there could be concerns about transparency and accountability in how decisions are made.",
        "While AI can assist in hiring decisions, it might limit human intuition and empathy, which are important in evaluating candidates for roles that require interpersonal skills."
    ]
    
    # Predefined ethical consequences
    consequences = [
        "Increased efficiency, but potentially fewer diverse hires.",
        "Fairer hiring process, but risk of algorithmic bias.",
        "Transparency may increase, but could create a lack of human touch.",
        "Faster hiring decisions, but risk of overlooking key human qualities."
    ]
    
    # Randomly select a scenario and a consequence
    selected_scenario = random.choice(scenarios)
    selected_consequence = random.choice(consequences)

    # Return a simple generated scenario
    return f"Policy Question: {policy_question}\n\nScenario: {selected_scenario}\n\nEthical Consequence: {selected_consequence}"

# Example policy question
policy_question = "Should AI be used in making hiring decisions?"

# Generate and print the ethical scenario
ethical_scenario = generate_ethics_scenario(policy_question)
print("Generated Ethical Scenario:")
print(ethical_scenario)