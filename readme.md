Disco Party App

Ez a program egy szórakoztató alkalmazás, amely egy diszkópartit szimulál animált GIF-ekkel és változó háttérszínekkel.
Python és a Tkinter könyvtár segítségével készült a GUI-hoz.

Modulok és Függvények
gif_handler_gd.py
    GifHandlerGD: osztály
        __init__(self, gif_files): Inicializálja a kezelőt egy GIF fájlok listájával.
        load_random_gif_GD(self): Betölt egy véletlenszerű GIF-et és átméretezi, hogy beleférjen a 750x750 pixeles méretbe.
        get_next_frame_GD(self): Visszaadja az aktuálisan betöltött GIF következő képkockáját.
disco_effect_gd.py
    Függvények
        get_random_color_gd(): Véletlenszerű színt generál hexadecimális formátumban.
main.py
    DiscoAppGD
    __init__(self, root): Inicializálja a fő alkalmazást a root Tkinter ablak segítségével.
    start_party_gd(self): Be- és kikapcsolja a party módot.
    change_color_gd(self): Véletlenszerűen változtatja a háttérszíneket, ha party módban van.
    update_title_gd(self): Animálja az ablak címét.
    animate_gif_gd(self): Animálja a betöltött GIF-et.

Hogyan futtassuk
Győződj meg róla, hogy a Python és a Pillow Modul telepítve van!!!
Futtasd a main.py fájlt az alkalmazás indításához.