import random
import sys
import ctypes

def enable_windows_ansi_support():
    if sys.platform.startswith('win32'):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
enable_windows_ansi_support()

def colored(color, text):
    
    """
    Use it to color the terminal, recognizes between hexadecimal and RGB
    """
    if isinstance(color, tuple) and len(color) == 3:
        r, g, b = color
    elif isinstance(color, str) and len(color) == 6:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
    else:
        raise ValueError("Invalid color format")

    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def random_rgb_value():
    return tuple(random.randint(0, 255) for _ in range(3))

def get_restaurant_list():
    """Prompt the user to enter restaurant names and return a list of them."""
    restaurant_list = []
    print("Ingrese los nombres de los restaurantes. Deje en blanco y presione enter para terminar.")
    while True:
        color = random_rgb_value()
        restaurant_name = input(colored(color,"Nombre del restaurante: "))

        if restaurant_name == "":
            break
        restaurant_list.append(restaurant_name)
    return restaurant_list

def choose_random_restaurant(restaurant_list):
    """Choose and return a random restaurant from the list."""
    if not restaurant_list:
        return "No hay restaurantes en la lista."
    return random.choice(restaurant_list)

def main():
    restaurants = get_restaurant_list()
    chosen_restaurant = choose_random_restaurant(restaurants)
    print(f"Restaurante seleccionado: {chosen_restaurant}")

if __name__ == "__main__":
    main()
