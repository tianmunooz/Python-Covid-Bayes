import streamlit as st

def bayes_theorem(prior, sensitivity, specificity):
    false_positive_rate = 1 - specificity
    pB = (sensitivity * prior) + (false_positive_rate * (1 - prior))
    posterior = (sensitivity * prior) / pB
    return posterior

st.title("Bayes' Theorem App for COVID-19 Testing")

st.markdown("""
This app calculates the probability of having COVID-19 given a positive test result, 
using **Bayes' Theorem**. Adjust the parameters below to see how they affect the result.
""")

prior = st.slider("Prevalence (Prior Probability) P(A)", 0.0, 1.0, 0.04, 0.01)
sensitivity = st.slider("Sensitivity (True Positive Rate) P(B|A)", 0.0, 1.0, 0.73, 0.01)
specificity = st.slider("Specificity P(¬B|¬A)", 0.0, 1.0, 0.95, 0.01)

posterior = bayes_theorem(prior, sensitivity, specificity)

st.write(f"### Posterior Probability P(A|B): {posterior:.4f}")

st.markdown("""
**Interpretation:**
- A high **specificity** (low false positive rate) increases confidence in a positive test.
- A low **prevalence** makes a positive result less reliable.
""")