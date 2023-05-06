import flet as ft

def main(page: ft.Page):
    page.title = "Mini-Mentes"
    page.theme_mode = "LIGHT"
    page.window_maximized = True
    # page.window_full_screen = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        [
                            ft.Text("Selecciona una Materia", size=40, weight=ft.FontWeight.W_900, selectable=True)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,expand=1
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(width=300,height=500,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=4),on_click=lambda _: page.go("/Biologia"),content=ft.Image(src=f"/images/Biologia2.png",border_radius=ft.border_radius.all(10))),
                            ft.ElevatedButton(width=300,height=500,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=4),on_click=lambda _: page.go("/Matematicas"),content=ft.Image(src=f"/images/Matematicas2.png",border_radius=ft.border_radius.all(10))),
                            ft.ElevatedButton(width=300,height=500,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=4),on_click=lambda _: page.go("/Geografia"),content=ft.Image(src=f"/images/Geografia2.png",border_radius=ft.border_radius.all(10))),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.START,expand=4
                    )
                ],
            )
        )
        if page.route == "/Biologia":
            page.views.append(
                ft.View(
                    "/Biologia",
                    [
                       ft.Row(
                            [
                                ft.Text("Biología", size=40, weight=ft.FontWeight.W_900, selectable=True)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,expand=1,vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="green",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=125,content=ft.Text(value="4°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="blue",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=250,content=ft.Text(value="5°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="red",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=375,content=ft.Text(value="6°",size=40,weight=ft.FontWeight.W_400)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END,expand=3
                        ),
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                    icon_color="black",
                                    icon_size=60,
                                    tooltip="Atrás",
                                    on_click=lambda _: page.go("/")
                                ),
                            ],alignment=ft.MainAxisAlignment.START,expand=1,vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ],
                )
            )
        elif page.route == "/Matematicas":
            page.views.append(
                ft.View(
                    "/Matematicas",
                    [
                        ft.Row(
                            [
                                ft.Text("Matemáticas", size=40, weight=ft.FontWeight.W_900, selectable=True)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,expand=1,vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="green",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=125,content=ft.Text(value="4°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="blue",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=250,content=ft.Text(value="5°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="red",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=375,content=ft.Text(value="6°",size=40,weight=ft.FontWeight.W_400)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END,expand=3
                        ),
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                    icon_color="black",
                                    icon_size=60,
                                    tooltip="Atrás",
                                    on_click=lambda _: page.go("/")
                                ),
                            ],alignment=ft.MainAxisAlignment.START,expand=1, vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ],
                )
            )
        elif page.route == "/Geografia":
            page.views.append(
                ft.View(
                    "/Geografia",
                    [
                        ft.Row(
                            [
                                ft.Text("Geografía", size=40, weight=ft.FontWeight.W_900, selectable=True)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,expand=1,vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="green",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=125,content=ft.Text(value="4°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="blue",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=250,content=ft.Text(value="5°",size=40,weight=ft.FontWeight.W_400)),
                                ft.ElevatedButton(on_click=lambda _: page.go("/Pregunta"),style=ft.ButtonStyle(bgcolor="red",color="white",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=375,content=ft.Text(value="6°",size=40,weight=ft.FontWeight.W_400)),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END,expand=3
                        ),
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                    icon_color="black",
                                    icon_size=60,
                                    tooltip="Atrás",
                                    on_click=lambda _: page.go("/")
                                ),
                            ],alignment=ft.MainAxisAlignment.START,expand=1,vertical_alignment=ft.CrossAxisAlignment.END
                        )
                    ],
                )
            )
        elif page.route == "/Pregunta":
            page.views.append(
                ft.View(
                    "/Pregunta",
                    [
                        ft.Row(
                            [
                                ft.Text("Pregunta 1", size=30, weight=ft.FontWeight.W_900, selectable=True)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,expand=2,vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                ft.OutlinedButton(style=ft.ButtonStyle(bgcolor="white",color="black",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=80,content=ft.Text(value="Opción 1",size=30,weight=ft.FontWeight.W_400)),
                                ft.OutlinedButton(style=ft.ButtonStyle(bgcolor="white",color="black",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=80,content=ft.Text(value="Opción 2",size=30,weight=ft.FontWeight.W_400)),
                                ft.OutlinedButton(style=ft.ButtonStyle(bgcolor="white",color="black",shape=ft.RoundedRectangleBorder(radius=10)),width=300,height=80,content=ft.Text(value="Opción 3",size=30,weight=ft.FontWeight.W_400)),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.START,expand=3
                        )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
ft.app(target=main,assets_dir="assets")