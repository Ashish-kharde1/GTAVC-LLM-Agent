import subprocess
import json

def decide_action(ascii_scene: str, reached: bool) -> str:
    """
    Send the ASCII scene to Ollama, ask it to:
      1) find the nearest car,
      2) give exactly one action from ["forward","backward","left","right","enter","stop"]
    If `reached` is True, switch objective to "drive".
    """
    system = "You are playing GTA Vice City. You see the scene below in ASCII art."
    if not reached:
        user = (
            f"{ascii_scene}\n\n"
            "Objective: reach the nearest visible vehicle and enter it.\n"
            "Allowed actions: forward, backward, left, right, enter, stop.\n"
            "First output the rough compass direction to the nearest car (e.g. 'north‑east'),\n"
            "then output exactly one action keyword from the allowed list.\n"
            "Provide output as JSON: {\"direction\": \"…\", \"action\": \"…\"}."
        )
    else:
        user = (
            f"{ascii_scene}\n\n"
            "Objective: you are inside the vehicle. Drive safely and explore.\n"
            "Allowed actions: forward, brake, left, right, stop.\n"
            "Provide exactly one action keyword as JSON: {\"action\": \"…\"}."
        )
    print("proc 1 done")
    # Combine system and user prompts since --system/--user are not supported
    full_prompt = system + "\n\n" + user
    proc = subprocess.run(
        ["ollama", "run", "deepseek-r1:1.5b", full_prompt],
        capture_output=True, text=True
    )
    print("proc 2 done")
    if proc.returncode != 0:
        raise RuntimeError(f"Ollama error: {proc.stderr}")
    # Extract JSON from output
    import re
    match = re.search(r'\{.*?\}', proc.stdout, re.DOTALL)
    if not match:
        raise RuntimeError(f"No JSON found in Ollama output: {proc.stdout}")
    return json.loads(match.group(0))
