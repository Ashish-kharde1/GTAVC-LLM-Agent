import time
from screen_capture import capture_frame
from ascii_converter import to_ascii
from llm_agent import decide_action
from action_executor import execute_action

def main():
    reached_vehicle = False
    print("Launching GTA LLM agent…")
    time.sleep(2)  # give you time to alt‑tab into the game

    while True:
        frame = capture_frame()
        ascii_scene = to_ascii(frame, new_width=80)
        print("screen captured")


        # ask LLM what to do
        print("llm running")
        resp = decide_action(ascii_scene, reached_vehicle)
        print("llm done")
        action = resp.get("action")
        direction = resp.get("direction")  # you'll see it in logs

        print(f"[LLM] Direction: {direction}  → Action: {action}")

        execute_action(action)
        time.sleep(0.1)

        # once we “enter” the car, switch mode
        if action == "enter" and not reached_vehicle:
            reached_vehicle = True
            print("✅ Entered vehicle — now driving mode.")

        # optional: break if you press ESC
        # if keyboard.is_pressed('esc'):
        #     print("Esc pressed, exiting.")
        #     break

if __name__ == "__main__":
    main()
