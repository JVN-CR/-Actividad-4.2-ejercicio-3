import flet as ft
from gui.login import mostrar_login


def main(page: ft.Page):
    page.title = "Clínica Veterinaria"
    page.window.width = 1200
    page.window.height = 780
    page.padding = 0
    page.bgcolor = "#EAF2FF"
    page.theme_mode = ft.ThemeMode.LIGHT

    mostrar_login(page)


if __name__ == "__main__":
    ft.run(main)
