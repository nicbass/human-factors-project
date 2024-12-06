import XInput

# Test controller connection
state = XInput.get_state(0)
print(state)  # Should print controller state if connected

# Test vibration
XInput.set_vibration(0, 1.0, 1.0)  # Max vibration
input("Press Enter to stop vibration...")
XInput.set_vibration(0, 0.0, 0.0)  # Stop vibration
