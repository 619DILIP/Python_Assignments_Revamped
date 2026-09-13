import json

# TO DO: Wire up whichever AI tool/model you have access to here.
# Your task: Replace this stub with a real call to your model provider using
# the values in config.json.
def call_model(prompt, message):
    raise NotImplementedError("Connect this to your AI tool of choice")


def load_messages():
    with open(r"src/data/support_messages.json", encoding="utf-8") as f:
        return json.load(f)


def run_extraction():
    messages = load_messages()

    # TO DO: Write your zero-shot prompt
    # Your task: Ask the model to extract order_id, issue, item, order_date,
    # and contact_email as JSON, with no examples given, just clear instructions.
    zero_shot_prompt = """
    # your zero-shot prompt here
    """

    # TO DO: Write your multi-shot prompt
    # Your task: Rewrite the prompt to include 2-3 worked examples
    # (input message -> correct JSON output) before asking it to process a new message.
    multi_shot_prompt = """
    # your multi-shot prompt here, including 2-3 examples
    """

    # TO DO: Write your constrained prompt
    # Your task: Take either version above and add explicit constraints -
    # exact JSON key names, what to output when a field is missing (e.g. null),
    # and no extra commentary outside the JSON.
    constrained_prompt = """
    # your constrained prompt here
    """

    prompts = {
        "zero_shot": zero_shot_prompt,
        "multi_shot": multi_shot_prompt,
        "constrained": constrained_prompt,
    }

    # TO DO: Run all three prompt versions against the sample messages
    # Your task: For each prompt version, call the model against at least 2 of
    # the 5 sample messages and print the results so you can compare them.
    for name, prompt in prompts.items():
        print(f"\n--- {name} ---")
        for msg in messages[:2]:
            # result = call_model(prompt, msg["message"])
            # print(result)
            pass

    print("\n✅ Extraction Run Completed!")


if __name__ == "__main__":
    run_extraction()
