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

    proc = subprocess.run(
        ["ollama", "generate", "llama2", "--system", system,
         "--user", user, "--json"],
        capture_output=True, text=True
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Ollama error: {proc.stderr}")
    return json.loads(proc.stdout)
