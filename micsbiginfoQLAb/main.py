from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
import tkinter as tk
import threading

# GUI ablak létrehozása
root = tk.Tk()
root.title("QLab Big Info Monitor")
root.geometry("800x200")
root.configure(bg="black")

# Feliratok
labels = {
    "name"     : tk.Label(root, text="Cue: ---", font=("Helvetica", 16), fg="white", bg="black"),
    "clock"    : tk.Label(root, text="00:00:00", font=("Courier", 16), fg="lime", bg="black"),
    "elapsed"  : tk.Label(root, text="Eltelt: 0.0 s", font=("Helvetica", 36), fg="orange", bg="black"),
    "remaining": tk.Label(root, text="Visszavan: 0.0 s", font=("Helvetica", 36), fg="red", bg="black")
}

# Elhelyezés
labels["name"].pack(pady=5)
labels["clock"].pack(pady=5)
labels["elapsed"].pack(pady=2)
labels["remaining"].pack(pady=2)


def parse_time_to_seconds(time_str):
    """Konvertálja az időformátumot egységes hh:mm:ss formátumra"""
    parts = time_str.split(':')

    if len(parts) == 3:  # h:m:s - már jó formátum
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
        return f"{hours:02d}:{minutes:02d}:{seconds:05.2f}"
    elif len(parts) == 2:  # m:s - kiegészítjük órával
        minutes = int(parts[0])
        seconds = float(parts[1])
        return f"00:{minutes:02d}:{seconds:05.2f}"
    else:  # csak másodperc - kiegészítjük órával és perccel
        seconds = float(parts[0])
        return f"00:00:{seconds:05.2f}"


# OSC callback függvények
def osc_display_name(address, *args):
    if args:
        labels["name"].config(text=f"Cue: {args[0]}")


def osc_display_clock(address, *args):
    if args:
        labels["clock"].config(text=args[0])


def osc_display_elapsed(address, *args):
    if args:
        labels["elapsed"].config(text=f"Eltelt: {parse_time_to_seconds(args[0])} s")


def osc_display_remaining(address, *args):
    if args:
        labels["remaining"].config(text=f"Visszavan: {parse_time_to_seconds(args[0])} s")


# OSC szerver külön szálon
def start_osc_server():
    dispatcher = Dispatcher()
    dispatcher.map("/displayName", osc_display_name)
    dispatcher.map("/displayClock", osc_display_clock)
    dispatcher.map("/displayElapsed", osc_display_elapsed)
    dispatcher.map("/displayRemaining", osc_display_remaining)

    server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", 8000), dispatcher)
    print("OSC szerver fut a 8000-es porton…")
    server.serve_forever()


# Indítás külön szálon
threading.Thread(target=start_osc_server, daemon=True).start()

# GUI futtatása
root.mainloop()
