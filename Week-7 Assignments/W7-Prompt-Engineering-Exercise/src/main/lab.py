import json

# Optional: only needed if you're calling a model programmatically instead of
# pasting into a chat window. See config.json and the README for that path.
def call_model(prompt, message):
    raise NotImplementedError("Optional - connect this only if you have your own API access")


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

    # TO DO: Record what your AI assistant returned
    # Your task: For each prompt version, run the prompt against at least 2 of
    # the 5 sample messages using your AI assistant of choice (chat window, or
    # call_model() if you have your own API access). Paste the raw response
    # text you got back into RESULTS below, keyed by prompt version and
    # message id.
    #
    # Example:
    # RESULTS = {
    #     "zero_shot": {1: '{"order_id": "48213", ...}', 2: '...'},
    #     "multi_shot": {1: '...', 2: '...'},
    #     "constrained": {1: '...', 2: '...'},
    # }
    RESULTS = {
        "zero_shot": {},
        "multi_shot": {},
        "constrained": {},
    }

    for name, prompt in prompts.items():
        print(f"\n--- {name} ---")
        for msg in messages[:2]:
            result = RESULTS.get(name, {}).get(msg["id"], "(not filled in yet)")
            print(f"Message {msg['id']}: {result}")

    print("\n✅ Extraction Run Completed!")


if __name__ == "__main__":
    run_extraction()
