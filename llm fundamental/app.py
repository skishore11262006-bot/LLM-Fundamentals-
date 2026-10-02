import ollama

MODEL = "qwen2.5:0.5b"


def ask_llm(prompt, system_prompt="", temperature=0.3):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temperature
        }
    )

    return response["message"]["content"]


def zero_shot_demo():

    prompt = "Explain Artificial Intelligence in simple words."

    answer = ask_llm(
        prompt,
        system_prompt="You are a helpful AI teacher.",
        temperature=0.3
    )

    print("\n--- ZERO SHOT ---")
    print(answer)


def few_shot_demo():

    prompt = """
Example 1:
Input: Python
Output: Programming Language

Example 2:
Input: Java
Output: Programming Language

Example 3:
Input: Mango
Output:
"""

    answer = ask_llm(
        prompt,
        system_prompt="Classify the input based on the examples.",
        temperature=0.2
    )

    print("\n--- FEW SHOT ---")
    print(answer)


def role_prompt_demo():

    prompt = "Explain neural networks."

    answer = ask_llm(
        prompt,
        system_prompt="""
You are an AI instructor.
Explain technical concepts to a beginner.
Use simple language and examples.
""",
        temperature=0.3
    )

    print("\n--- ROLE PROMPT ---")
    print(answer)


def temperature_demo():

    prompt = "Write a creative description of an AI robot."

    print("\n--- LOW TEMPERATURE ---")

    answer1 = ask_llm(
        prompt,
        temperature=0.1
    )

    print(answer1)

    print("\n--- HIGH TEMPERATURE ---")

    answer2 = ask_llm(
        prompt,
        temperature=1.0
    )

    print(answer2)


def main():

    print("=" * 60)
    print("       LLM FUNDAMENTALS PLAYGROUND")
    print("=" * 60)

    while True:

        print("""
1. Zero-shot prompting
2. Few-shot prompting
3. Role/System prompting
4. Temperature experiment
5. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            zero_shot_demo()

        elif choice == "2":
            few_shot_demo()

        elif choice == "3":
            role_prompt_demo()

        elif choice == "4":
            temperature_demo()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()