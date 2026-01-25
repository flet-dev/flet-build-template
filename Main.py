import flet as ft

def main(page: ft.Page):
    page.title = "King Messenger"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0e1621"
    
    page.appbar = ft.AppBar(
        title=ft.Text("King Messenger", weight="bold"),
        bgcolor="#242f3d",
        center_title=True
    )
    
    page.add(
        ft.Column([
            ft.Container(height=20),
            ft.Row([ft.CircleAvatar(content=ft.Text("K"), radius=40)], alignment="center"),
            ft.Row([ft.Text("King Messengerga xush kelibsiz!", size=20, weight="bold")], alignment="center"),
            ft.ListView(expand=True, spacing=10, controls=[
                ft.ListTile(leading=ft.Icon(ft.icons.CHAT), title=ft.Text("Chatlar")),
                ft.ListTile(leading=ft.Icon(ft.icons.HISTORY), title=ft.Text("Stories")),
            ])
        ], expand=True)
    )

ft.app(target=main)

